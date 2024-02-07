#!/bin/bash




#SBATCH -J paralRun
#SBATCH -o outFile.%j.txt
#SBATCH -e errFile.%j.txt
#SBATCH -p compute1
#SBATCH -N 1 
#SBATCH -n 5
#SBATCH -c 10
#SBATCH -t 00:05:00


tstart=`date +%s%N`
echo Starting job - `date`

srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash ./twice.sh 2 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash ./twice.sh 7 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash ./twice.sh 6 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash ./twice.sh 1 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash ./twice.sh 3 &

echo waiting for all executions to complete 

wait

tend=`date +%s%N`

tdiff=$(((tend-tstart)/1000000000))

echo Calculation ended
echo Total CPU time $tdiff
