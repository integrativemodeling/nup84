
# little function that is used to get flexible beads
def get_pdb_bead_bits(hierarchy):
    pdbbits=[]
    beadbits=[]
    for h in hierarchy: 
       if "_pdb" in h.get_name():pdbbits.append(h)
       if "_bead" in h.get_name():beadbits.append(h)
    return (pdbbits,beadbits)


beadsize=20                             # the maximum number of allowed aggregated 
                                        # residues in a bead for missing regions
pdbfile='3IKO_Sec13-Nup145C-Nup84.pdb'  

#-----------------

#coordinate generation
simo.add_component_name("Nup84",color=0.0)                                    #create the subunit
simo.add_component_sequence("Nup84","data/3IKO.Nup84.fasta.txt")           #add the sequence
Nup84=simo.autobuild_pdb_and_intervening_beads("Nup84",'data/'+pdbfile,"C",   #automatic generation of coordinates
                                        resolutions=[1,10],beadsize=beadsize)

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Nup84)
#Nup84_dens=simo.add_component_density("Nup84",
#                               pdbbits,
#                               num_components=10, # number of gaussian into which the simulated density is approximated
#                               resolution=1,      # resolution that you want to calculate the simulated density
#                               inputfile='data/Nup84_dens.txt') # read what it was calculated before
                               # outputfile='data/Nup84_dens.txt') # do the calculation
                               # mrcfile='data/Nup84_dens.mrc') # do the calculation and output the mrc

simo.show_component_table("Nup84") # printing out information to do debug

#-----------------
#-----------------


#simo.add_component_name("Nup85",color=0.1)
#simo.add_component_sequence("Nup85","data/protein_fasta.Nup85.txt")
#Nup85_1=simo.autobuild_pdb_and_intervening_beads("Nup85",'data/'+pdbfile,"B",resrange=(1,555),
#                                        resolutions=[1,10],beadsize=beadsize)
#(pdbbits,beadbits)=get_pdb_bead_bits(Nup85_1)
#                       
#Nup85_1_dens=simo.add_component_density("Nup85",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Nup85_1_dens.txt')

#-----------------


#Nup85_2=simo.autobuild_pdb_and_intervening_beads("Nup85",'data/'+pdbfile,"B",
#                                        resrange=(556,745),
#                                        resolutions=[1,10],beadsize=beadsize)

#(pdbbits,beadbits)=get_pdb_bead_bits(Nup85_2)

#Nup85_2_dens=simo.add_component_density("Nup85",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Nup85_2_dens.txt')
                               
#simo.show_component_table("Nup85")

#-----------------
#-----------------

#simo.add_component_name("Nup120",color=0.2)
#simo.add_component_sequence("Nup120","data/protein_fasta.Nup120.txt")

#Nup120_1=simo.autobuild_pdb_and_intervening_beads("Nup120",'data/'+pdbfile,"C",
#                                        resrange=(1,730),
#                                        resolutions=[1,10],beadsize=beadsize)

#(pdbbits,beadbits)=get_pdb_bead_bits(Nup120_1)

#Nup120_1_dens=simo.add_component_density("Nup120",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Nup120_1_dens.txt')

#-----------------

                       
#Nup120_2=simo.autobuild_pdb_and_intervening_beads("Nup120",'data/'+pdbfile,"C",
#                                        resrange=(731,1040),
#                                        resolutions=[1,10],beadsize=beadsize)

#(pdbbits,beadbits)=get_pdb_bead_bits(Nup120_2)

                    
#Nup120_2_dens=simo.add_component_density("Nup120",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Nup120_2_dens.txt')  

#simo.show_component_table("Nup120")

#-----------------
#-----------------

#simo.add_component_name("Nup133",color=0.3)
#simo.add_component_sequence("Nup133","data/protein_fasta.Nup133.txt")
                       
#Nup133=simo.autobuild_pdb_and_intervening_beads("Nup133",'data/'+pdbfile,"D",
#                                        resolutions=[1,10],beadsize=beadsize)

#(pdbbits,beadbits)=get_pdb_bead_bits(Nup133)
                    
#Nup133_dens=simo.add_component_density("Nup133",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Nup133_dens.txt')  
                               
#simo.show_component_table("Nup133")

#-----------------
#-----------------

simo.add_component_name("Nup145c",color=0.4)
simo.add_component_sequence("Nup145c","data/3IKO.Nup145C.fasta.txt")

Nup145c_1=simo.autobuild_pdb_and_intervening_beads("Nup145c",'data/'+pdbfile,"B",
                                        resrange=(1,130),
                                        resolutions=[1,10],beadsize=beadsize)
                       
(pdbbits,beadbits)=get_pdb_bead_bits(Nup145c_1)
  
                       
#Nup145c_1_dens=simo.add_component_density("Nup145c",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Nup145c_1_dens.txt')


#-----------------

Nup145c_2=simo.autobuild_pdb_and_intervening_beads("Nup145c",'data/'+pdbfile,"B",
                                        resrange=(131,552),
                                        resolutions=[1,10],beadsize=beadsize)

(pdbbits,beadbits)=get_pdb_bead_bits(Nup145c_2)

#Nup145c_2_dens=simo.add_component_density("Nup145c",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Nup145c_2_dens.txt')

#-----------------

