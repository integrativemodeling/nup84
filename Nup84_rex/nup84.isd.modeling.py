import IMP
import IMP.core
import IMP.base
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi.restraints.crosslinking
import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.em
import IMP.pmi.restraints.basic
import IMP.pmi.representation
import IMP.pmi.tools
import IMP.pmi.samplers
import IMP.pmi.output
import IMP.pmi.macros

import os

rbmaxtrans = 2.00
fbmaxtrans = 2.00
rbmaxrot=0.04
nrmffiles=1000
nframes=100
nsteps=100
outputobjects = []
sampleobjects = []

m = IMP.Model()
#simo = IMP.pmi.representation.Representation(m,upperharmonic=True,disorderedlength=True)
simo = IMP.pmi.representation.Representation(m,upperharmonic=True,disorderedlength=False)

execfile("nup84.isd.topology.py")
total_mass=sum((IMP.atom.Mass(p).get_mass() for h in resdensities for p in IMP.atom.get_leaves(h)))
print 'total mass',total_mass

#simo.translate_hierarchies_to_reference_frame(Nup84_complex)
simo.shuffle_configuration(100)
#simo.translate_hierarchies(Nup84_complex,(100,100,100))

simo.set_rigid_bodies_max_rot(rbmaxrot)
simo.set_floppy_bodies_max_trans(fbmaxtrans)
simo.set_rigid_bodies_max_trans(rbmaxtrans)
simo.set_floppy_bodies()
simo.setup_bonds()

prot = simo.prot
outputobjects.append(simo)
sampleobjects.append(simo)


ev = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(simo,resolution=10)
ev.add_to_model()
outputobjects.append(ev)

eb = IMP.pmi.restraints.basic.ExternalBarrier(simo,radius=300)
eb.add_to_model()
outputobjects.append(eb)

# we apply a distance restraint between the 
# k = 1/(2*sigma*sigma) we use sigma=70 Angstroms
# kappa=0.00010204081632653061
# we got the distances from the Jeremy

print "IMP.pmi.restraints.basic.DistanceRestraint(simo,(510,510,Nup85), (211,211,Nup133), distancemin=329,distancemax=426,resolution=1)"
print "IMP.pmi.restraints.basic.DistanceRestraint(simo,(8,8,Nup120), (211,211,Nup133), distancemin=326,distancemax=435,resolution=1)"
print "IMP.pmi.restraints.basic.DistanceRestraint(simo,(8,8,Nup120), (510,510,Nup85), distancemin=213,distancemax=258,resolution=1)"

dr1= IMP.pmi.restraints.basic.DistanceRestraint(simo,(181,181,"Nup85"), (211,211,"Nup133"), distancemin=298.5,distancemax=426,resolution=1)
dr1.add_to_model()
dr1.set_label("Nup85_Nup133")
outputobjects.append(dr1)

dr2= IMP.pmi.restraints.basic.DistanceRestraint(simo,(8,8,"Nup120"), (211,211,"Nup133"), distancemin=294.5,distancemax=445,resolution=1)
dr2.add_to_model()
dr2.set_label("Nup120_Nup133")
outputobjects.append(dr2)

dr3= IMP.pmi.restraints.basic.DistanceRestraint(simo,(8,8,"Nup120"), (181,181,"Nup85"), distancemin=145,distancemax=268,resolution=1)
dr3.add_to_model()
dr3.set_label("Nup120_Nup85")
outputobjects.append(dr3)



columnmap={}
columnmap["Protein1"]=0
columnmap["Protein2"]=2
columnmap["Residue1"]=1
columnmap["Residue2"]=3
columnmap["IDScore"]=4
columnmap["XLUniqueID"]=5

ids_map=IMP.pmi.tools.map()
ids_map.set_map_element(1.0,1.0)

xl1 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   'data/yeast_Nup84_DSS.new.dat',
                                   length=21.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   label="DSS")
xl1.add_to_model()
sampleobjects.append(xl1)
outputobjects.append(xl1)
xl1.set_psi_is_sampled(False)
psi=xl1.get_psi(1.0)[0]
psi.set_scale(0.05)


xl2 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   'data/EDC_XL_122013.new.dat',
                                   length=16.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   label="EDC")
xl2.add_to_model()
sampleobjects.append(xl2)
outputobjects.append(xl2)
xl2.set_psi_is_sampled(False)
psi=xl2.get_psi(1.0)[0]
psi.set_scale(0.05)

print 'EVAL 1'
print m.evaluate(False)
simo.optimize_floppy_bodies(100)
print 'EVAL 2'
print m.evaluate(False)
mc1=IMP.pmi.macros.ReplicaExchange0(m,
                                    simo,
                                    sampleobjects,
                                    outputobjects,
                                    crosslink_restraints=[xl1,xl2],
                                    #crosslink_restraints=[xl1],
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=2.5,
                                    number_of_best_scoring_models=500,
                                    monte_carlo_steps=10,
                                    number_of_frames=30000,
                                    write_initial_rmf=True,
                                    initial_rmf_name_suffix="initial",
                                    stat_file_name_suffix="stat",
                                    best_pdb_name_suffix="model",
                                    do_clean_first=True,
                                    do_create_directories=True,
                                    global_output_directory="output.3",
                                    rmf_dir="rmfs/",
                                    best_pdb_dir="pdbs/",
                                    replica_stat_file_suffix="stat_replica")
mc1.execute_macro()
rex1=mc1.get_replica_exchange_object()
print 'EVAL 3'
print m.evaluate(False)
