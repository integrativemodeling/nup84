from __future__ import print_function
from modeller import *
from modeller.automodel import *
from modeller.scripts import complete_pdb
import fnmatch
import os
import sys
#import pylab

log.verbose()
env = environ()
#env.io.atom_files_directory = ['../']

######################### 1. build_profile.py ########################
##-- Read in the sequence database
#sdb = sequence_db(env)
##sdb.read(seq_database_file='pdball.pir', seq_database_format='PIR',
##         chains_list='ALL', minmax_db_seq_len=(1, 4000), clean_sequences=True)
#
##-- Write the sequence database in binary form
##sdb.write(seq_database_file='pdball.bin', seq_database_format='BINARY',
##          chains_list='ALL')
#
##-- Now, read in the binary database
#sdb.read(seq_database_file='pdball.bin', seq_database_format='BINARY',
#         chains_list='ALL')
#
##-- Read in the target sequence/alignment
#aln = alignment(env)
##aln.append(file='nup145.pir', alignment_format='PIR', align_codes='ALL')
#aln.append(file='3KFO.fasta.txt', alignment_format='FASTA', align_codes='ALL')
#
##-- Convert the input sequence/alignment into
##   profile format
#prf = aln.to_profile()
#
##-- Scan sequence database to pick up homologous sequences
#prf.build(sdb, matrix_offset=-450, rr_file='${LIB}/blosum62.sim.mat',
#          gap_penalties_1d=(-500, -50), n_prof_iterations=5,
#          check_profile=False, max_aln_evalue=0.01, gaps_in_target=False)
#
##-- Write out the profile in text format
#prf.write(file='all_build_profile_3kfo.prf', profile_format='TEXT')
#
##-- Convert the profile back to alignment format
#aln = prf.to_alignment()
#
##-- Write out the alignment file
#aln.write(file='all_build_profile_3kfo.ali', alignment_format='PIR')
#
#
######################### 2. compare.py ########################
#aln = alignment(env)
#
#for (pdb, chain) in (('3kfo', 'A'), ('3kfo', 'A')):
#    m = model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
#    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
#aln.malign()
#aln.malign3d()
#aln.compare_structures()
#aln.id_table(matrix_file='all_family.mat')
#env.dendrogram(matrix_file='all_family.mat', cluster_cut=-1.0)


######################## 3. align.py ########################
#aln = alignment(env)
#mdl = model(env, file='3kfo', model_segment=('FIRST:A','LAST:A'))
#aln.append_model(mdl, align_codes='3kfoA', atom_files='3kfo.pdb')
#aln.append(file='all_build_profile_3kfo.ali', align_codes='N133N')
##aln.append(file='1xksA.ali')
#
##aln.align(gap_penalties_1d=(-600, -400))
#aln.align2d()
#aln.write(file='all_N133N_3kfoA_align.ali', alignment_format='PIR')
#aln.write(file='all_N133N_3kfoA_align.pap', alignment_format='PAP')

#It begin1s from here
aln = alignment(env)
aln.append(file='all_align_begin.ali')
aln.write(file='all_align_final.ali', alignment_format='PIR')
aln.write(file='all_align_final.pap', alignment_format='PAP')
aln.id_table(matrix_file='all_align_final.mat')
aln.check()

#exit()
######################### 4. model-single.py ########################
class MyModel(automodel):
    def special_patches(self, aln):
        self.rename_segments('B', 44)

    def special_restraints(self, aln):
        rsr = self.restraints
        at = self.atoms
#       Add some restraints from a file:
#       rsr.append(file='my_rsrs1.rsr')

#       Residues 20 through 30 should be an alpha helix:
        #rsr.add(secondary_structure.alpha(self.residue_range('20:', '30:')))
#       Two beta-strands:
        #rsr.add(secondary_structure.strand(self.residue_range('1:', '6:')))
        #rsr.add(secondary_structure.strand(self.residue_range('9:', '14:')))
#       An anti-parallel sheet composed of the two strands:
        #rsr.add(secondary_structure.sheet(at['N:1'], at['O:14'],
        #                                  sheet_h_bonds=-5))
#       Use the following instead for a *parallel* sheet:
        #rsr.add(secondary_structure.sheet(at['N:1'], at['O:9'],
        #                                  sheet_h_bonds=5))

#       Restrain the specified CA-CA distance to 10 angstroms (st. dev.=0.1)
#       Use a harmonic potential and X-Y distance group.
        #http://salilab.org/modeller/manual/node27.html

        #DSS Intra-molecular Crosslinks        
        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:102:B'],
                                                         at['CA:163:B']),
                               mean=17.0, stdev=5.0))
                                       
        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:231:B'],
                                                         at['CA:238:B']),
                               mean=17.0, stdev=5.0))

        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:247:B'],
                                                         at['CA:237:B']),
                               mean=17.0, stdev=5.0))

        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:247:B'],
                                                         at['CA:345:B']),
                               mean=17.0, stdev=5.0))

        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:85:B'],
                                                         at['CA:64:B']),
                               mean=17.0, stdev=5.0))

        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:536:B'],
                                                         at['CA:564:B']),
                               mean=17.0, stdev=5.0))

        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:680:B'],
                                                         at['CA:734:B']),
                               mean=17.0, stdev=5.0))

        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:718:B'],
                                                         at['CA:733:B']),
                               mean=17.0, stdev=5.0))
                                   
        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:718:B'],
                                                         at['CA:734:B']),
                               mean=17.0, stdev=5.0))

        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:729:B'],
                                                         at['CA:733:B']),
                               mean=17.0, stdev=5.0))

        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:729:B'],
                                                         at['CA:734:B']),
                               mean=17.0, stdev=5.0))


        #EDC Intra-molecular Crosslinks        
        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:85:B'],
                                                         at['CA:63:B']),
                               mean=15.0, stdev=2.0))
                                       
        rsr.add(forms.upper_bound(group=physical.xy_distance,
                               feature=features.distance(at['CA:87:B'],
                                                         at['CA:59:B']),
                               mean=15.0, stdev=2.0))
                              
        #rsr.add(forms.upper_bound(group=physical.xy_distance,
        #                       feature=features.distance(at['NZ:73'],
        #                                                 at['NZ:168']),
        #                       mean=17.0, stdev=5.0))

        #rsr.add(forms.upper_bound(group=physical.xy_distance,
        #                       feature=features.distance(at['CA:73'],
        #                                                 at['CA:168']),
        #                       mean=17.0, stdev=5.0))

        #rsr.add(forms.upper_bound(group=physical.xy_distance,
        #                       feature=features.distance(at['NZ:82'],
        #                                                 at['NZ:168']),
        #                       mean=17.0, stdev=5.0))

        #rsr.add(forms.upper_bound(group=physical.xy_distance,
        #                       feature=features.distance(at['CA:82'],
        #                                                 at['CA:168']),
        #                       mean=17.0, stdev=5.0))