#Nup145c_3=simo.autobuild_pdb_and_intervening_beads("Nup145c",'data/'+pdbfile,"B",
#                                        resrange=(554,712),
#                                        resolutions=[1,10],beadsize=beadsize)

#(pdbbits,beadbits)=get_pdb_bead_bits(Nup145c_3)
                           
#Nup145c_3_dens=simo.add_component_density("Nup145c",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Nup145c_3_dens.txt')
                                 
simo.show_component_table("Nup145c")

#-----------------
#-----------------

#simo.add_component_name("Seh1",color=0.5)
#simo.add_component_sequence("Seh1","data/protein_fasta.Seh1.txt")
#Seh1=simo.autobuild_pdb_and_intervening_beads("Seh1",'data/'+pdbfile,"F",
#                                        resolutions=[1,10],beadsize=beadsize)

#(pdbbits,beadbits)=get_pdb_bead_bits(Seh1)

#Seh1_dens=simo.add_component_density("Seh1",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Seh1_dens.txt')
                                 
#simo.show_component_table("Seh1")

#-----------------
#-----------------

simo.add_component_name("Sec13",color=0.6)
simo.add_component_sequence("Sec13","data/3IKO.Sec13.fasta.txt")

Sec13=simo.autobuild_pdb_and_intervening_beads("Sec13",'data/'+pdbfile,"A",
                                        resolutions=[1,10],beadsize=beadsize)

(pdbbits,beadbits)=get_pdb_bead_bits(Sec13)

#Sec13_dens=simo.add_component_density("Sec13",pdbbits,
#                               num_components=10,resolution=1,
#                               inputfile='data/Sec13_dens.txt')
                                 
#simo.show_component_table("Sec13")

#-----------------
#-----------------

simo.setup_component_sequence_connectivity("Nup84")  # this creates the restraints that makes flexible parts, 
                                                     # and different rigid bodies all connected by the sequence
#simo.setup_component_sequence_connectivity("Nup85")
#simo.setup_component_sequence_connectivity("Nup120")
#simo.setup_component_sequence_connectivity("Nup133")
simo.setup_component_sequence_connectivity("Nup145c")
#simo.setup_component_sequence_connectivity("Seh1")
simo.setup_component_sequence_connectivity("Sec13")

# here we are creating the list of hierarchies for all  rigid bodies

#Nup84_all    =Nup84+Nup84_dens        
#Nup85_1_all  =Nup85_1+Nup85_1_dens
#Nup85_2_all  =Nup85_2+Nup85_2_dens
#Nup120_1_all =Nup120_1+Nup120_1_dens
#Nup120_2_all =Nup120_2+Nup120_2_dens
#Nup133_all   =Nup133+Nup133_dens
#Nup145c_1_all=Nup145c_1+Nup145c_1_dens
#Nup145c_2_all=Nup145c_2+Nup145c_2_dens
#Nup145c_3_all=Nup145c_3+Nup145c_3_dens
#Seh1_all     =Seh1+Seh1_dens
#Sec13_all    =Sec13+Sec13_dens

Nup84_all    =Nup84
Nup145c_1_all=Nup145c_1
Nup145c_2_all=Nup145c_2
#Nup145c_3_all=Nup145c_3
Sec13_all    =Sec13

# list of hierarchies for the super rigid bodies

#Nup85_all    =Nup85_1_all+Nup85_2_all
#Nup120_all   =Nup120_1_all+Nup120_2_all
#Nup145c_all  =Nup145c_1_all+Nup145c_2_all+Nup145c_3_all
Nup145c_all  =Nup145c_1_all+Nup145c_2_all
#Nup84_complex=Nup84_all+Nup85_all+Nup120_all+Nup133_all+Nup145c_all+Seh1_all+Sec13_all
Nup84_complex=Nup84_all+Nup145c_all+Sec13_all

# create the rigid bodies

simo.set_rigid_body_from_hierarchies(Nup84_all)
#simo.set_rigid_body_from_hierarchies(Nup85_1_all)
#simo.set_rigid_body_from_hierarchies(Nup85_2_all)
#simo.set_rigid_body_from_hierarchies(Nup120_1_all) 
#simo.set_rigid_body_from_hierarchies(Nup120_2_all) 
#simo.set_rigid_body_from_hierarchies(Nup133_all)
simo.set_rigid_body_from_hierarchies(Nup145c_1_all)  
simo.set_rigid_body_from_hierarchies(Nup145c_2_all)
#simo.set_rigid_body_from_hierarchies(Nup145c_3_all)
#simo.set_rigid_body_from_hierarchies(Seh1_all)
simo.set_rigid_body_from_hierarchies(Sec13_all)

# create the super rigid bodies

#simo.set_super_rigid_body_from_hierarchies(Nup85_all)
#simo.set_super_rigid_body_from_hierarchies(Nup120_all)
simo.set_super_rigid_body_from_hierarchies(Nup145c_all)
simo.set_super_rigid_body_from_hierarchies(Nup84_complex)

# used elsewhere

#resdensities=Nup145c_1_dens+\
#             Nup145c_2_dens+\
#             Nup145c_3_dens+\
#             Nup120_1_dens+\
#             Nup120_2_dens+\
#             Nup85_1_dens+\
#             Nup85_2_dens+\
#             Nup84_dens+\
#             Nup133_dens+\
#             Seh1_dens+\
#             Sec13_dens

# setup floppy bodies

simo.set_floppy_bodies()
