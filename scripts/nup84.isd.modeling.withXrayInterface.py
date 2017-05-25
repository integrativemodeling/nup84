from __future__ import print_function
import util
import IMP
import IMP.core
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi.mmcif
import IMP.pmi.restraints.crosslinking
import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.em
import IMP.pmi.restraints.em2d
import IMP.pmi.restraints.basic
import IMP.pmi.restraints.proteomics
import IMP.pmi.representation
import IMP.pmi.tools
import IMP.pmi.metadata
import IMP.pmi.samplers
import IMP.pmi.output
import IMP.pmi.macros

import os
import sys
sys.path.append('../util/')
import make_archive

rbmaxtrans = 2.00
fbmaxtrans = 2.00
rbmaxrot=0.04
nrmffiles=1000
nframes=100
nsteps=100
outputobjects = []
sampleobjects = []

m = IMP.Model()
#simo = IMP.pmi.representation.Representation(m,upperharmonic=True,disorderedlength=True)
simo = IMP.pmi.representation.Representation(m,upperharmonic=True,disorderedlength=False)

# We used HHpred to detect remote homologs for some input subunits
simo.add_metadata(IMP.pmi.metadata.Software(
          name='HHpred', classification='protein homology detection',
          description='Protein homology detection by HMM-HMM comparison',
          version='2.0.16',
          url='https://toolkit.tuebingen.mpg.de/hhpred'))
# We used PSIPRED to predict secondary structure for subunits
simo.add_metadata(IMP.pmi.metadata.Software(
          name='PSIPRED', classification='secondary structure prediction',
          description='Protein secondary structure prediction based on '
                      'position-specific scoring matrices',
          version='4.0',
          url='http://bioinf.cs.ucl.ac.uk/psipred/'))
# We used DISOPRED to predict (and remove) disordered regions in the subunits
simo.add_metadata(IMP.pmi.metadata.Software(
          name='DISOPRED', classification='disorder prediction',
          description='prediction of protein disorder', version=3,
          url='http://bioinf.cs.ucl.ac.uk/psipred/?disopred=1'))
simo.add_metadata(IMP.pmi.metadata.Citation(
          pmid='25161197',
          title="Structural characterization by cross-linking reveals the "
                "detailed architecture of a coatomer-related heptameric "
                "module from the nuclear pore complex.",
          journal="Mol Cell Proteomics", volume=13, page_range=(2927,2943),
          year=2014,
          authors=['Shi Y', 'Fernandez-Martinez J', 'Tjioe E', 'Pellarin R',
                   'Kim SJ', 'Williams R', 'Schneidman-Duhovny D', 'Sali A',
                   'Rout MP', 'Chait BT'],
          doi='10.1074/mcp.M114.041673'))

for subdir, zipname in make_archive.ARCHIVES.items():
    simo.add_metadata(IMP.pmi.metadata.Repository(
          doi="10.5281/zenodo.583173", root="../%s" % subdir,
          url="https://zenodo.org/record/583173/files/%s" % zipname,
          top_directory=None if subdir.endswith('.gz')
                        else os.path.basename(subdir)))
simo.add_metadata(IMP.pmi.metadata.Repository(
          doi="10.5281/zenodo.583173", root="..",
          url='https://zenodo.org/record/583173/files/nup84-v1.0.2.zip',
          top_directory='nup84-v1.0.2'))

if '--mmcif' in sys.argv:
    # Record the modeling protocol to an mmCIF file
    po = IMP.pmi.mmcif.ProtocolOutput(open('nup84.cif', 'w'))
    simo.add_protocol_output(po)

simo.dry_run = '--dry-run' in sys.argv

exec(open("nup84.topology.withXrayInterface.py").read())

#simo.translate_hierarchies_to_reference_frame(Nup84_complex)
simo.shuffle_configuration(100)
#simo.translate_hierarchies(Nup84_complex,(100,100,100))

simo.set_rigid_bodies_max_rot(rbmaxrot)
simo.set_floppy_bodies_max_trans(fbmaxtrans)
simo.set_rigid_bodies_max_trans(rbmaxtrans)
simo.set_floppy_bodies()
simo.setup_bonds()

prot = simo.prot
outputobjects.append(simo)
sampleobjects.append(simo)


ev = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(simo,resolution=10)
ev.add_to_model()
outputobjects.append(ev)

eb = IMP.pmi.restraints.basic.ExternalBarrier(simo,radius=300)
eb.add_to_model()
outputobjects.append(eb)

columnmap={}
columnmap["Protein1"]=0
columnmap["Protein2"]=2
columnmap["Residue1"]=1
columnmap["Residue2"]=3
columnmap["IDScore"]=4
columnmap["XLUniqueID"]=5

ids_map=IMP.pmi.tools.map()
ids_map.set_map_element(1.0,1.0)

xl1 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   '../data/yeast_Nup84_DSS.new.dat',
                                   length=21.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   filelabel="DSS",
                                   label="DSS")
xl1.add_to_model()
sampleobjects.append(xl1)
outputobjects.append(xl1)
xl1.set_psi_is_sampled(False)
psi=xl1.get_psi(1.0)[0]
psi.set_scale(0.05)


xl2 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   '../data/EDC_XL_122013.new.dat',
                                   length=16.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   filelabel="EDC",
                                   label="EDC")
xl2.add_to_model()
sampleobjects.append(xl2)
outputobjects.append(xl2)
xl2.set_psi_is_sampled(False)
psi=xl2.get_psi(1.0)[0]
psi.set_scale(0.05)

