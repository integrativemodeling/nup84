import IMP
import IMP.pmi
import IMP.pmi.analysis
import IMP.pmi.output
import IMP.atom
import glob

rmfs=glob.glob("output.1/rmfs/*.rmf3")

selection_dictionary={"Nup145c-Sec13":[("Nup145c",145,181),"Sec13"],
                      "Nup85-Seh1":[("Nup85",123,460),"Seh1"],
                      "Nup84-Nup145c":[("Nup84",1,488),("Nup145c",145,181)]}

model=IMP.Model()


frames=[0]*len(rmfs)

model=IMP.Model()
pr=IMP.pmi.analysis.Precision(model,'one',
                              selection_dictionary=selection_dictionary)
pr.set_precision_style('pairwise_drmsd_k')

pr.add_structures(zip(rmfs,frames),is_mpi=False)



refrmf='reference/xray-hub.rmf3'
pr.set_reference_structure(refrmf,0)

print pr.get_average_distance_wrt_reference_structure()
