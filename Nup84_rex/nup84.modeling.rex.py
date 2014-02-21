import IMP
import IMP.core
import IMP.base
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi.restraints.crosslinking
import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.em
import IMP.pmi.representation
import IMP.pmi.tools
import IMP.pmi.samplers
import IMP.pmi.output
import IMP.pmi.macros

import os

rbmaxtrans = 1.00
fbmaxtrans = 1.00
rbmaxrot=0.025
nrmffiles=1000
nframes=100
nsteps=100
outputobjects = []
sampleobjects = []

m = IMP.Model()
simo = IMP.pmi.representation.Representation(m,upperharmonic=True,disorderedlength=True)

execfile("nup84.topology.py")
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


columnmap={}
columnmap["Protein1"]=0
columnmap["Protein2"]=2
columnmap["Residue1"]=1
columnmap["Residue2"]=3
columnmap["IDScore"]=4

ids_map=IMP.pmi.tools.map()
ids_map.set_map_element(1.0,1.0)

xl1 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   'data/yeast_Nup84_DSS.dat',
                                   length=21.0,
                                   slope=0.02,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   label="DSS")
xl1.add_to_model()
sampleobjects.append(xl1)
outputobjects.append(xl1)

xl2 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   'data/EDC_XL_122013.dat',
                                   length=12.0,
                                   slope=0.02,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   label="EDC")
xl2.add_to_model()
sampleobjects.append(xl2)
outputobjects.append(xl2)

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
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=2.5,
                                    number_of_best_scoring_models=500,
                                    monte_carlo_steps=10,
                                    number_of_frames=100,
                                    write_initial_rmf=True,
                                    initial_rmf_name_suffix="initial",
                                    stat_file_name_suffix="stat",
                                    best_pdb_name_suffix="model",
                                    do_clean_first=True,
                                    do_create_directories=True,
                                    global_output_directory="pre-EM",
                                    rmf_dir="rmfs/",
                                    best_pdb_dir="pdbs/",
                                    replica_stat_file_suffix="stat_replica")
mc1.execute_macro()
rex1=mc1.get_replica_exchange_object()
print 'EVAL 3'
print m.evaluate(False)

gem = IMP.pmi.restraints.em.GaussianEMRestraint(resdensities,'data/emd_5151.map.mrc.gmm.2.txt',
                                               cutoff_dist_for_container=0.0,
                                                target_mass_scale=total_mass,
                                                target_radii_scale=3.0,
                                                model_radii_scale=3.0)
gem.add_to_model()
gem.set_weight(100.0)
gem.center_model_on_target_density()
outputobjects.append(gem)

print 'EVAL 4'
print m.evaluate(False)

mc2=IMP.pmi.macros.ReplicaExchange0(m,
                                    simo,
                                    sampleobjects,
                                    outputobjects,
                                    crosslink_restraints=[xl1,xl2],
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=5.0,
                                    number_of_best_scoring_models=500,
                                    monte_carlo_steps=10,
                                    number_of_frames=100000,
                                    write_initial_rmf=True,
                                    initial_rmf_name_suffix="initial",
                                    stat_file_name_suffix="stat",
                                    best_pdb_name_suffix="model",
                                    do_clean_first=True,
                                    do_create_directories=True,
                                    global_output_directory="post-EM",
                                    rmf_dir="rmfs/",
                                    best_pdb_dir="pdbs/",
                                    replica_stat_file_suffix="stat_replica",
                                    replica_exchange_object=rex1,
                                    em_object_for_rmf=gem)
mc2.execute_macro()
