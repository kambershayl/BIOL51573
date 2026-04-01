#!/usr/bin/env python3
import argparse

###------------- accept and parse command line arguments
# create an argument parser object
parser = argparse.ArgumentParser(description = "This script calculates the number at a given position in the Fibonacci sequence")


parser.add_argument("job_name", help = "The name you want to give this job")
parser.add_argument("partition", help = "What partition (ex. Comp01)?")
parser.add_argument("nodes", help ="number of nodes")
parser.add_argument("qos", help = "qos is comp")
parser.add_argument("cpus_per_task", help = "number of CPUs")
parser.add_argument("time", help = "time in 0:00:00")
parser.add_argument("mail_user", help = "the email to send job info to")
# add a positional argument, in this case, the position in the Fibonacci sequence
parser.add_argument("position", help = "Position in the Fibonacci sequence", type = int)
# an optional argument for verbose output or not
# if 'store_true', this means assign "True" if the optional argument is specified 
# on the command line, so the default for 'store_true' is actually false
parser.add_argument("-v","--verbose", help = "Print verbose output", action = 'store_true')

# parse the arguments
args = parser.parse_args()

print("#!/bin/bash")
print(f"#SBATCH --job-name={args.job_name}")
print(f"#SBATCH --partition={args.partition}")
print(f"#SBATCH --nodes={args.nodes}")
print(f"#SBATCH --qos={args.qos}")
print(f"#SBATCH --cpus-per-task={args.cpus_per_task}")
print(f"#SBATCH --time={args.time}")
print("#SBATCH --output=blast_%j.out")
print("#SBATCH --error=blast_%j.err")
print("#SBATCH --mail-type = all")
print(f"#SBATCH --mail-user={args.mail_user}")

print("export OMP_NUM_THREADS=32")
print("module purge")
print("module load intel/18.0.1 impi/18.0.1 mkl/18.0.1")
print("cd $SLURM_SUBMIT_DIR")


# prompt the user for position in the Fibonacci sequence
# position = input("please enter a position:")


# initialize two integers
a,b = 0,1

for i in range(int(args.position)):
    a,b = b, a + b

fibonacci_number = a

if args.verbose:
    print(f"the fibonacci number for {args.position} is {fibonacci_number}")
else: 
    print(fibonacci_number)
