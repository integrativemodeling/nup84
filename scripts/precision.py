import IMP
import IMP.pmi
import IMP.pmi.analysis
import IMP.pmi.output
import IMP.atom
import glob

selection_dictionary={"Hub":["Nup145c","Sec13","Seh1","Nup85"]}


for eoe in ('hub', 'all'):
    rmfs = glob.glob("output.1/rmfs/*.rmf3")
    frames=[0]*len(rmfs)
    
    model=IMP.Model()
    
    if eoe=='all':
       pr=IMP.pmi.analysis.Precision(model,'ten',
                                     selection_dictionary={})
    else:
       pr=IMP.pmi.analysis.Precision(model,'ten',
                                     selection_dictionary=selection_dictionary)
    pr.set_threshold(60.0)
    pr.set_precision_style('pairwise_drmsd_Q')

    pr.add_structures(zip(rmfs,frames), 'all', is_mpi=False)
        
    outfile="precision."+eoe+".dat"
    pr.get_precision(outfile, 'all', 'all', is_mpi=False, skip=10)
