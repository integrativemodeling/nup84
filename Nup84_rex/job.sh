#!/bin/bash
#
#$ -S /bin/bash
#$ -l netapp=1G,scratch=1G
#$ -cwd
#$ -o /netapp/sali/pellarin/nup84/Nup84_rex/
#$ -e /netapp/sali/pellarin/nup84/Nup84_rex/
#$ -j y
#$ -l arch=linux-x64
#$ -l mem_free=2G
#$ -pe ompi 64
#$ -R yes
#$ -l netappsali=2G                  
#$ -l scrapp=2G
#$ -V
#$ -l h_rt=300:00:0.
#$ -t 1
#$ -N j10.4

# load MPI modules
#module load openmpi-x86_64
module load openmpi-1.6-nodlopen
module load sali-libraries
# IMP stuff

export IMP=/netapp/sali/pellarin/imp-250114/imp-pmi-fast/setup_environment.sh


# write hostname and starting time 
hostname
date

# run the job
mpirun -np $NSLOTS $IMP python nup84.modeling.rex.py 

# done
date