print('EVAL 1')
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))
simo.optimize_floppy_bodies(100)
print('EVAL 2')
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))

nframes=500
if '--test' in sys.argv: nframes=50
mc1=IMP.pmi.macros.ReplicaExchange0(m,
                                    simo,
                                    monte_carlo_sample_objects=sampleobjects,
                                    output_objects=outputobjects,
                                    crosslink_restraints=[xl1,xl2],
                                    #crosslink_restraints=[xl1],
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=2.5,
                                    number_of_best_scoring_models=50,
                                    monte_carlo_steps=10,
                                    number_of_frames=nframes,
                                    write_initial_rmf=True,
                                    initial_rmf_name_suffix="initial",
                                    stat_file_name_suffix="stat",
                                    best_pdb_name_suffix="model",
                                    do_clean_first=True,
                                    do_create_directories=True,
                                    global_output_directory="pre-2DEM_output.1",
                                    rmf_dir="rmfs/",
                                    best_pdb_dir="pdbs/",
                                    replica_stat_file_suffix="stat_replica",
                                    test_mode=simo.dry_run)
mc1.execute_macro()

rex1=mc1.get_replica_exchange_object()
print('EVAL 3')
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))

# 2DEM restraints
images = ['../data/nup84_kinked_from_class2.pgm']

em2d = IMP.pmi.restraints.em2d.ElectronMicroscopy2D(simo,
                                                    images,
                                                    resolution=1.0,
                                                    pixel_size = 5.91,
                                                    image_resolution = 30.0,
                                                    projection_number = 400)
# Point to the raw micrographs from which the class average was derived
# for completeness (we don't use these directly in the modeling)
r = IMP.pmi.metadata.Repository(doi="10.5281/zenodo.58025",
        url='https://zenodo.org/record/58025/files/Nup84complex_particles.spd')
l = IMP.pmi.metadata.FileLocation(repo=r, path='Nup84complex_particles.spd',
        details="Raw micrographs from which the class average was derived")
micrographs = IMP.pmi.metadata.EMMicrographsDataset(number=800, location=l)
for d in em2d.datasets:
    d.add_primary(micrographs)

em2d.add_to_model()
em2d.set_weight(500)
outputobjects.append(em2d)

print('EVAL 4')
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))

nframes=5000
if '--test' in sys.argv: nframes=10
mc2=IMP.pmi.macros.ReplicaExchange0(m,
                                    simo,
                                    monte_carlo_sample_objects=sampleobjects,
                                    output_objects=outputobjects,
                                    crosslink_restraints=[xl1,xl2],
                                    #crosslink_restraints=[xl1],
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=2.5,
                                    number_of_best_scoring_models=500,
                                    monte_carlo_steps=10,
                                    number_of_frames=nframes,
                                    write_initial_rmf=True,
                                    initial_rmf_name_suffix="initial",
                                    stat_file_name_suffix="stat",
                                    best_pdb_name_suffix="model",
                                    do_clean_first=True,
                                    do_create_directories=True,
                                    global_output_directory="output.1",
                                    rmf_dir="rmfs/",
                                    best_pdb_dir="pdbs/",
                                    replica_stat_file_suffix="stat_replica",
                                    replica_exchange_object=rex1,
                                    test_mode=simo.dry_run)
mc2.execute_macro()

if '--mmcif' in sys.argv:
    # Dump coordinates of previously-generated cluster representatives
    # Number of structures and dRMSD are from Table S4 in the Nup84 paper.
    r = IMP.pmi.metadata.Repository(doi="10.5281/zenodo.438727",
           url='https://zenodo.org/record/438727/files/nup84_localization.zip')
    pp = po._add_simple_postprocessing(num_models_begin=15000,
                                       num_models_end=2267)
    for cluster, num_models, drmsd, rep in (
                       ('1', 1257, 15.4, '31.0.rmf3'),
                       ('2', 1010, 12.7, '16.0.rmf3')):
        den = {}
        for d in po.all_modeled_components:
            den[d] = IMP.pmi.metadata.FileLocation(repo=r,
                                      path='localization/cluster%s/%s.mrc'
                                           % (cluster, d.lower()),
                                      details="Localization density for %s" % d)
        util.read_rmf_file(simo,
                           '../outputs/3-xray.after_cluster_on_hub.cluster'
                           '%s.top5.pdb.rmf.score/%s' % (cluster, rep))
        s = util.read_stat_file(
                           '../outputs/3-xray.after_cluster_on_hub.cluster'
                           '%s.top5.pdb.rmf.score/stat.filtered.out' % cluster)
        r = IMP.pmi.metadata.Repository(doi="10.5281/zenodo.583173",
                     url="https://zenodo.org/record/583173/files/"
                         "clus.%s.dcd" % cluster)
        f = IMP.pmi.metadata.FileLocation(path='.', repo=r,
                details="All ensemble structures for cluster %s" % cluster)
        c = po._add_simple_ensemble(pp, name="Cluster " + cluster,
                                    num_models=num_models, drmsd=drmsd,
                                    num_models_deposited=1,
                                    localization_densities=den,
                                    ensemble_file=f)
        m = po.add_model(c.model_group)
        # Center the mmCIF model so that it's consistent with our
        # PDB trajectories, which are centered in the same way
        m.transform = IMP.algebra.Transformation3D(-m.geometric_center)
        m.name = 'Best scoring model'
        m.stats = s

    po.flush()
