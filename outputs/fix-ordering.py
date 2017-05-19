#!/usr/bin/env python

from __future__ import print_function
import sys
import string

fh_in = open(sys.argv[1])
fh_out = open(sys.argv[2], 'w')

# Serial number of the last atom in each chain (in chain order)
last_atom_of_chain = (657, 1272, 2205, 3248, 3681, 3991, 4282)

num_model = 0
_chain_lines = {}
chain_num = 0
atom_index = 0
for line in fh_in:
    if line.startswith('ATOM'):
        atmnum = int(line[6:11])
        resnum = int(line[22:26])
        chain_id = line[21]
        _chain_lines[resnum] = line
        if atmnum == last_atom_of_chain[chain_num]:
            assert(chain_id == string.ascii_uppercase[chain_num])
            # Sort atoms by residue number (buggy old IMP::pmi used for Nup84
            # put all the beads at the start of a chain; we need to put those
            # back in the right place)
            for resnum in sorted(_chain_lines.keys()):
                atom_index += 1
                fh_out.write("ATOM  %5d" % (atom_index,)
                             + _chain_lines[resnum][11:])
            _chain_lines = {}
            chain_num += 1
    else:
        if line == 'ENDMDL\n':
            assert(_chain_lines == {})
            assert(atom_index == last_atom_of_chain[-1])
            chain_num = 0
            atom_index = 0
        fh_out.write(line)
