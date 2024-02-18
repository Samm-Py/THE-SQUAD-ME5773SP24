#!/bin/bash
#
# ======================================================================
# This file executes a run time analysis the linalg.py file:
# 
#   sbatch job_linalg_study.slurm
#
# DISCLAIMER: 
# This file was created for educational purposes to be used in the
# ME 5773 High Performance Computing course at the University of Texas 
# at San Antonio to be used with Arc HPC cluster. 
# Use it at your own risk.
# 
#
# Authors: Alexis Cornidez
#          Samuel Roberts
#
# Last modification date: 02/18/2024
# Version: 0.1
# ======================================================================
#SBATCH -J JobLinalg_Study
#SBATCH -o outFileLinalg.txt    # Name of 'stdout' output file.
#SBATCH -e errFileLinalg.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of threads used by each task.
#SBATCH -t 00:05:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user alexis.cornidez@my.utsa.edu # Put your utsa-email here.
#SBATCH --mail-user samuel.roberts@my.utsa.edu # Put your utsa-email here.
#

date

# Print start time stamp
tstart=`date +%s%N` 
echo Starting job - 'date'

# Load Anaconda3 to be able to access the specific environment.
module load anaconda3

# Acivate the environment that you want to use.
conda activate envTeam3


# 
# Running the MKL_NUM_THREADS with 7 different values:
for num_threads in 1 2 4 8 16 20 40; do
	echo "----------------------"

		export MKL_NUM_THREADS=$num_threads

		# Print the Number of Threads on Each Run
	echo "Execution with MKL_NUM_THREADS=$num_threads"
# 


# Running linalg.py.

python3 linalg.py
echo "Running Python file"	

done
echo "Execution complete"
echo "-----------------"

# Print end time stamp

tend=`date +%s%N`

# Calculate the time difference

tdiff=$(( (tend-tstart)/1000000 ))

# Output calculation time
echo Calculations ended
echo Total CPU time $tdiff [ms]
