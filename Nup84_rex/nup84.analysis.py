
import IMP
import IMP.core
import IMP.base
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.em
import IMP.pmi.restraints.crosslinking
import IMP.pmi.representation as representation
import IMP.pmi.tools as tools
import IMP.pmi.samplers as samplers
import IMP.pmi.output as output

import os,sys
import numpy

root='/veena1/home/pellarin/'

'''
datadir=root+"/Dropbox/eif3/IMP/data/"
pdbdir=root+"/Dropbox/eif3/pdbs/"
sequencedir=root+"/Dropbox/eif3/Sequence/"
bigj_ac_40s=False



simo = representation.SimplifiedModel(m,upperharmonic=True,disorderedlength=True)

if bigj_ac_40s:
   execfile("bigj.topology.py")
   execfile("ac.topology.py")
   execfile("40s.topology.py")
else:
   #construct big
   execfile("big.topology.py")
   execfile("rigid_bodies_big.py")
'''

m = IMP.Model()

def fix_rmf(name):
    
    nname = os.path.splitext(name)[0] + ".new.rmf3"
    old = RMF.open_rmf_file_read_only(name)
    new = RMF.create_rmf_file(nname)
    RMF.clone_hierarchy(old, new)
    RMF.clone_static_frame(old, new)
    cat = new.get_category("IMP")
    k = new.get_key(cat, "rigid body index", RMF.int_traits)
    cur = 0
    for nid in new.get_node_ids():
        n = new.get_node(nid)
        if n.get_static_value(k) is not None:
            print "patched from", n.get_static_value(k), "to", cur
            n.set_static_value(k, cur)
            cur += 1
    for f in old.get_frames():
        old.set_current_frame(f)
        new.add_frame(
            old.get_current_frame_name(),
            old.get_current_frame_type())
        RMF.clone_loaded_frame(old, new)
    os.rename(nname,name)


class OutputDatabase():
   def __init__(self, files,sliceevery=10):
       mm=0
       self.pointer={}
       self.pointer_iterator=[]       
       for j in files:
           fieldlist=[]
           po=output.ProcessOutput(j)

           for k in po.get_keys():
               if "ISDCrossLinkMS_Distance_" in k: fieldlist.append(k)
               if "ISDCrossLinkMS_Sigma_" in k: fieldlist.append(k)
               if "ISDCrossLinkMS_Psi_" in k: fieldlist.append(k)
               
           allfields=po.get_fields(["rmf_file"]+fieldlist,filterout="None")
  
           
           for n,e in enumerate(allfields["rmf_file"]):
             if e!=None:
                if mm % sliceevery==0:       
                   tmp_dict={}
       
                   for k in allfields:
                       tmp_dict[k]=allfields[k][n]
                
                   self.pointer[mm]=tmp_dict               
                   self.pointer_iterator.append(mm)
                mm+=1
           

           
   def get_item(self,index):
       tmp_dict=self.pointer[index]
       tmp_list=[float(tmp_dict[name]) for name in sorted(tmp_dict.keys()) if name != "rmf_file"] 
       return tmp_list

   def get_items(self,indexes):
       return [self.get_item(i) for i in indexes]

       
   def get_rmf_file(self,index):
       return self.pointer[index]["rmf_file"]
       
   def get_rmf_files(self,indexes):
       return [self.get_rmf_file(i) for i in indexes]
     
   def get_iterator(self):
       return self.pointer_iterator
       
   def get_labels(self):
       tmp_dict=self.pointer[0]
       tmp_list=[name for name in sorted(tmp_dict.keys()) if name != "rmf_file"] 
       labels=[l.replace("ISDCrossLinkMS_Distance_","")
                .replace("intrarb-","")
                .replace("interrb-","")
                .replace("_None","")
                .replace("10-10-","")
                .replace("0.1","L")
                .replace("0.05","M")
                .replace("0.01","H")
                .replace("eIF3","") for l in tmp_list]
       return labels
   
   def get_nframes(self):
       return len(self.pointer_iterator)
   
   def get_ncrosslinks(self):
       return len(self.get_item(0))

