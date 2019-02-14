import IMP
import IMP.pmi1
import IMP.pmi1.macros
import sys

model=IMP.Model()

mc=IMP.pmi1.macros.AnalysisReplicaExchange0(model,
                  stat_file_name_suffix="stat",
                  #merge_directories=["path/to/run1", "path/to/run2"],
                  global_output_directory="./output.1")

feature_list=["ISDCrossLinkMS_Distance_intrarb",
              "ISDCrossLinkMS_Distance_interrb",
              "ElectronMicroscopy2D",
              "ISDCrossLinkMS_Data_Score",
              "ISDCrossLinkMS_Psi_1.0_",
              "ISDCrossLinkMS_Sigma_1_",
              "LinkerRestraint",
              "ExcludedVolumeSphere_",
              "SimplifiedModel_Link_"]

prefiltervalue=300,
if '--test' in sys.argv: prefiltervalue=800
nclusters=1
mc.clustering("SimplifiedModel_Total_Score_None",
              "rmf_file",
              "rmf_frame_index",
              alignment_components=None,
              rmsd_calculation_components=None,
              distance_matrix_file="distance.rawmatrix.pkl",
              load_distance_matrix_file=False,
              number_of_best_scoring_models=15000,
              prefiltervalue=prefiltervalue,
              #first_and_last_frames=[0.0,0.5],
              outputdir="kmeans_50_%d" % nclusters,
              feature_keys=feature_list,
              #display_plot=True,
              get_every=1,
              skip_clustering=False,
              number_of_clusters=nclusters
              )
