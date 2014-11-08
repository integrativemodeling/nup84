# Nup84 complex

These scripts demonstrate the use of [IMP](http://salilab.org/imp), [MODELLER](http://salilab.org/modeller), and [PMI](https://github.com/salilab/pmi) in the modeling of the Nup84 complex using 286 DSS/EDC chemical cross-links and an electron microscopy (EM) 2D class average.

First, [MODELLER](http://salilab.org/modeller) is used to generate
initial structures for the individual components in the Nup84 complex. Then, IMP
is used to model these components using DSS/EDC crosslinks and the electron microscopy 2D class average for the entire Nup84 complex.

The scripts work with the latest [IMP](http://salilab.org/imp) (develop branch).
A default build of IMP should work, but for most effective sampling, it should
be built with [MPI](http://integrativemodeling.org/nightly/doc/html/namespaceIMP_1_1mpi.html) so that replica exchange can be used.

## List of files and directories:

- `data`		                         contains all relevant data, input structures that were generated by MODELLER or deposited in PDB, etc.

- `scripts`
  - `nup84.isd.modeling.withXrayInterface.py`  the main IMP/PMI script modeling with 3 crystal interfaces
  - `nup84.isd.modeling.py`                    the main IMP/PMI script modeling with no crystal interfaces

  - `nup84.topology.withXrayInterface.py`      constructs Nup84 subunits with 3 crystal interfaces
  - `nup84.topology.py`                        constructs Nup84 subunits with no crystal interfaces

  - `nup84.merge.py`                           script to merge output files from all runs and cluster; filter threshold on total score can be set here
 
  - `MODELLER_scripts/Nup84` MODELLER scripts to generate comparative models of Nup84

  - `MODELLER_scripts/Nup85` MODELLER scripts to generate comparative models of Nup85

  - `MODELLER_scripts/Nup120` MODELLER scripts to generate comparative models of Nup120

  - `MODELLER_scripts/Nup145C` MODELLER scripts to generate comparative models of Nup145C

- `scripts/output.1/pdbs`    The best 500 models from the modeling are accumulated in this directory, and updated as the calculation proceeds.
- `scripts/output.1/rmfs`    The structures of the lowest temperature replica will be written here as [RMF files](http://integrativemodeling.org/rmf/).
- `scripts/output.1/stat.n.out`	 Log files. They contain all relevant numbers of the calculation.

## Running the MODELLER scripts:
- `cd scripts/MODELLER_scripts`
- `(cd Nup84 && python all_sjkim_final1.py > all_sjkim_final1.log)` : ScNup84N 7-488
- `(cd Nup84 && python all_sjkim_final2.py > all_sjkim_final2.log)` : ScNup84C 506-726
- `(cd Nup85 && python all_sjkim_final.py > all_sjkim_final.log)` : ScNup85 44-744
- `(cd Nup120 && python all_sjkim_final1.py > all_sjkim_final1.log)` : ScNup120 1-1037
- `(cd Nup145C && python all_sjkim_final.py > all_sjkim_final.log)` : ScNup145C 126-553
- Note that the Nup133 component is built as part of a [separate study](http://salilab.org/nup133/).

## Running the IMP/PMI scripts for the Nup84 complex:
with 3 crystal interfaces:
- `cd scripts`
- `python nup84.isd.modeling.withXrayInterface.py & > nup84.isd.modeling.withXrayInterface.out` (on a single processor; prepend `mpirun -np 4` or similar if you built IMP with MPI support)

with no crystal interfaces:
- `cd scripts`
- `python nup84.isd.modeling.py &> nup84.isd.modeling.out`

Next, merge and cluster the resulting models (this script can also be used to
combine results from multiple independent runs):
- `python nup84.merge.py`

Finally, analyze the resulting clusters:
- `python precision.py`
- `python accuracy_xray_interface.py`
- `python contact_map/make_contact_map.py`

## Information

_Author(s)_: Riccardo Pellarin, Elina Tjioe, and Seung Joong Kim

_Date_: October 6th, 2014

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: [![build info](https://salilab.org/imp/systems/?sysstat=6)](http://salilab.org/imp/systems/)

_Testable_: Yes.

_Parallelizeable_: Yes

_Publications_:
 - Yi Shi\*, Javier Fernandez-Martinez\*, Elina Tjioe\*, Riccardo Pellarin\*, Seung Joong Kim\*, Rosemary Williams, Dina Schneidman-Duhovny, Andrej Sali, Michael P. Rout, and Brian T. Chait, [Structural characterization by cross-linking reveals the detailed architecture of a coatomer-related heptameric module from the nuclear pore complex](http://mcponline.org/content/early/2014/08/26/mcp.M114.041673), Molecular & Cellular Proteomics, 2014, mcp.M114.041673.

 \*These authors contributed equally to this work as co-first authors.
