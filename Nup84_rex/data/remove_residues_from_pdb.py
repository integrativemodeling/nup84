#!/usr/bin/python

import os


def within(residue, ranges):
  for s, e in ranges:
    if s <= residue <= e:
      return True
  return False



def remove_ranges_from_pdb(infile, outfile, ranges):
  with open(infile, 'r') as inf:
    with open(outfile, 'w') as outf:
      for line in inf:
        if line.startswith('ATOM'):
          try:
            resno = int(line[22:26].strip())
            if within(resno, ranges):
              continue
          except ValueError:
            pass
        outf.write(line)



class Pdb(object):
  def __init__(self, name):
    self.name = name
    self.ranges = []


def process_disordered_file(disordered_file):
  pdbs = {}
  with open(disordered_file, 'r') as inf:
    for line in inf:
      line = line.strip()
      cmd, rest = line.split(':', 1)
      if cmd == 'FILE':
        alias, name = rest.split(':', 1)
        pdbs[alias] = Pdb(name)
      else:
        try:
          p = pdbs[cmd]
        except KeyError:
          raise Exception, 'I do not know file %s' % cmd
        ranges = [int(x) for x in rest.split('-')]
        p.ranges.append((ranges[0], ranges[1]))
  for p in pdbs.itervalues():
    root, ext = os.path.splitext(p.name)
    new_file = '%s_new%s' % (root, ext)
    print '%s => %s' % (p.name, new_file)
    remove_ranges_from_pdb(p.name, new_file, p.ranges)


import optparse
P = optparse.OptionParser()
P.add_option('--disordered_file', '-d', action='store', type='string',
    help='file with disordered regions')
opts, args = P.parse_args()
if not opts.disordered_file:
  print '--disordered_file is required'
  exit()

process_disordered_file(opts.disordered_file)
