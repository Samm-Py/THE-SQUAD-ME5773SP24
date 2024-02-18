#!/bin/bash


#SBATCH -o outFile.%j.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of threads used by each task.
#SBATCH -t 00:05:00          # Maximum estimated run time (dd-hh:mm:ss)
#


module load anaconda3
conda activate envTeam3

export OMP_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1

srun --exclusive  -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash -c "python3 integral.py" & 
