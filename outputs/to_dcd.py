#!/usr/bin/env python

"""This is a simple script to convert the multimodel PDB files into
   binary trajectories. We write the models as DCD (CHARMM/NAMD) trajectories,
   with each bead or residue represented as a single 'atom', in residue
   number order (the same order as in the mmCIF file).

   We use the updated version of MDTools that's bundled with Chimera, so you
   may need to change sys.path accordingly, below.
"""

from __future__ import print_function
import string
import sys
sys.path.append('/opt/chimera-1.11-1.fc24/share/Trajectory/DCD/MDToolsMarch97/')
import md
import gzip

# Serial number of the last atom in each chain (in chain order)
last_atom_of_chain = (657, 1272, 2205, 3248, 3681, 3991, 4282)

# Make an empty set of atoms
ag = md.AtomGroup()
for i in range(last_atom_of_chain[-1]):
    atom = md.Atom()
    ag.atoms.append(atom)

if len(sys.argv) != 3:
    print("Usage: %s [input pdb.gz] [output DCD file]" % sys.argv[0],
          file=sys.stderr)
    sys.exit(1)

d = md.DCDWrite(sys.argv[2], ag)
fh = gzip.open(sys.argv[1])
num_model = 0
chain_num = 0
atom_index = 0
for line in fh:
    if line.startswith('ATOM'):
        atmnum = int(line[6:11])
        chain_id = line[21]
        assert(chain_id == string.ascii_uppercase[chain_num])
        a = ag.atoms[atom_index]
        a.x = float(line[30:38])
        a.y = float(line[38:46])
        a.z = float(line[46:54])
        if atmnum == last_atom_of_chain[chain_num]:
            chain_num += 1
        atom_index += 1
    if line == 'ENDMDL\n':
        assert(atom_index == last_atom_of_chain[-1])
        num_model += 1
        print("Written model %d" % num_model)
        chain_num = 0
        atom_index = 0
        d.append()
