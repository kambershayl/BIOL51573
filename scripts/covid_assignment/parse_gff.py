#!/usr/bin/env python3

import argparse
from gff_functions import read_fasta, read_gff, write_output

def main():
    parser = argparse.ArgumentParser(description = "this script will collect data on the name of the files")
    parser.add_argument("fasta", help = "the name of the fasta file you want to analyze")
    parser.add_argument("gff", help = "the name of the gff file you want to analyze")
    args = parser.parse_args()
    # if I call the object args, then I can shorten the name for the arguments to args.fasta and args.gff

    genome_sequence = read_fasta(args.fasta)
    # read_fasta is a function that I imported from gff_functions2.py
    features = read_gff(args.gff, genome_sequence)
    # read_gff is a function that I imported from gff_functions2.py
    write_output(features)
    # features is the output of read_gff
    # write_output is a function that I imported from gff_functions2.py
    print(f"{len(features)} features written to covid_genes.fasta")

if __name__ == '__main__':
    main()