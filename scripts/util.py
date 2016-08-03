from __future__ import print_function

import RMF
import IMP.rmf

import os
import sys
import tempfile
import shutil
import contextlib

@contextlib.contextmanager
def temp_dir():
    tmpdir = tempfile.mkdtemp()
    yield tmpdir
    shutil.rmtree(tmpdir, ignore_errors=True)

def _remove_densities(in_file, out_file):
    m = IMP.Model()

    rh = RMF.open_rmf_file_read_only(in_file)
    h = IMP.rmf.create_hierarchies(rh, m)
    for component in h[0].get_children():
        for rep in component.get_children():
            if rep.get_name() == 'Densities':
                IMP.atom.destroy(rep)

    rh = RMF.create_rmf_file(out_file)
    IMP.rmf.add_hierarchies(rh, h)
    IMP.rmf.save_frame(rh)


def read_rmf_file(simo, fname):
    with temp_dir() as t:
        cleaned_rmf = os.path.join(t, "clean.rmf")
        _remove_densities(in_file=fname, out_file=cleaned_rmf)

        for c in simo.get_component_names():
            simo.set_coordinates_from_rmf(c, cleaned_rmf, 0,
                                          force_rigid_update=True)
