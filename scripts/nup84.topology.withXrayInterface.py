def get_pdb_bead_bits(hierarchy):
    pdbbits=[]
    beadbits=[]
    for h in hierarchy:
       if "_pdb" in h.get_name():pdbbits.append(h)
       if "_bead" in h.get_name():beadbits.append(h)
    return (pdbbits,beadbits)

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
n84_pdbfile    ='../data/ScNup84_7-488_506-726_new2.pdb'
n85_pdbfile    ='../data/ScNup85_44-744_new2.pdb'
n120_pdbfile   ='../data/ScNup120_1-1037_new.pdb'
n133n_pdbfile  ='../data/ScNup133N_56-480_new.pdb'
n133c_pdbfile  ='../data/ScNup133C_490_1157_new.pdb'
n145c_pdbfile  ='../data/ScNup145C_126-553_new2.pdb'
seh1_pdbfile   ='../data/ScSeh1_1-346_new2.pdb'
sec13_pdbfile  ='../data/ScSec13_2-296_new2.pdb'
#-----------------

simo.create_component("Nup84",color=0.0)
simo.add_component_sequence("Nup84", n84_fastafile)

Nup84=simo.autobuild_model("Nup84", n84_pdbfile,"A", resrange=(1,726), resolutions=[1,10], missingbeadsize=beadsize)

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup84)
Nup84_dens=simo.add_component_density("Nup84",
                               pdbbits,
                               num_components=7, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Nup84_dens.txt') # read what it was calculated before
                               #outputfile='../data/Nup84_dens.txt', # do the calculation
                               #outputmap='../data/Nup84_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

simo.show_component_table("Nup84")
simo.setup_component_geometry("Nup84")
#-----------------

simo.create_component("Nup85",color=0.1)
simo.add_component_sequence("Nup85", n85_fastafile)

Nup85_1=simo.autobuild_model("Nup85", n85_pdbfile,"B", resrange=(1,529), resolutions=[1,10], missingbeadsize=beadsize)
Nup85_2=simo.autobuild_model("Nup85", n85_pdbfile,"B", resrange=(530,744), resolutions=[1,10], missingbeadsize=beadsize)

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup85_1)
Nup85_1_dens=simo.add_component_density("Nup85",
                               pdbbits,
                               num_components=8, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Nup85_1_dens.txt') # read what it was calculated before
                               #outputfile='../data/Nup85_1_dens.txt', # do the calculation
                               #outputmap='../data/Nup85_1_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup85_2)
Nup85_2_dens=simo.add_component_density("Nup85",
                               pdbbits,
                               num_components=3, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Nup85_2_dens.txt') # read what it was calculated before
                               #outputfile='../data/Nup85_2_dens.txt', # do the calculation
                               #outputmap='../data/Nup85_2_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

simo.show_component_table("Nup85")
simo.setup_component_geometry("Nup85")

#-----------------
simo.create_component("Nup120",color=0.2)
simo.add_component_sequence("Nup120", n120_fastafile)
Nup120_1=simo.autobuild_model("Nup120", n120_pdbfile,"C", resrange=(1,710), resolutions=[1,10], missingbeadsize=beadsize)
Nup120_2=simo.autobuild_model("Nup120", n120_pdbfile,"C", resrange=(711,1037), resolutions=[1,10], missingbeadsize=beadsize)

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup120_1)
Nup120_1_dens=simo.add_component_density("Nup120",
                               pdbbits,
                               num_components=7, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Nup120_1_dens.txt') # read what it was calculated before
                               #outputfile='../data/Nup120_1_dens.txt', # do the calculation
                               #outputmap='../data/Nup120_1_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup120_2)
Nup120_2_dens=simo.add_component_density("Nup120",
                               pdbbits,
                               num_components=3, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Nup120_2_dens.txt') # read what it was calculated before
                               #outputfile='../data/Nup120_2_dens.txt', # do the calculation
                               #outputmap='../data/Nup120_2_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

simo.show_component_table("Nup120")
simo.setup_component_geometry("Nup120")

#-----------------
simo.create_component("Nup133",color=0.3)
simo.add_component_sequence("Nup133", n133_fastafile)

Nup133_1=simo.autobuild_model("Nup133",n133n_pdbfile,"D", resrange=(1,480),resolutions=[1,10],missingbeadsize=beadsize)
Nup133_2=simo.autobuild_model("Nup133",n133c_pdbfile,"D", resrange=(481,1157),resolutions=[1,10],missingbeadsize=beadsize)

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup133_1)
Nup133_1_dens=simo.add_component_density("Nup133",
                               pdbbits,
                               num_components=5, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Nup133_1_dens.txt') # read what it was calculated before
                               #outputfile='../data/Nup133_1_dens.txt', # do the calculation
                               #outputmap='../data/Nup133_1_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup133_2)
Nup133_2_dens=simo.add_component_density("Nup133",
                               pdbbits,
                               num_components=7, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Nup133_2_dens.txt') # read what it was calculated before
                               #outputfile='../data/Nup133_2_dens.txt', # do the calculation
                               #outputmap='../data/Nup133_2_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

simo.show_component_table("Nup133")
simo.setup_component_geometry("Nup133")
#-----------------

simo.create_component("Nup145c",color=0.4)
simo.add_component_sequence("Nup145c", n145c_fastafile)

Nup145c=simo.autobuild_model("Nup145c",n145c_pdbfile,"E", resrange=(1,712),resolutions=[1,10],missingbeadsize=beadsize)

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup145c)
Nup145c_dens=simo.add_component_density("Nup145c",
                               pdbbits,
                               num_components=7, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Nup145c_dens.txt') # read what it was calculated before
                               #outputfile='../data/Nup145c_dens.txt', # do the calculation
                               #outputmap='../data/Nup145c_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

simo.show_component_table("Nup145c")
simo.setup_component_geometry("Nup145c")

#-----------------
simo.create_component("Seh1",color=0.5)
simo.add_component_sequence("Seh1", seh1_fastafile)
Seh1=simo.autobuild_model("Seh1",seh1_pdbfile,"F", resrange=(1,349),resolutions=[1,10],missingbeadsize=beadsize)

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Seh1)
Seh1_dens=simo.add_component_density("Seh1",
                               pdbbits,
                               num_components=4, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Seh1_dens.txt') # read what it was calculated before
                               #outputfile='../data/Seh1_dens.txt', # do the calculation
                               #outputmap='../data/Seh1_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

simo.show_component_table("Seh1")
simo.setup_component_geometry("Seh1")
#-----------------
simo.create_component("Sec13",color=0.6)
simo.add_component_sequence("Sec13", sec13_fastafile)
Sec13=simo.autobuild_model("Sec13",sec13_pdbfile,"G", resrange=(1,297),resolutions=[1,10],missingbeadsize=beadsize)

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Sec13)
Sec13_dens=simo.add_component_density("Sec13",
                               pdbbits,
                               num_components=3, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile='../data/Sec13_dens.txt') # read what it was calculated before
                               #outputfile='../data/Sec13_dens.txt', # do the calculation
                               #outputmap='../data/Sec13_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc

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



Nup84_Nup145C_Sec13_all = Nup84+Nup84_dens+Nup145c+Nup145c_dens+Sec13+Sec13_dens
Nup85_Seh1_all   = Nup85_1+Nup85_2+Nup85_1_dens+Nup85_2_dens+Seh1+Seh1_dens
Nup120_all  = Nup120_1+Nup120_2+Nup120_1_dens+Nup120_2_dens
Nup133_all  = Nup133_1+Nup133_2+Nup133_1_dens+Nup133_2_dens

Nup84_complex=Nup84_Nup145C_Sec13_all+Nup85_Seh1_all+Nup120_all+Nup133_all

resdensities=Nup84_dens+Nup85_1_dens+Nup85_2_dens+Nup120_1_dens+Nup120_2_dens+ \
             Nup133_1_dens+Nup133_2_dens+Nup145c_dens+Seh1_dens+Sec13_dens

simo.set_rigid_body_from_hierarchies(Nup145c+Nup145c_dens+Nup84+Nup84_dens+Sec13+Sec13_dens)
simo.set_rigid_body_from_hierarchies(Nup85_1+Nup85_1_dens+Seh1+Seh1_dens)
simo.set_rigid_body_from_hierarchies(Nup85_2+Nup85_2_dens)
simo.set_rigid_body_from_hierarchies(Nup120_1+Nup120_1_dens)
simo.set_rigid_body_from_hierarchies(Nup120_2+Nup120_2_dens)
simo.set_rigid_body_from_hierarchies(Nup133_1+Nup133_1_dens)
simo.set_rigid_body_from_hierarchies(Nup133_2+Nup133_2_dens)

simo.set_super_rigid_body_from_hierarchies(Nup84_Nup145C_Sec13_all+Nup85_Seh1_all)
simo.set_super_rigid_body_from_hierarchies(Nup84_Nup145C_Sec13_all) 
simo.set_super_rigid_body_from_hierarchies(Nup85_Seh1_all) 
simo.set_super_rigid_body_from_hierarchies(Nup120_all)
simo.set_super_rigid_body_from_hierarchies(Nup133_all)

simo.set_super_rigid_body_from_hierarchies(Nup84_complex)

simo.set_floppy_bodies()
