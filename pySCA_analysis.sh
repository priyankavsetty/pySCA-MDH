#!/bin/bash
# Author: Priyanka V. Setty
# Date: 2023-01-20
# Usage: ./pySCA_analysis.sh <input fasta file of amino acid sequences> <reference sequence as fasta file> <reference group number for sequences based on GC content> <output directory> <conservation plot title> 
# Purpose:

in=$1
ref=$2
n=$3
outdir=$4
title=$5

aln=$(echo "Inputs/aligned_$n").fasta
anotSeq=$(echo "Inputs/annotated_$n").an
db=$(echo "Outputs/annotated_$n").db
json=$(echo "Inputs/di_$n").json
plt=$(echo "Inputs/di_plot_$n").png


# Step 1: run mafft alignment on input fasta sequences and save the aligned file in fasta format
mafft --6merpair --thread -1 --keeplength --addfragments $in $ref > $aln

# Step 2: Annotate the MSA (need to run these commands in the installed pySCA folder )
./annotate_MSA.py $f -o $anotSeq -a 'pfam'

# Step 3: Process the MSA
./scaProcessMSA.py $anotSeq -s 2pwz -c A -f 'Escherichia coli' -t -n

# Step 4: SCA core calculations
./scaCore.py $db

# Step 5: Get first order statistics ( conservation values and plot)
python pySCA.py -i $db -t $title -d $json -p $plt