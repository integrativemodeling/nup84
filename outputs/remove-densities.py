#!/usr/bin/env python

"""Simple script to remove the Densities nodes from an RMF file.

   The original simulations of the Nup84 turned on GMM representation
   of the subunits so that they could be fitted into 3D EM density
   maps, so the RMF files here contain this representation. However,
   this functionality was not used in the final modeling,
   and has been turned off in the modeling scripts. Consequently,
   the molecular hierarchy in each RMF file does not match that
   created by the modeling scripts. If you want to use a modeling
   script together with these RMFs (e.g. by using IMP.rmf.link_hierarchies())
   then first strip out the Densities nodes with this script.
"""

from __future__ import print_function
import RMF
import IMP.rmf
import sys

if len(sys.argv) != 3:
    print("Usage: %s infile outfile\n" % sys.argv[0], file=sys.stderr)
    sys.exit(1)

m = IMP.Model()

rh = RMF.open_rmf_file_read_only(sys.argv[1])
h = IMP.rmf.create_hierarchies(rh, m)
for component in h[0].get_children():
    for rep in component.get_children():
        if rep.get_name() == 'Densities':
            IMP.atom.destroy(rep)

rh = RMF.create_rmf_file(sys.argv[2])
IMP.rmf.add_hierarchies(rh, h)
IMP.rmf.save_frame(rh)
