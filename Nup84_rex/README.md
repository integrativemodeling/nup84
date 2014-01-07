Nup84 modeling script using DSS/EDC crosslinks and 3DEM data.
Authors: Riccardo Pellarin

The script works with the latest IMP, PMI (checkout resolution-zero branch: git checkout resolution-zero) and isd2 libraries.
Compile imp using mpi (needed for the replica exchange, use "module load mpi/openmpi-x86_64-nodlopen" on the cluster)

List of files and directories:

data			contains all relevant data, input structure, etc.
nup84.modeling.rex.py   the main modeling script (rex stands for replica exchange)
nup84.topology.py       constructs Nup84 subunits, as well as calculates the densities for the EM restraints
pdbs                    the production will write the best scoring models into pdb files
rmfs			the production will write the rmf3 files for lowest temperature replica. Each
			rmf3 file contains a single structure. rmf3 files are grouped into directories 
			containing 100 files (group.0, group.1, group.2, etc.)

Python dependencies:
biopython 		(to read fasta files)
sklearn   		(for the gaussian mixture model decomposition of the EM map)

How to install:
(elina can you write down what you did?)
