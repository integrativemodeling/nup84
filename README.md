# Nup84 complex

These scripts demonstrate the use of [IMP](http://salilab.org/imp), [MODELLER](http://salilab.org/modeller), and [PMI](https://github.com/salilab/pmi) in the modeling of the Nup84 complex using DSS/EDC crosslinks and 2D EM data.

First, [MODELLER](http://salilab.org/modeller) is used to generate
initial structures for the individual components in the Nup84 complex. Then, IMP
is used to model these components using DSS/EDC crosslinks and the electron microscopy 2D class average for the entire Nup84 complex.

The scripts work with the latest [IMP](http://salilab.org/imp) (develop branch).
A default build of IMP should work, but for most effective sampling, it should
be built with [MPI](http://integrativemodeling.org/nightly/doc/html/namespaceIMP_1_1mpi.html) so that replica exchange can be used.

## List of files and directories:

- data		                         contains all relevant data, input structure, etc.

- scripts
  - nup84.isd.modeling.withXrayInterface.py  the main modeling script with 3 crystal interfaces

  - nup84.isd.modeling.py                    the main modeling script with no crystal interfaces

  - nup84.topology.withXrayInterface.py      constructs Nup84 subunits with 3 crystal interfaces, as well as calculates the densities for the EM restraints

  - nup84.topology.py                        constructs Nup84 subunits with no crystal interfaces, as well as calculates the densities for the EM restraints

  - nup84.merge.py                           script to merge output files from all runs ; filter threshold on total score can be set here
 
  - vmd_scripts/rmdstt.tcl                   VMD script to launch RMSD Trajectory Tool window 

  - vmd_scripts/nup84_3-xray_density.tcl     VMD script to calculate localization density for Nup84 with 3 crystal interfaces

  - vmd_scripts/nup84_no-xray_density.tcl    VMD script to calculate localization density for Nup84 with no crystal interfaces

  - vmd_scripts/ALPS_motif_density.tcl       VMD script to calculate localization density for Nup84 at ALPS motif regions 

  - chimera_scripts/nup84_density.cmd        Chimera script to view all localization density files 


- output.1/pdbs    the production will write the best scoring models into pdb files they are initialized and then updated as long as the calculation goes
                 (They are the best 500 models, so at the beginning they are empty, since you haven't start the calculation yet)

- output.1/rmfs    the production will write the rmf3 files for lowest temperature replica.
			
- stat.n.out	 log files. They contain all relevant numbers of the calculation.

Python dependencies:
- biopython 		(to read fasta files)
- sklearn   		(for the gaussian mixture model decomposition of the EM map)

## Biopython and sklearn are required to run nup84 script:
- sudo yum install python-biopython
- sudo yum install scikit-learn

## Running nup84 script:
with 3 crystal interfaces:
- `python nup84.isd.modeling.withXrayInterface.py & > nup84.isd.modeling.withXrayInterface.out` (on a single processor; prepend `mpirun -np 4` or similar if you built IMP with MPI support)
- `python nup84.merge.py`
- `clustering_master_script_3-xray.sh`
- `python nup84.analysis.py`

with no crystal interfaces:
- `python nup84.isd.modeling.py &> nup84.isd.modeling.out`
- `python nup84.merge.py`
- `clustering_master_script_no-xray.sh`
- `python nup84.analysis.py`

## Running VMD script:
- vmd after_merging/all_models/[ALL].pdb -e vmd_scripts/rmsdtt.tcl 
- In RMSD Trajectory Tool top window, type 'all', then click the button 'ALIGN' to align all pdb models
- In vmd command line, type 'source vmd_scripts/nup84_3-xray_density.tcl' to create localization density dx files

## Running Chimera script:
- chimera [ALL].dx chimera_scripts/nup84_density.cmd 

## Information

_Author(s)_: Riccardo Pellarin, Elina Tjioe, and Seung Joong Kim

_Date_: September 2nd, 2014

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: None

_Testable_: Yes.

_Parallelizeable_: Yes

_Publications_:
 - Yi Shi\*, Javier Fernandez-Martinez\*, Elina Tjioe\*, Riccardo Pellarin\*, Seung Joong Kim\*, Rosemary Williams, Dina Schneidman-Duhovny, Andrej Sali, Michael P. Rout, and Brian T. Chait, [Structural characterization by cross-linking reveals the detailed architecture of a coatomer-related heptameric module from the nuclear pore complex](http://mcponline.org/content/early/2014/08/26/mcp.M114.041673), Molecular & Cellular Proteomics, 2014, mcp.M114.041673.

 \*These authors contributed equally to this work as co-first authors.
