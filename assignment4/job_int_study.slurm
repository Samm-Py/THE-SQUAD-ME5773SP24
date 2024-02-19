#!/bin/bash


#SBATCH -o integral_thread.txt    # Name of 'stdout' output file.
#SBATCH -e integral_thread_err.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of threads used by each task.
#SBATCH -t 00:30:00          # Maximum estimated run time (dd-hh:mm:ss)
#


module load anaconda3
conda activate envTeam3

array = ('1','2','4','8')
for i in "${array[@]}"
do
	export OMP_NUM_THREADS="$i"
	export NUMEXPR_NUM_THREADS="$i"
	srun --exclusive  -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash -c "python3 integral.py"  
done

