import IMP
import IMP.pmi
import IMP.pmi.analysis
import IMP.pmi.output
import IMP.atom
import glob

selection_dictionary={"Hub":["Nup145c","Sec13","Seh1","Nup85"]}

rmfs = glob.glob("kmeans_50_1/cluster.0/*.rmf3")
frames=[0]*len(rmfs)

model=IMP.Model()

pr=IMP.pmi.analysis.Precision(model,resolution=10,
                             selection_dictionary=selection_dictionary)
pr.set_threshold(60.0)
pr.set_precision_style('pairwise_drmsd_Q')

pr.add_structures(zip(rmfs,frames), 'all')

outfile="precision.dat"
pr.get_precision('all', 'all', outfile)
