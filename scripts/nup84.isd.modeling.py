from __future__ import print_function
import IMP
import IMP.core
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi.restraints.crosslinking
import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.em
import IMP.pmi.restraints.em2d
import IMP.pmi.restraints.basic
import IMP.pmi.restraints.proteomics
import IMP.pmi.representation
import IMP.pmi.tools
import IMP.pmi.samplers
import IMP.pmi.output
import IMP.pmi.macros

import os
import sys

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

exec(open("nup84.topology.py").read())

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
                                   '../data/yeast_Nup84_DSS.new.dat',
                                   length=21.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   filelabel="DSS",
                                   label="DSS")
xl1.add_to_model()
sampleobjects.append(xl1)
outputobjects.append(xl1)
xl1.set_psi_is_sampled(False)
psi=xl1.get_psi(1.0)[0]
psi.set_scale(0.05)


xl2 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   '../data/EDC_XL_122013.new.dat',
                                   length=16.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   filelabel="EDC",
                                   label="EDC")
xl2.add_to_model()
sampleobjects.append(xl2)
outputobjects.append(xl2)
xl2.set_psi_is_sampled(False)
psi=xl2.get_psi(1.0)[0]
psi.set_scale(0.05)

print('EVAL 1')
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))
simo.optimize_floppy_bodies(100)
print('EVAL 2')
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))

nframes=500
if '--test' in sys.argv: nframes=50
mc1=IMP.pmi.macros.ReplicaExchange0(m,
                                    simo,
                                    monte_carlo_sample_objects=sampleobjects,
                                    output_objects=outputobjects,
                                    crosslink_restraints=[xl1,xl2],
                                    #crosslink_restraints=[xl1],
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=2.5,
                                    number_of_best_scoring_models=50,
                                    monte_carlo_steps=10,
                                    number_of_frames=nframes,
                                    write_initial_rmf=True,
                                    initial_rmf_name_suffix="initial",
                                    stat_file_name_suffix="stat",
                                    best_pdb_name_suffix="model",
                                    do_clean_first=True,
                                    do_create_directories=True,
                                    global_output_directory="pre-2DEM_output.1",
                                    rmf_dir="rmfs/",
                                    best_pdb_dir="pdbs/",
                                    replica_stat_file_suffix="stat_replica")
mc1.execute_macro()

rex1=mc1.get_replica_exchange_object()
print('EVAL 3')
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))


# 2DEM restraints
images = ['../data/nup84_kinked_from_class2.pgm']

em2d = IMP.pmi.restraints.em2d.ElectronMicroscopy2D(simo,
                                                    images,
                                                    resolution=1.0,
                                                    pixel_size = 5.91,
                                                    image_resolution = 30.0,
                                                    projection_number = 400)
em2d.add_to_model()
em2d.set_weight(500)
outputobjects.append(em2d)

print('EVAL 4')
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))

nframes=5000
if '--test' in sys.argv: nframes=10
mc2=IMP.pmi.macros.ReplicaExchange0(m,
                                    simo,
                                    monte_carlo_sample_objects=sampleobjects,
                                    output_objects=outputobjects,
                                    crosslink_restraints=[xl1,xl2],
                                    #crosslink_restraints=[xl1],
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=2.5,
                                    number_of_best_scoring_models=500,
                                    monte_carlo_steps=10,
                                    number_of_frames=nframes,
                                    write_initial_rmf=True,
                                    initial_rmf_name_suffix="initial",
                                    stat_file_name_suffix="stat",
                                    best_pdb_name_suffix="model",
                                    do_clean_first=True,
                                    do_create_directories=True,
                                    global_output_directory="output.1",
                                    rmf_dir="rmfs/",
                                    best_pdb_dir="pdbs/",
                                    replica_stat_file_suffix="stat_replica",
                                    replica_exchange_object=rex1)
mc2.execute_macro()
