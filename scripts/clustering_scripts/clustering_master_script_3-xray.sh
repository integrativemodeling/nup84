dirA=/path/to/3-xray.after_merge_filter_and_before_cluster.all_models.6519/
dirB=/path/to/second_directory_or_empty_dir/
cutoff=40
name=clustering.3-xray-w500.40.0
./clustering_all.sh $dirA $dirB $cutoff $name

dirA=/salilab/park2/etjioe/em2d_run1/after_merging/3x_w500_0722/all_models.6856/
dirB=/salilab/park2/etjioe/clustering_scripts/empty_dir/
cutoff=40
name=clustering.3-xray-hub-w500.40.0
./clustering_hub.sh $dirA $dirB $cutoff $name
