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

import os

rbmaxtrans = 1.00   # rigid body maximum translation, in Angstrom
fbmaxtrans = 1.00   # floppy body maximum translation, in Angstrom (floppy bodies a re the flexible beads)
rbmaxrot=0.025      # rigid body maximum rotation, in radiant
nrmffiles=1000      # number of rmf directories (group.0, group.1, ...)
nframes=100         # number of rmf files per rmf directory (group.0, group.1, ...)
nsteps=100          # number of Monte Carlo step between each rmf saving
outputobjects = []  # list of object that are producing output and dumped in a log file
sampleobjects = []  # the object that are sampled by Monte Carlo

m = IMP.Model()
simo = IMP.pmi.representation.SimplifiedModel(m,upperharmonic=True,disorderedlength=True)

execfile("nup84.topology.py")

#simo.translate_hierarchies_to_reference_frame(Nup84_complex)
simo.shuffle_configuration(200)  # randomize the initial coordinates within a box of 200 Angstroms
#simo.translate_hierarchies(Nup84_complex,(100,100,100))

simo.set_rigid_bodies_max_rot(rbmaxrot)   
simo.set_floppy_bodies_max_trans(fbmaxtrans)
simo.set_rigid_bodies_max_trans(rbmaxtrans)
simo.set_floppy_bodies()
simo.setup_bonds()        # just for display, not important

prot = simo.prot
outputobjects.append(simo)  # because we want to have the log of the model
sampleobjects.append(simo)  # because we want to sample the coordinates

# Excluded Volume
ev = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(simo,resolution=10)
ev.add_to_model()
outputobjects.append(ev) # because we want to have the log of the excluded volume

# Cross Linking data

# Dictionary to parse correctly the columns of a cross-link data file
columnmap={}
columnmap["Protein1"]=0
columnmap["Protein2"]=2
columnmap["Residue1"]=1
columnmap["Residue2"]=3
columnmap["IDScore"]=4

ids_map=IMP.pmi.tools.map()        
ids_map.set_map_element(1.0,1.0) # a dictionary to classify the cross-links
                                 # here we have only one class

xl1 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   'data/yeast_Nup84_DSS.dat',
                                   length=21.0,                # maximum expected distance for DSS cross-links
                                   slope=0.02,                 # slope for a linear reastraint that is added on top of 
                                                               # the cross-link restraint: I need that to create a funnel
                                   columnmapping=columnmap,    
                                   ids_map=ids_map,
                                   resolution=1.0,
                                   label="DSS")
xl1.add_to_model()
sampleobjects.append(xl1)
outputobjects.append(xl1)

xl2 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo, 
                                   'data/EDC_XL_122013.dat',
                                   length=12.0,
                                   slope=0.02,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,
                                   resolution=1.0,
                                   label="EDC")
xl2.add_to_model()
sampleobjects.append(xl2)
outputobjects.append(xl2)

# short optimization to relax the flexible beads, having the rigid bodies fixed in the space

simo.optimize_floppy_bodies(1000)

'''
# Em restraint

gem = IMP.pmi.restraints.em.GaussianEMRestraint(resdensities,'data/emd_5151.map.gmm.txt')
gem.add_to_model()
outputobjects.append(gem)
sampleobjects.append(gem)
'''


# Sampling: setting up the sampling objects

mc = IMP.pmi.samplers.MonteCarlo(m,sampleobjects, 1.0) # initilize the monte carlo at temperature=1.0
mc.set_label("mc")
outputobjects.append(mc)

rex= IMP.pmi.samplers.ReplicaExchange(m,1.0,2.5,mc)  # replica exchange lower temperature=1, max temperature =2.5
myindex=rex.get_my_index()                         # this is the index of the replica exchange
outputobjects.append(rex)

# Log and output rmf and pdb preparation

sw = IMP.pmi.tools.Stopwatch()   # to see performance we measure elasped time between each coordinate saving
outputobjects.append(sw)

output = IMP.pmi.output.Output()
output.init_stat2("stat."+str(myindex)+".out", outputobjects, 
                  extralabels=["rmf_file"])                                 # this is the log file
output.init_pdb_best_scoring("pdbs/models",prot,500,replica_exchange=True)  # this set the directory that 
                                                                            # contains the 500 best scoring conformations
                                                                            # into pdb files (for the lowest temperature)
                                                                            # the names are assigned at run time
output.init_rmf("initial."+str(myindex)+".rmf3", [prot])                    
output.add_restraints_to_rmf("initial."+str(myindex)+".rmf3",[xl1,xl2])
output.write_rmf("initial."+str(myindex)+".rmf3",0)
output.close_rmf("initial."+str(myindex)+".rmf3")


# actual production run

for k in range(nrmffiles):
  rmfdir="rmfs/group."+str(k)
  
  for i in range(nframes):
    mc.run(nsteps)
    score=m.evaluate(False)
    rmfname="None"
    if rex.get_my_temp()==1.0:
       if not os.path.exists(rmfdir):
          os.makedirs(rmfdir)
       output.write_pdb_best_scoring(score)
       rmfname=rmfdir+"/"+str(i)+".rmf3"
       output.init_rmf(rmfname, [prot])
       output.add_restraints_to_rmf(rmfname,[xl1,xl2])
       output.write_rmf(rmfname,0)
       output.close_rmf(rmfname)

    output.set_output_entry("rmf_file",rmfname)
    #output.set_output_entry("rmf_frame_index",i)
    
    output.write_stats2() 
    rex.swap_temp(i,score)

