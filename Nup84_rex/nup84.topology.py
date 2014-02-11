beadsize=20

n84_fastafile  ='data/protein_fasta.Nup84.txt'
n85_fastafile  ='data/protein_fasta.Nup85.txt'
n120_fastafile ='data/protein_fasta.Nup120.txt'
n133_fastafile ='data/protein_fasta.Nup133.txt'
n145c_fastafile='data/protein_fasta.Nup145c.txt'
seh1_fastafile ='data/protein_fasta.Seh1.txt'
sec13_fastafile='data/protein_fasta.Sec13.txt'

n84n_pdbfile   ='data/ScNup84N_7-488.pdb'  
n84c_pdbfile   ='data/ScNup84C_506-726.pdb'   
n85_pdbfile    ='data/ScNup85_44-744.pdb'  
n120_pdbfile   ='data/ScNup120_1-1037.pdb'        
n133n_pdbfile  ='data/ScNup133N_56-480.pdb'    
n133c_pdbfile  ='data/ScNup133C_490_1157.pdb'
n145c_pdbfile  ='data/ScNup145C_126-553.pdb'  
seh1_pdbfile   ='data/ScSeh1_1-346.pdb'
sec13_pdbfile  ='data/ScSec13_2-296.pdb'

#-----------------
simo.create_component("Nup84",color=0.0)
simo.add_component_sequence("Nup84", n84_fastafile)
tmp_color=0.0
Nup84_1=simo.add_component_beads("Nup84", [(1,6)], colors=[tmp_color])
Nup84_2=simo.autobuild_model("Nup84", n84n_pdbfile,"A", resrange=(7,488), resolutions=[1,10], missingbeadsize=beadsize)
Nup84_3=simo.add_component_beads("Nup84", [(489,505)], colors=[tmp_color])
Nup84_4=simo.autobuild_model("Nup84", n84c_pdbfile,"A", resrange=(506,726), resolutions=[1,10], missingbeadsize=beadsize)
simo.show_component_table("Nup84")
#-----------------
simo.create_component("Nup85",color=0.1)
simo.add_component_sequence("Nup85", n85_fastafile)
tmp_color=0.1
Nup85_1=simo.add_component_beads("Nup85", [(1,43)],colors=[tmp_color])
Nup85_2=simo.autobuild_model("Nup85", n85_pdbfile,"B", resrange=(44,744), resolutions=[1,10], missingbeadsize=beadsize)
simo.show_component_table("Nup85")
#-----------------
simo.create_component("Nup120",color=0.2)
simo.add_component_sequence("Nup120","data/protein_fasta.Nup120.txt")
Nup120_1=simo.autobuild_model("Nup120", n120_pdbfile,"C", resrange=(1,710), resolutions=[1,10], missingbeadsize=beadsize)
Nup120_2=simo.autobuild_model("Nup120", n120_pdbfile,"C", resrange=(711,1037), resolutions=[1,10], missingbeadsize=beadsize)
simo.show_component_table("Nup120")
#-----------------
simo.create_component("Nup133",color=0.3)
simo.add_component_sequence("Nup133","data/protein_fasta.Nup133.txt")
tmp_color=0.3
Nup133_1=simo.add_component_beads("Nup133", [(1,55)],colors=[tmp_color])
Nup133_2=simo.autobuild_model("Nup133",n133n_pdbfile,"D", resrange=(56,480),resolutions=[1,10],missingbeadsize=beadsize)
Nup133_3=simo.add_component_beads("Nup133", [(481,489)],colors=[tmp_color])
Nup133_4=simo.autobuild_model("Nup133",n133c_pdbfile,"D", resrange=(490,1157),resolutions=[1,10],missingbeadsize=beadsize)
simo.show_component_table("Nup133")
#-----------------
simo.create_component("Nup145c",color=0.4)
simo.add_component_sequence("Nup145c","data/protein_fasta.Nup145c.txt")
tmp_color=0.4
Nup145c_1=simo.add_component_beads("Nup145c", [(1,125)],colors=[tmp_color])
Nup145c_2=simo.autobuild_model("Nup145c",n145c_pdbfile,"E", resrange=(126,553),resolutions=[1,10],missingbeadsize=beadsize)
Nup145c_3=simo.add_component_beads("Nup145c", [(554,712)],colors=[tmp_color])
simo.show_component_table("Nup145c")
#-----------------
simo.create_component("Seh1",color=0.5)
simo.add_component_sequence("Seh1","data/protein_fasta.Seh1.txt")
Seh1=simo.autobuild_model("Seh1",seh1_pdbfile,"F", resrange=(1,349),resolutions=[1,10],missingbeadsize=beadsize)
simo.show_component_table("Seh1")
#-----------------
simo.create_component("Sec13",color=0.6)
simo.add_component_sequence("Sec13","data/protein_fasta.Sec13.txt")
Sec13=simo.autobuild_model("Sec13",sec13_pdbfile,"G", resrange=(1,297),resolutions=[1,10],missingbeadsize=beadsize)
simo.show_component_table("Sec13")
#-----------------

simo.setup_component_sequence_connectivity("Nup84")
simo.setup_component_sequence_connectivity("Nup85")
simo.setup_component_sequence_connectivity("Nup120")
simo.setup_component_sequence_connectivity("Nup133")
simo.setup_component_sequence_connectivity("Nup145c")
simo.setup_component_sequence_connectivity("Seh1")
simo.setup_component_sequence_connectivity("Sec13")

Nup84_all   =Nup84_1+Nup84_2+Nup84_3+Nup84_4
Nup85_all   =Nup85_1+Nup85_2
Nup120_all  =Nup120_1+Nup120_2
Nup133_all  =Nup133_1+Nup133_2+Nup133_3+Nup133_4
Nup145c_all =Nup145c_1+Nup145c_2+Nup145c_3
Seh1_all    =Seh1
Sec13_all   =Sec13
Nup84_complex=Nup84_all+Nup85_all+Nup120_all+Nup133_all+Nup145c_all+Seh1_all+Sec13_all

simo.set_rigid_body_from_hierarchies(Nup84_1)
simo.set_rigid_body_from_hierarchies(Nup84_2)
simo.set_rigid_body_from_hierarchies(Nup84_3)
simo.set_rigid_body_from_hierarchies(Nup84_4)
simo.set_rigid_body_from_hierarchies(Nup85_1)
simo.set_rigid_body_from_hierarchies(Nup85_2)
simo.set_rigid_body_from_hierarchies(Nup120_1) 
simo.set_rigid_body_from_hierarchies(Nup120_2) 
simo.set_rigid_body_from_hierarchies(Nup133_1)
simo.set_rigid_body_from_hierarchies(Nup133_2)
simo.set_rigid_body_from_hierarchies(Nup133_3)
simo.set_rigid_body_from_hierarchies(Nup133_4)
simo.set_rigid_body_from_hierarchies(Nup145c_1)  
simo.set_rigid_body_from_hierarchies(Nup145c_2)
simo.set_rigid_body_from_hierarchies(Nup145c_3)
simo.set_rigid_body_from_hierarchies(Seh1)
simo.set_rigid_body_from_hierarchies(Sec13)

simo.set_super_rigid_body_from_hierarchies(Nup84_all)
simo.set_super_rigid_body_from_hierarchies(Nup85_all)
simo.set_super_rigid_body_from_hierarchies(Nup120_all)
simo.set_super_rigid_body_from_hierarchies(Nup133_all)
simo.set_super_rigid_body_from_hierarchies(Nup145c_all)

simo.set_super_rigid_body_from_hierarchies(Nup84_complex)

simo.set_floppy_bodies()
