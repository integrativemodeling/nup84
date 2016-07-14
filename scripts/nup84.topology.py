beadsize=20

n84_fastafile  ='../data/protein_fasta.Nup84.txt'
n85_fastafile  ='../data/protein_fasta.Nup85.txt'
n120_fastafile ='../data/protein_fasta.Nup120.txt'
n133_fastafile ='../data/protein_fasta.Nup133.txt'
n145c_fastafile='../data/protein_fasta.Nup145c.txt'
seh1_fastafile ='../data/protein_fasta.Seh1.txt'
sec13_fastafile='../data/protein_fasta.Sec13.txt'

#n84n_pdbfile   ='../data/ScNup84N_7-488.pdb'
#n84c_pdbfile   ='../data/ScNup84C_506-726.pdb'
#n85_pdbfile    ='../data/ScNup85_44-744.pdb'
#n120_pdbfile   ='../data/ScNup120_1-1037.pdb'
#n133n_pdbfile  ='../data/ScNup133N_56-480.pdb'
#n133c_pdbfile  ='../data/ScNup133C_490_1157.pdb'
#n145c_pdbfile  ='../data/ScNup145C_126-553.pdb'
#seh1_pdbfile   ='../data/ScSeh1_1-346.pdb'
#sec13_pdbfile  ='../data/ScSec13_2-296.pdb'

# After removal of disordered regions in PDB files.
n84_pdbfile   ='../data/ScNup84_7-488_506-726_new.pdb'
n85_pdbfile    ='../data/ScNup85_44-744_new.pdb'
n120_pdbfile   ='../data/ScNup120_1-1037_new.pdb'
n133n_pdbfile  ='../data/ScNup133N_56-480_new.pdb'
n133c_pdbfile  ='../data/ScNup133C_490_1157_new.pdb'
n145c_pdbfile  ='../data/ScNup145C_126-553_new.pdb'
seh1_pdbfile   ='../data/ScSeh1_1-346_new.pdb'
sec13_pdbfile  ='../data/ScSec13_2-296_new.pdb'

#-----------------
simo.create_component("Nup84",color=0.0)
simo.add_component_sequence("Nup84", n84_fastafile)

Nup84=simo.autobuild_model("Nup84", n84_pdbfile,"A", resrange=(1,726), resolutions=[1,10], missingbeadsize=beadsize)

simo.show_component_table("Nup84")
simo.setup_component_geometry("Nup84")
#-----------------

simo.create_component("Nup85",color=0.1)
simo.add_component_sequence("Nup85", n85_fastafile)

Nup85_1=simo.autobuild_model("Nup85", n85_pdbfile,"B", resrange=(1,529), resolutions=[1,10], missingbeadsize=beadsize)
Nup85_2=simo.autobuild_model("Nup85", n85_pdbfile,"B", resrange=(530,744), resolutions=[1,10], missingbeadsize=beadsize)

simo.show_component_table("Nup85")
simo.setup_component_geometry("Nup85")

#-----------------
simo.create_component("Nup120",color=0.2)
simo.add_component_sequence("Nup120", n120_fastafile)
Nup120_1=simo.autobuild_model("Nup120", n120_pdbfile,"C", resrange=(1,710), resolutions=[1,10], missingbeadsize=beadsize)
Nup120_2=simo.autobuild_model("Nup120", n120_pdbfile,"C", resrange=(711,1037), resolutions=[1,10], missingbeadsize=beadsize)

simo.show_component_table("Nup120")
simo.setup_component_geometry("Nup120")

#-----------------
simo.create_component("Nup133",color=0.3)
simo.add_component_sequence("Nup133", n133_fastafile)

Nup133_1=simo.autobuild_model("Nup133",n133n_pdbfile,"D", resrange=(1,480),resolutions=[1,10],missingbeadsize=beadsize)
Nup133_2=simo.autobuild_model("Nup133",n133c_pdbfile,"D", resrange=(481,1157),resolutions=[1,10],missingbeadsize=beadsize)

simo.show_component_table("Nup133")
simo.setup_component_geometry("Nup133")
#-----------------

simo.create_component("Nup145c",color=0.4)
simo.add_component_sequence("Nup145c", n145c_fastafile)

Nup145c=simo.autobuild_model("Nup145c",n145c_pdbfile,"E", resrange=(1,712),resolutions=[1,10],missingbeadsize=beadsize)

simo.show_component_table("Nup145c")
simo.setup_component_geometry("Nup145c")

#-----------------
simo.create_component("Seh1",color=0.5)
simo.add_component_sequence("Seh1", seh1_fastafile)
Seh1=simo.autobuild_model("Seh1",seh1_pdbfile,"A", resrange=(1,349),resolutions=[1,10],missingbeadsize=beadsize)

simo.show_component_table("Seh1")
simo.setup_component_geometry("Seh1")
#-----------------
simo.create_component("Sec13",color=0.6)
simo.add_component_sequence("Sec13", sec13_fastafile)
Sec13=simo.autobuild_model("Sec13",sec13_pdbfile,"D", resrange=(1,297),resolutions=[1,10],missingbeadsize=beadsize)

simo.show_component_table("Sec13")
simo.setup_component_geometry("Sec13")

#-----------------

simo.setup_component_sequence_connectivity("Nup84", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Nup85", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Nup120", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Nup133", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Nup145c", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Seh1", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Sec13", resolution=1.0, scale=4.0)

Nup84_all   = Nup84
Nup85_all   = Nup85_1+Nup85_2
Nup120_all  = Nup120_1+Nup120_2
Nup133_all  = Nup133_1+Nup133_2
Nup145c_all = Nup145c
Seh1_all    = Seh1
Sec13_all   = Sec13

Nup84_complex=Nup84_all+Nup85_all+Nup120_all+Nup133_all+Nup145c_all+Seh1_all+Sec13_all

simo.set_rigid_body_from_hierarchies(Nup84)
simo.set_rigid_body_from_hierarchies(Nup85_1)
simo.set_rigid_body_from_hierarchies(Nup85_2)
simo.set_rigid_body_from_hierarchies(Nup120_1)
simo.set_rigid_body_from_hierarchies(Nup120_2)
simo.set_rigid_body_from_hierarchies(Nup133_1)
simo.set_rigid_body_from_hierarchies(Nup133_2)
simo.set_rigid_body_from_hierarchies(Nup145c)
simo.set_rigid_body_from_hierarchies(Seh1)
simo.set_rigid_body_from_hierarchies(Sec13)

simo.set_super_rigid_body_from_hierarchies(Sec13+Nup85_all+Seh1+Nup145c)
simo.set_super_rigid_body_from_hierarchies(Nup84_all)
simo.set_super_rigid_body_from_hierarchies(Nup85_all)
simo.set_super_rigid_body_from_hierarchies(Nup120_all)
simo.set_super_rigid_body_from_hierarchies(Nup133_all)
simo.set_super_rigid_body_from_hierarchies(Nup145c_all)
simo.set_super_rigid_body_from_hierarchies(Seh1_all)
simo.set_super_rigid_body_from_hierarchies(Sec13_all)

simo.set_super_rigid_body_from_hierarchies(Nup84_complex)

simo.set_floppy_bodies()
