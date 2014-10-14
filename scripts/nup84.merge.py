import IMP
import IMP.pmi
import IMP.pmi.macros

is_mpi=False # set to True to run in parallel (requires mpi4py)

model=IMP.Model()

mc=IMP.pmi.macros.AnalysisReplicaExchange0(model,
                  stat_file_name_suffix="stat",
                  merge_directories=["path/to/run1", "path/to/run2"],
                  global_output_directory="./output.1",
                  rmf_dir="rmfs/")

feature_list=["ISDCrossLinkMS_Distance_intrarb",
              "ISDCrossLinkMS_Distance_interrb",
              "ElectronMicroscopy2D",
              "ISDCrossLinkMS_Data_Score",
              "ISDCrossLinkMS_Psi_1.0_",
              "ISDCrossLinkMS_Sigma_1_",
              "LinkerRestraint",
              "ExcludedVolumeSphere_",
              "SimplifiedModel_Link_"]

mc.clustering("SimplifiedModel_Total_Score_None",
              "rmf_file",
              "rmf_frame_index",
              alignment_components=["Nup85","Nup145c","Sec13","Seh1"],
              rmsd_calculation_components=["Nup85","Nup145c","Sec13","Seh1","Nup120","Nup84"],
              distance_matrix_file="distance.rawmatrix.pkl",
              load_distance_matrix_file=False,
              number_of_best_scoring_models=15000,
              prefiltervalue=300,
              #first_and_last_frames=[0.0,0.5],
              outputdir="./",
              feature_keys=feature_list,
              #display_plot=True,
              is_mpi=is_mpi,
              get_every=1,
              skip_clustering=True,
              #number_of_clusters=1,
              density_custom_ranges={"Nup84_density":["Nup84"],"Nup145c_density":["Nup145c"],"Nup85_density":["Nup85"],"Seh1_density":["Seh1"],"Nup133_density":["Nup133"],"Nup120_density":["Nup120"],"Sec13_density":["Sec13"]})
