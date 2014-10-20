import IMP
import IMP.pmi
import IMP.pmi.analysis
import glob
import os

import IMP
import IMP.pmi
import IMP.pmi.macros

is_mpi=False  # set to True to run in parallel (requires mpi4py)

model=IMP.Model()

# perform the analysis

cm=IMP.pmi.analysis.CrossLinkTable()

model=IMP.Model()

cross_link="DSS"
cluster_directory="/salilab/park2/etjioe/clustering_0722_thres_300/clustering.clustering.3-xray-w500.40.0.40/"
cluster_number=1
cluster_assignment_file="cluster.dat"
pdb_file_names_file="xyz.pdblist"
original_directory_A='/salilab/park2/etjioe/em2d_run1/after_merging/3x_w500_0722/all_models.6856/'

pdbfs=open(cluster_directory+pdb_file_names_file,'r')
pdblist=[]

for l in pdbfs:
    tk=l.split()[0]
    pdblist.append(tk)

caf=open(cluster_directory+cluster_assignment_file,'r')
files=[]

for l in caf:
    if l.split()[0] == "#": continue
    nstr=int(l.split()[0])
    clus=int(l.split()[1])
    print nstr,clus
    if clus==cluster_number:
      files.append(pdblist[nstr-1])    

# trim the file
files=[f.replace("best_pdb/A",original_directory_A).replace(".pdb",".rmf3") for f in files if "best_pdb/A" in f]

files=files[0::100]

if cross_link=="EDC": threshold=25
if cross_link=="DSS": threshold=35

# now you give the stat file, from where you extract the 
# information on the cross-links
# for instance we will merge the stat.?.out files into a single one
filenames=glob.glob(original_directory_A+"/stat.*.out")
with open('stat.3xray.out', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

cm.set_crosslinks('stat.3xray.out',filter_label=cross_link,filter_rmf_file_names=[os.path.basename(f) for f in files])

# alternatively you can pass a list of frames you are interested in

nup84 = ["Nup133","Nup84","Nup120","Nup145c","Sec13","Seh1","Nup85"]

prot=IMP.pmi.analysis.get_hier_from_rmf(model,0,files[0])
cm.set_hierarchy(prot)

for z, fil in enumerate(files):
    cm.set_coordinates_for_contact_map(fil,0)
    print z
    
    
cm.set_threshold(threshold)
cm.set_tolerance(0)

cm.plot(prot_listx=nup84,prot_listy=nup84,alphablend=0.3,scale_symbol_size=0.5,filename="contactmap.pdf",gap_between_components=100)
cm.write_cross_link_database("cross_link_table.csv")
#cm.plot_bars("xl_bar_plot",nup84,nup84,nxl_per_row=20)
#cm.crosslink_distance_histogram("cross_link_histogram",yplotrange=[0,0.1],normalized=True)

