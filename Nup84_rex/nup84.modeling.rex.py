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

#simo.translate_hierarchies_to_reference_frame(Nup84_complex)
simo.shuffle_configuration(200)
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

simo.optimize_floppy_bodies(1000)

'''
gem = IMP.pmi.restraints.em.GaussianEMRestraint(resdensities,'data/emd_5151.map.gmm.txt')
gem.add_to_model()
outputobjects.append(gem)
sampleobjects.append(gem)
'''

mc = IMP.pmi.samplers.MonteCarlo(m,sampleobjects, 1.0)
mc.set_label("mc")
outputobjects.append(mc)

rex= IMP.pmi.samplers.ReplicaExchange(m,1,2.5,mc)
myindex=rex.get_my_index()
outputobjects.append(rex)

sw = IMP.pmi.tools.Stopwatch()
outputobjects.append(sw)

output = IMP.pmi.output.Output()
output.init_stat2("stat."+str(myindex)+".out", outputobjects, 
                  extralabels=["rmf_file"])

try:
   os.mkdir("pdbs")
except:
   pass

try:
   os.mkdir("rmfs")
except:
   pass

output.init_pdb_best_scoring("pdbs/models",prot,500,replica_exchange=True)
output.init_rmf("initial."+str(myindex)+".rmf3", [prot])
output.add_restraints_to_rmf("initial."+str(myindex)+".rmf3",[xl1,xl2])
output.write_rmf("initial."+str(myindex)+".rmf3")
output.close_rmf("initial."+str(myindex)+".rmf3")

for k in range(nrmffiles):
  rmfdir="rmfs/group."+str(k)
  
  for i in range(nframes):
    mc.optimize(nsteps)
    score=m.evaluate(False)
    rmfname="None"
    if rex.get_my_temp()==1.0:
       if not os.path.exists(rmfdir):
          os.makedirs(rmfdir)
       output.write_pdb_best_scoring(score)
       rmfname=rmfdir+"/"+str(i)+".rmf3"
       output.init_rmf(rmfname, [prot])
       output.add_restraints_to_rmf(rmfname,[xl1,xl2])
       output.write_rmf(rmfname)
       output.close_rmf(rmfname)
       output.set_output_entry("rmf_file",rmfname)
       output.write_stats2() 
    #output.set_output_entry("rmf_frame_index",i)
    
    rex.swap_temp(i,score)