class ClusterByCrossLink():
 
 def __init__(self,filelist,sliceframe=10,tolerancepercrosslink=1.0):
   clusters={}
   od=OutputDatabase(filelist,sliceframe)
   self.od=od
   self.nframes=self.od.get_nframes()
   ncrosslinks=self.od.get_ncrosslinks()
   #first stupid clustering
   for mm in self.od.get_iterator():
       item=self.od.get_item(mm)
       if len(clusters.keys())==0: clusters[len(clusters.keys())+1]=[mm]

       else:
          assigned=False
          for n in clusters.keys():
              dist = numpy.linalg.norm(numpy.array(self.od.get_item(clusters[n][0]))-numpy.array(item))
              #print dist,len(clusters.keys()),[(mm,len(clusters[m])) for mm in clusters]       
              if dist<=tolerancepercrosslink*ncrosslinks:
                 assigned=True
                 clusters[n].append(mm)
                 break
          if assigned==False:
             clusters[len(clusters.keys())+1]=[mm]
             
   #merge clusters
   #delta cluster indicates whether the number of clusters didn;t change in the last iteration
   deltaclusters=1
   from itertools import combinations
   while deltaclusters!=0:
     meanlist={}
     nclustersold=len(clusters.keys())
     for k in clusters.keys():
       print k,len(clusters[k])
       clusteritem=[self.od.get_item(mm) for mm in clusters[k]]
       meanlist[k]=list(numpy.mean(numpy.array(clusteritem),axis=0))

     mergedclusters=clusters


     for a, b in combinations(meanlist.keys(), 2):
       if a not in mergedclusters:continue
       if b not in mergedclusters:continue    
       dist = numpy.linalg.norm(numpy.array(meanlist[a])-numpy.array(meanlist[b]))
       if dist<=tolerancepercrosslink*ncrosslinks:
          mergedclusters[a]+=clusters[b]
          mergedclusters.pop(b)
          print "merged",len(mergedclusters[a])

     clusters=mergedclusters
     nclusters=len(clusters.keys())
     print "merge", nclustersold-nclusters  
     deltaclusters=nclustersold-nclusters
  
   self.clusters=clusters

 def get_clusters(self):
   return self.clusters
 
 def get_largest_cluster_key(self):
   clusterkeys=get_largest_clusters(self,nclusters=1,population_filter=0)
   return clusterkeys[0]

 def get_rmf_files_largest_cluster(self):
   return self.od.get_rmf_files(self.clusters[self.get_largest_cluster_key()])  
 
 def get_largest_cluster_keys(self,nclusters=1,population_filter=0.1):
   #this function select the clusters according to the size rank and the population
   size_cluster_list=[]
   for k in self.clusters:
       size_cluster_list.append((len(self.clusters[k]),k))
   sorted_size_cluster_list = sorted(size_cluster_list, key=lambda tup: tup[0])
   cluster_keys=[]
   for item in sorted_size_cluster_list:
       if float(item[0])/self.nframes>=population_filter:
          cluster_keys.append(item[1])
   return cluster_keys         
 
 def get_rmf_files(self,clusterkey):
   return self.od.get_rmf_files(self.clusters[clusterkey])  


dirname="./"
basedir="./"+dirname
#allfilteredfields={}
filelist=[basedir+"stat."+j+".out" for j in ["0","1","2","3","4","5","6","7"]]
#filelist=[basedir+"stat."+j+".out" for j in ["0"]]

cbxl=ClusterByCrossLink(filelist,10,tolerancepercrosslink=0.5)
                        
#clusterize

nframes=cbxl.od.get_nframes()
ncrosslinks=cbxl.od.get_ncrosslinks()

#calculate the density for all frames
import RMF
import IMP.rmf
import IMP.em
import shutil

