dirA=/path/to/no-xray.after_merge_filter_and_before_cluster.all_models/
dirB=/path/to/second_directory_or_empty_dir/
cutoff=40
name=clustering.no-xray-w500.40.0
./clustering_all.sh $dirA $dirB $cutoff $name

dirA=/path/to/no-xray.after_merge_filter_and_before_cluster.all_models/
dirB=/path/to/second_directory_or_empty_dir/
cutoff=40
name=clustering.no-xray-hub-w500.40.0
./clustering_hub.sh $dirA $dirB $cutoff $name
