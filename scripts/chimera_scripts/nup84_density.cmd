# Chimera command script showing Nup84 densities
#
#open *.dx
#2.5 x Volume ; complex 2.5 x volume
#3-xray
#Nup120-CTD
volume #0 style surface level 0.00778 color forestgreen step 2
#Nup120
volume #1 style surface level 0.00963 color forestgreen step 2
#Nup133
volume #2 style surface level 0.00959 color khaki step 2
#Nup145c-CTD
volume #3 style surface level 0.00032 color gray step 2 
#Nup145c-NTD
volume #4 style surface level 0.00043 color gray step 2 
#Nup145c-middle
volume #5 style surface level 0.01 color gray step 2
#Nup84
volume #6 style surface level 0.00849 color lightblue step 2 
#Nup84_complex
volume #7 style surface transparency 1.0 level 0.00961 color white step 2 
#Nup85 
volume #8 style surface level 0.00818 color gold step 2 
#Sec13 
volume #9 style surface level 0.0112 color brown step 2 
#Seh1 
volume #10 style surface level 0.0106 color dodgerblue step 2 
volume all show
echo script finished
