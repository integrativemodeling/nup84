#!/usr/bin/env python

"""This is a simple script to convert the multimodel PDB files into
   binary trajectories. We write the models as DCD (CHARMM/NAMD) trajectories,
   with each bead or residue represented as a single 'atom', in residue
   number order (the same order as in the mmCIF file.

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
_chain_atoms = {}
chain_num = 0
atom_index = 0
for line in fh:
    if line.startswith('ATOM'):
        atmnum = int(line[6:11])
        resnum = int(line[22:26])
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        chain_id = line[21]
        _chain_atoms[resnum] = (x,y,z)
        if atmnum == last_atom_of_chain[chain_num]:
            assert(chain_id == string.ascii_uppercase[chain_num])
            # Sort atoms by residue number (buggy old IMP::pmi used for Nup84
            # put all the beads at the start of a chain; we need to put those
            # back in the right place)
            for resnum in sorted(_chain_atoms.keys()):
                a = ag.atoms[atom_index]
                a.x, a.y, a.z = _chain_atoms[resnum]
                atom_index += 1
            _chain_atoms = {}
            chain_num += 1
    if line == 'ENDMDL\n':
        assert(_chain_atoms == {})
        assert(atom_index == last_atom_of_chain[-1])
        num_model += 1
        print("Written model %d" % num_model)
        chain_num = 0
        atom_index = 0
        d.append()
