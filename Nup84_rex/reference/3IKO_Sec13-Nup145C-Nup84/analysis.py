import IMP
import IMP.pmi.output

rmsd=[]
score=[]
dsspsi=[]
edcpsi=[]
dsssigma=[]
edcsigma=[]

rmsdfield="SimplifiedModel_3IKO_RelativeDRMS_None"
scorefield="SimplifiedModel_Total_Score_None"
dsspsifield="ISDCrossLinkMS_Psi_1.0_DSS"
edcpsifield="ISDCrossLinkMS_Psi_1.0_EDC"
dsssigmafield="ISDCrossLinkMS_Sigma_1_DSS"
edcsigmafield="ISDCrossLinkMS_Sigma_1_EDC"

for i in range(1):
   statfile="stat."+str(i)+".out"
   sf=IMP.pmi.output.ProcessOutput(statfile)
   

   fielddict=sf.get_fields([rmsdfield,scorefield,dsspsifield,edcpsifield,dsssigmafield,edcsigmafield])

   rmsd+=fielddict[rmsdfield]
   score+=fielddict[scorefield]
   dsspsi+=fielddict[dsspsifield]
   edcpsi+=fielddict[edcpsifield]
   dsssigma+=fielddict[dsssigmafield]
   edcsigma+=fielddict[edcsigmafield]    

IMP.pmi.output.plot_scatter_xy_data(rmsd,score,labelx='RMSD',labely='Score',
                                    xmin=0,xmax=300,ymin=0.0,ymax=100,
                                    savefile=True,filename="score.vs.rmsd.eps")

IMP.pmi.output.plot_field_histogram("Psi-DSS",dsspsi)
IMP.pmi.output.plot_field_histogram("Psi-EDC",edcpsi)
IMP.pmi.output.plot_field_histogram("Sigma-DSS",dsssigma)
IMP.pmi.output.plot_field_histogram("Sigma-EDC",edcsigma)



