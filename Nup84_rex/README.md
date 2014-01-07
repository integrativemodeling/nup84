Nup84 modeling script using DSS/EDC crosslinks and 3DEM data.
Authors: Riccardo Pellarin, Elina Tjioe

The script works with the latest IMP, PMI (checkout resolution-zero branch: `git checkout resolution-zero`) and isd2 libraries.
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

Getting IMP, PMI, ISD2 and compiling it on Fedora:
-------------------------------------------------------------
git clone https://github.com/salilab/imp.git imp-latest
cd imp-latest/modules
git clone https://github.com/salilab/isd2.git
git clone https://github.com/salilab/pmi.git
cd pmi
git checkout resolution-zero
cd ../../
module load mpi/openmpi-x86_64
./setup_git.py
cd ..
mkdir imp-latest-build
cd imp-latest-build/
cmake ../imp-latest
make

Biopython and sklearn are required to run nup84 script:
------------------------------------------------------------
sudo yum install python-biopython
sudo yum install scikit-learn

Running nup84 script:
---------------------------
imp-latest-build/setup_environment.sh python nup84.modeling.rex.py &> nup84.modeling.rex.out

