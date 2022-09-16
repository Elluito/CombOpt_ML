#!/bin/bash -l
# Submission script for serial Python job
# Luis Alfredo Avendano  2021-10-22

# Run from the current directory and with current environment
#$ -cwd -V

# Ask for some time (hh:mm:ss max of 48:00:00)
#$ -l h_rt=01:00:00

# ASk for some GPU
#$ -l coproc_k80=1

# Ask for some memory (by default, 1G, without a request)
#$ -l h_vmem=8G
#$ -pe smp 3

# Send emails when job starts and ends
#

# Now run the job
#module add anaconda
module add cuda/11.1.1

conda activate GraphNetworks
which python
#nvcc --version
#~python $1 $2 $3 $4 $5 $6
#python src/main.py --input $1 --output $2 --num-walks 20 --walk-length 80 --window-size 5 --dimensions 10 --OPT1 True --OPT2 True --OPT3 True --until-layer 6
python src/main.py --input graph/karate-mirrored.edgelist --output emb/karate-mirrored.emb --num-walks 20 --walk-length 80 --window-size 5 --dimensions 10 --OPT1 True --OPT2 True --OPT3 True --until-layer 6
#python src/main.py --input graph/karate-mirrored.edgelist --output emb/karate-mirrored.emb