a = MyModel(env,
              alnfile='all_align_final.ali',
              knowns=('3f3fD', '4lctD', '2qx5B', '3eweD'),
              #knowns=('4j73A'),  
              sequence='ScNup85',
              assess_methods=(assess.DOPE, assess.GA341))
            
a.starting_model= 1                 # index of the first model
a.ending_model  = 30                # index of the last model
                                    # (determines how many models to calculate)
if '--test' in sys.argv: a.ending_model = 1
a.make()                            # do homology modeling

"""
a = automodel(env, 
              alnfile='all_align_final1.ali',
              #knowns=('3t97C', '3ghgA', '3ghgA', '3u0cA'),
              knowns=('4j73A'),  
              sequence='SEA2',
              assess_methods=(assess.DOPE, assess.GA341))

a.starting_model = 1
a.ending_model = 20

a.make()
"""

#a.rename_segments('A', 601)

######################## 5. evaluate_model.py ########################
#env = environ()
#env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
#env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990001.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N1.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990002.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N2.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990003.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N3.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990004.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N4.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990005.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N5.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990006.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N6.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990007.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N7.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990008.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N8.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990009.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N9.profile',
#              normalize_profile=True, smoothing_window=15)
#
## read model file
#mdl = complete_pdb(env, 'N133N.B99990010.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='N133N10.profile',
#              normalize_profile=True, smoothing_window=15)
#
#
## read model file
#mdl = complete_pdb(env, '1xks.pdb')
## Assess with DOPE:
#s = selection(mdl)   # all atom selection
#s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='1xksA.profile',
#              normalize_profile=True, smoothing_window=15)
              

######################## 6. plot_profiles.py ########################
#def get_profile(profile_file, seq):
#    """Read `profile_file` into a Python array, and add gaps corresponding to
#       the alignment sequence `seq`."""
#    # Read all non-comment and non-blank lines from the file:
#    f = file(profile_file)
#    vals = []
#    for line in f:
#        if not line.startswith('#') and len(line) > 10:
#            spl = line.split()
#            vals.append(float(spl[-1]))
#    # Insert gaps into the profile corresponding to those in seq:
#    for n, res in enumerate(seq.residues):
#        for gap in range(res.get_leading_gaps()):
#            vals.insert(n, None)
#    # Add a gap at position '0', so that we effectively count from 1:
#    vals.insert(0, None)
#    return vals
#
#e = environ()
#a = alignment(e, file='all_align_1xks_final1.ali')
#
#template = get_profile('1xksA.profile', a['1xksA'])
#model1 = get_profile('N133N1.profile', a['N133N'])
#model2 = get_profile('N133N2.profile', a['N133N'])
#model3 = get_profile('N133N3.profile', a['N133N'])
#model4 = get_profile('N133N4.profile', a['N133N'])
#model5 = get_profile('N133N5.profile', a['N133N'])
#model6 = get_profile('N133N6.profile', a['N133N'])
#model7 = get_profile('N133N7.profile', a['N133N'])
#model8 = get_profile('N133N8.profile', a['N133N'])
#model9 = get_profile('N133N9.profile', a['N133N'])
#model10 = get_profile('N133N10.profile', a['N133N'])
#
## Plot the template and model profiles in the same plot for comparison:
#pylab.figure(1, figsize=(10,6))
#pylab.xlabel('Alignment position')
#pylab.ylabel('DOPE per-residue score')
#pylab.plot(model1, color='red', linewidth=2, label='Model1')
#pylab.plot(model2, color='blue', linewidth=2, label='Model2')
#pylab.plot(model3, color='cyan', linewidth=2, label='Model3')
#pylab.plot(model4, color='orange', linewidth=2, label='Model4')
#pylab.plot(model5, color='violet', linewidth=2, label='Model5')
#pylab.plot(model6, color='yellow', linewidth=2, label='Model6')
#pylab.plot(model7, color='magenta', linewidth=2, label='Model7')
#pylab.plot(model8, color='gray', linewidth=2, label='Model8')
#pylab.plot(model9, color='pink', linewidth=2, label='Model9')
#pylab.plot(model10, color='black', linewidth=2, label='Model10')
#
#pylab.plot(template, color='green', linewidth=2, label='Template (3kfoA)')
##pylab.legend(loc=0)
#pylab.savefig('all_dope_profile_final1_N133N.png', dpi=150)