def get_particles(prot,align_molecules):
    particle_dict={}
    allparticles=[]
    for c in prot.get_children():
        name=c.get_name()
        particle_dict[name]=IMP.atom.get_leaves(c)
        for s in c.get_children():
            if "_Res:1" in s.get_name() and "_Res:10" not in s.get_name(): 
                allparticles+=IMP.atom.get_leaves(s)
            if "Beads" in s.get_name():
                allparticles+=IMP.atom.get_leaves(s)
          
    particle_align=[]
    for name in particle_dict:
        particle_dict[name]=IMP.pmi.tools.sort_by_residues(list(set(particle_dict[name]) & set(allparticles)))
        if name in align_molecules:
            particle_align+=particle_dict[name]
    
    #for p in particle_align:
    #    print p.get_name()
    
    #for name in particle_dict:
    #    for p in particle_dict[name]:
    #        print name, p.get_name()
    
    return particle_align,particle_dict


align_molecules=["Nup145c","Seh1","Sec13","Nup85"]
do_calculate_density=True
do_fix_rmf=False

clusters=cbxl.get_clusters()
o=IMP.pmi.output.Output()

for ncl,key in enumerate(cbxl.get_largest_cluster_keys(nclusters=100,population_filter=0.1)):
  print cbxl.get_rmf_files(key)
  dircluster=dirname+"cluster."+str(ncl)+"/"
  
  inputlist=[list(l) for l in zip(*cbxl.od.get_items(clusters[key]))]
  if not os.path.exists(dircluster): os.makedirs(dircluster)
  output.plot_fields_box_plots(dircluster+"crosslinks",inputlist,range(len(inputlist)),xlabels=cbxl.od.get_labels())
  
  if do_calculate_density:
    for n,rmfname in enumerate(cbxl.get_rmf_files(key)):
       
        print n, rmfname,len(cbxl.get_rmf_files(key))
        if do_fix_rmf:
          fix_rmf(basedir+rmfname)
        new_rmfname=rmfname.replace("/","_")
        shutil.copy(basedir+rmfname,dircluster+new_rmfname)
        rh= RMF.open_rmf_file_read_only(basedir+rmfname)
        prot=IMP.rmf.create_hierarchies(rh, m)[0]
        IMP.rmf.link_hierarchies(rh, [prot])        
        IMP.rmf.load_frame(rh, 0)        
        m.update()

        if n==0:
          dmap_dict={}

          particle_align,particle_dict=get_particles(prot,align_molecules)
                        
          xyzs_ref=[IMP.core.XYZ(p).get_coordinates() for p in particle_align]
          
          for name in particle_dict:
              dmap_dict[name]=IMP.em.SampledDensityMap(particle_dict[name],1.0,2)
        else:          
          particle_align,particle_dict=get_particles(prot,align_molecules)

          xyzs=[IMP.core.XYZ(p).get_coordinates() for p in particle_align]    
          transformation=IMP.algebra.get_transformation_aligning_first_to_second(xyzs,xyzs_ref)
          rbs=[]
          for name in particle_dict:
              for p in particle_dict[name]: 
                  if IMP.core.RigidBody.particle_is_instance(p):
                     rb=IMP.core.RigidMember(p).get_rigid_body()
                     if rb not in rbs:
                        rbs.append(rb)
                        IMP.core.transform(rb,transformation)
                  else:
                     IMP.core.transform(IMP.core.XYZ(p),transformation)
              sdm=IMP.em.SampledDensityMap(particle_dict[name],1.0,2)
              dmap_dict[name].add(sdm)                  
              #IMP.em.add_to_map(dmap_dict[name],particle_dict[name])
              
          #IMP.atom.write_pdb_of_c_alphas(prot,str(n)+".pdb")

        o.init_pdb(dircluster+str(n)+".pdb",prot)        
        o.write_pdb(dircluster+str(n)+".pdb")
        #IMP.atom.write_pdb_of_c_alphas(prot,str(n)+".pdb")          

    for name in particle_dict:    
      IMP.em.write_map(dmap_dict[name],dircluster+"all."+name+".mrc",IMP.em.MRCReaderWriter())
    
    
    




   
