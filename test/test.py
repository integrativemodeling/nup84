#!/usr/bin/env python

import unittest
import os
import sys
import subprocess
import glob
import ihm.reader
try:
    from ihm import cross_linkers
except ImportError:
    cross_linkers = None

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(unittest.TestCase):
    def run_modeller_script(self, script_dir, script_name, model_name, resrng):
        """Run a Modeller script and test the output model"""
        os.chdir(os.path.join(TOPDIR, 'scripts', 'MODELLER_scripts',
                              script_dir))
        # Run script
        p = subprocess.check_call(["python", script_name, "--test"])
        # Make sure PDB was produced with the requested residue range
        with open('%s.B99990001.pdb' % model_name) as fh:
            pdb_lines = [x for x in fh.readlines() if x.startswith('ATOM')]
        rng = (int(pdb_lines[0][22:26]), int(pdb_lines[-1][22:26]))
        self.assertEqual(rng, resrng)

    def test_nup84n(self):
        """Test generation of Nup84N model"""
        self.run_modeller_script('Nup84', 'all_sjkim_final1.py',
                                 'ScNup84N', (7, 488))

    def test_nup84c(self):
        """Test generation of Nup84C model"""
        self.run_modeller_script('Nup84', 'all_sjkim_final2.py',
                                 'ScNup84C', (506, 726))

    def test_nup85(self):
        """Test generation of Nup85 model"""
        self.run_modeller_script('Nup85', 'all_sjkim_final.py',
                                 'ScNup85', (44, 744))

    def test_nup120(self):
        """Test generation of Nup120 model"""
        self.run_modeller_script('Nup120', 'all_sjkim_final1.py',
                                 'ScNup120', (1, 1037))

    def test_nup133N(self):
        """Test generation of Nup133N model"""
        self.run_modeller_script('Nup133', 'all_sjkim_final1.py',
                                 'ScNup133N', (56, 480))

    def test_nup133C(self):
        """Test generation of Nup133C model"""
        self.run_modeller_script('Nup133', 'all_sjkim_final2.py',
                                 'ScNup133C', (490, 1155))

    def test_nup145c(self):
        """Test generation of Nup145C model"""
        self.run_modeller_script('Nup145C', 'all_sjkim_final.py',
                                 'ScNup145C', (126, 553))

    def test_no_xray(self):
        """Test model building with no X ray interfaces"""
        os.chdir(os.path.join(TOPDIR, 'scripts'))
        self.run_imp_script('nup84.isd.modeling.py')

    def test_xray(self):
        """Test model building with X ray interfaces"""
        os.chdir(os.path.join(TOPDIR, 'scripts'))
        self.run_imp_script('nup84.isd.modeling.withXrayInterface.py')

    def test_mmcif(self):
        """Test generation of mmCIF output"""
        os.chdir(os.path.join(TOPDIR, 'scripts'))
        if os.path.exists("nup84.cif"):
            os.unlink("nup84.cif")
        # Potentially override methods that need network access
        env = os.environ.copy()
        env['PYTHONPATH'] = os.path.join(TOPDIR, 'test', 'mock') \
                            + ':' + env.get('PYTHONPATH', '')
        p = subprocess.check_call(
                ["python", "nup84.isd.modeling.withXrayInterface.py",
                 "--mmcif", "--dry-run"], env=env)
        # Check output file
        self._check_mmcif_file('nup84.cif')

    def _check_mmcif_file(self, fname):
        with open(fname) as fh:
            s, = ihm.reader.read(fh)
        self.assertEqual(len(s.citations), 1)
        self.assertEqual(len(s.software), 6)
        self.assertEqual(len(s.orphan_starting_models), 9)
        # Should be a single states, of two models
        self.assertEqual(len(s.state_groups), 1)
        self.assertEqual(len(s.state_groups[0]), 1)
        self.assertEqual(len(s.state_groups[0][0]), 2)
        # Check # of spheres and atoms in each model
        models = [g[0] for g in s.state_groups[0][0]]
        self.assertEqual([len(m._spheres) for m in models], [4282, 4282])
        self.assertEqual([len(m._atoms) for m in models], [0, 0])

        # Should be 2 ensembles (clusters)
        self.assertEqual([e.num_models for e in s.ensembles],
                         [1257, 1010])
        # Check localization densities
        self.assertEqual([len(e.densities) for e in s.ensembles], [7, 7])
        self.assertEqual([len(e.sequence) for e in s.entities],
                         [726, 744, 1037, 1157, 712, 349, 297])
        self.assertEqual([a.details for a in s.asym_units],
                         ['Nup84', 'Nup85', 'Nup120', 'Nup133', 'Nup145c',
                          'Seh1', 'Sec13'])
        # 3 restraints - 2 sets of crosslinks, and one EM2D image
        xl1, xl2, em2d = s.restraints
        if cross_linkers is None:
            self.assertEqual(xl1.linker_type, 'DSS')
        else:
            self.assertEqual(xl1.linker.auth_name, cross_linkers.dss.auth_name)
        self.assertEqual(len(xl1.experimental_cross_links), 164)
        self.assertEqual(len(xl1.cross_links), 164)
        self.assertEqual(xl1.dataset.location.path,
                         'nup84-v1.0.3/data/yeast_Nup84_DSS.new.dat')
        self.assertEqual(sum(len(x.fits) for x in xl1.cross_links), 328)

        if cross_linkers is None:
            self.assertEqual(xl2.linker_type, 'EDC')
        else:
            self.assertEqual(xl2.linker.auth_name, cross_linkers.edc.auth_name)
        self.assertEqual(len(xl2.experimental_cross_links), 127)
        self.assertEqual(len(xl2.cross_links), 127)

        self.assertAlmostEqual(em2d.image_resolution, 30.0, places=1)
        self.assertEqual(em2d.number_raw_micrographs, 800)
        self.assertEqual(len(em2d.fits), 2)
        self.assertEqual(em2d.dataset.location.path,
                         'nup84-v1.0.3/data/nup84_kinked_from_class2.pgm')
        self.assertEqual(em2d.dataset.parents[0].location.path,
                         'Nup84complex_particles.spd')

    def run_imp_script(self, script_name):
        """Run IMP modeling"""
        p = subprocess.check_call(["python", script_name, "--test"])
        p = subprocess.check_call(["python", "nup84.merge.py", "--test"])
        p = subprocess.check_call(["python", "precision.py"])
        os.unlink("precision.dat")
        p = subprocess.check_call(["python", "accuracy_xray_inferface.py"])
        p = subprocess.check_call(["python", "contact_map/make_contact_map.py"])
        os.unlink("kmeans_50_1/cluster.0/XL_table.pdf")

if __name__ == '__main__':
    unittest.main()
