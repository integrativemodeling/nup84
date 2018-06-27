#!/usr/bin/env python

import unittest
import os
import sys
import subprocess
import glob

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
        p = subprocess.check_call(
                ["python", "nup84.isd.modeling.withXrayInterface.py",
                 "--mmcif", "--dry-run"])
        # Check size of output file
        with open("nup84.cif") as fh:
            wcl = len(fh.readlines())
        self.assertTrue(wcl >= 55260)

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
