import IMP
import IMP.pmi
import IMP.pmi.analysis
import IMP.pmi.output
import IMP.atom
import glob

rmfs=glob.glob("output.1/rmfs/*.rmf3")

selection_dictionary={"Nup145c-Sec13":[(145,181,"Nup145c"),"Sec13"],
                      "Nup85-Seh1":[(123,460,"Nup85"),"Seh1"],
                      "Nup84-Nup145c":[(1,488,"Nup84"),(145,181,"Nup145c")]}

model=IMP.Model()


frames=[0]*len(rmfs)

model=IMP.Model()
pr=IMP.pmi.analysis.Precision(model,1,
                              selection_dictionary=selection_dictionary)
pr.set_precision_style('pairwise_drmsd_k')

pr.add_structures(zip(rmfs,frames), 'all')



refrmf='reference/xray-hub.rmf3'
pr.set_reference_structure(refrmf,0)

print pr.get_average_distance_wrt_reference_structure('all')
