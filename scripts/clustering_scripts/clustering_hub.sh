#!/bin/bash

rm -r best_pdb
mkdir -p best_pdb
rm -f best_pdb/*.pdb

#cutoff=20.0
#system=`echo "no-xray-new-hub"`
#rm -rf clustering.$system.$cutoff

dirA=$1
dirB=$2
cutoff=$3
system=$4
rm -rf clustering.$system.$cutoff

#dirA=/salilab/park2/etjioe/final_nup84_complex/after_merging_3runs/after_em2d_filter_from_class2/em2d_no-xray_run1-3/filtered_no-xray_run1-3_0.76/
#dirB=/salilab/park2/etjioe/final_nup84_complex/after_merging_3runs/after_em2d_filter_from_class2/em2d_no-xray_run4-6/filtered_no-xray_run4-6_0.76/ 

#/salilab/park2/etjioe/Nup84_XL/after_merging/Modeling_after_EM2D_filter_of_top_5000_models_with_threshold_0.76/duplicate_no-xray_filtered_pdbs_by_em2d_with_threshold_0.76
#dirA=/salilab/park2/etjioe/Nup84_XL/after_merging/Modeling_after_EM2D_filter_of_top_5000_models_with_threshold_0.76/4-xray_filtered_pdbs_by_em2d_with_threshold_0.76
#dirB=/salilab/park2/etjioe/Nup84_XL/after_merging/Modeling_after_EM2D_filter_of_top_5000_models_with_threshold_0.76/duplicate_4-xray_filtered_pdbs_by_em2d_with_threshold_0.76


for i in $dirA/*.pdb
do
newname=`echo $i | sed "s|$dirA/|best_pdb/A|g"`
cp $i $newname
done

for i in $dirB/*.pdb
do
newname=`echo $i | sed "s|$dirB/|best_pdb/B|g"`
cp $i $newname
done


mkdir -p clustering
rm -f clustering/clus*.pdb
rm -f clustering/clus*.score.dat
rm -f clustering/cluster.dat
rm -f clustering/coor.xyz
rm -f clustering/scores.dat

onepdb=`ls best_pdb/*.pdb | awk '(NR==1){print }'`

nconf=`ls best_pdb/*.pdb | wc | awk '{print $1}'`
echo $nconf $onepdb

ncoord=`cat $onepdb | grep ' CA ' | awk 'BEGIN {FIELDWIDTHS=" 6 5 1 4 1 3 1 1 4 1 3 8 8 8 6 6 6 4"};{print}' | wc | awk '{print $1}'`

echo $onepdb $ncoord

# filter chains ($8=="E"||$8=="G"||$8=="F"||$8=="B")

((k=0)) ; for i in best_pdb/*.pdb ; do ((k++)) ; echo "XYZ" $k $i ; grep ' CA ' $i | awk 'BEGIN {FIELDWIDTHS=" 6 5 1 4 1 3 1 1 4 1 3 8 8 8 6 6 6 4"};{print $12,$13,$14}' ; done > clustering/coor.xyz
for i in best_pdb/*.pdb ; do  echo $i ; done > clustering/xyz.pdblist

echo 'clustering/coor.xyz' > clustering/clus.in
echo 'clustering/xyz.tmp' >> clustering/clus.in
echo $nconf >> clustering/clus.in
echo $ncoord >> clustering/clus.in
echo 0 >> clustering/clus.in
echo 5 >> clustering/clus.in
echo $cutoff >> clustering/clus.in
echo clustering/cluster.dat >> clustering/clus.in
echo clustering/ccenter.dat >> clustering/clus.in

./cluster.x < clustering/clus.in > clustering/clus.out

rm -f clustering/xyz.tmp
rm -f clustering/clus.*.score.dat

((k=0))
for cmember in `cat clustering/cluster.dat | grep -v '#' | awk '{print $2}'`
do
   ((k++))

   pdbname=`awk '(NR=='"$k"'){print }' clustering/xyz.pdblist`
   framen=`echo $pdbname | tr -s '.' ' ' | tr -s '/' ' ' | awk '{print $2}'`
   echo $framen

   echo $cmember $pdbname $k

   echo "MODEL        1" >> clustering/clus.$cmember.pdb
   cat $pdbname >> clustering/clus.$cmember.pdb
   #echo "ENDMDL" >> clustering/clus.$cmember.pdb
   
   if [ ! -e clustering/clus.$cmember ]
   then
   mkdir clustering/clus.$cmember
   fi
   
   if [[ $pdbname == *best_pdb/A* ]]
   then
     rmffilename=`echo $pdbname | sed "s|best_pdb/A|$dirA/|g"  | sed "s/\.pdb/.rmf3/g" `   
   fi
   
   if [[ $pdbname == *best_pdb/B* ]]
   then   
     rmffilename=`echo $pdbname | sed "s|best_pdb/B|$dirB/|g"  | sed "s/\.pdb/.rmf3/g" `
   fi

   echo $rmffilename
   cp $rmffilename  clustering/clus.$cmember
   
done

mv clustering clustering.$system.$cutoff
