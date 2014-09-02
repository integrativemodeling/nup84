#Nup84 complex
Nup84 modeling script using DSS/EDC crosslinks and 2D EM data.
Authors: Riccardo Pellarin, Elina Tjioe, and Seung Joong Kim

The script works with the latest IMP, PMI and isd_emxl libraries.
Compile IMP using mpi (needed for the replica exchange, use "module load mpi/openmpi-x86_64-nodlopen" on the cluster)

List of files and directories:

data		                         contains all relevant data, input structure, etc.

nup84.isd.modeling.withXrayInterface.py  the main modeling script with 3 crystal interfaces
nup84.isd.modeling.py                    the main modeling script with no crystal interfaces

nup84.topology.withXrayInterface.py      constructs Nup84 subunits with 3 crystal interfaces, as well as calculates the densities for the EM restraints
nup84.topology.py                        constructs Nup84 subunits with no crystal interfaces, as well as calculates the densities for the EM restraints

output.1/pdbs    the production will write the best scoring models into pdb files they are initialized and then updated as long as the calculation goes
                 (They are the best 500 models, so at the beginning they are empty, since you haven't start the calculation yet)

output.1/rmfs    the production will write the rmf3 files for lowest temperature replica.
			
stat.n.out	 log files. They contain all relevant numbers of the calculation.

Python dependencies:
biopython 		(to read fasta files)
sklearn   		(for the gaussian mixture model decomposition of the EM map)

Biopython and sklearn are required to run nup84 script:
------------------------------------------------------------
sudo yum install python-biopython
sudo yum install scikit-learn

Getting IMP, PMI, ISD_EMXL and compiling it with fast-build on Fedora:
-----------------------------------------------------------------------
git clone https://github.com/salilab/imp.git imp-latest
cd imp-latest/modules
git clone https://github.com/salilab/isd_emxl.git
git clone https://github.com/salilab/pmi.git
cd ../
module load mpi
./setup_git.py
cd ..
mkdir imp-latest-build
cd imp-latest-build/
cmake ../imp-latest -DCMAKE_CXX_COMPILER=mpicxx -DCMAKE_BUILD_TYPE=Release -DIMP_MAX_CHECKS=NONE -DIMP_MAX_LOG=SILENT
make

Running nup84 script:
---------------------------
with 3 crytal interfaces:
imp-latest-build/setup_environment.sh /path_to/mpirun -np 4 python nup84.isd.modeling.withXrayInterface.py &> nup84.isd.modeling.withXrayInterface.out

with no crytal interfaces:
imp-latest-build/setup_environment.sh /path_to/mpirun -np 4 python nup84.isd.modeling.py &> nup84.isd.modeling.out
