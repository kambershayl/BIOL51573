#!/usr/bin/env python3

import argparse
# imports the argparse module

from gff_functions import read_fasta, read_gff, write_output
# imports the 3 functins I wrote in gff_functions.py, which I put in the same directory as this script

def main():
    # main is just a function that holds all the steps of the script in order
    # it is the main function that will call all of the other functions
    # technically, I could write this entire script without a main function

    parser = argparse.ArgumentParser(description = "this script will collect data on the name of the files")
    # created an object called parser. It reads what I type on the command line
    # the description is more for me than it is the code

    parser.add_argument("fasta", help = "the name of the fasta file you want to analyze")
    parser.add_argument("gff", help = "the name of the gff file you want to analyze")
    # tells parser to expect two arguments after the script name in the command line

    args = parser.parse_args()
    # this is where parse actually reads and stores what I typed on the command line
    # it stores them as args.fasta and args.gff
    # args is an object that holds the fasta and gff files
    # .fasta and .gff are the attribute names on args
    # if I call the object args, then I can shorten the name for the arguments to args.fasta and args.gff

    genome = read_fasta(args.fasta)
    # read_fasta is a function that I imported from gff_functions2.py
    # this takes my read_fasta function that I imported, uses args.fasta,
    # which is an attribute of the object args,
    # and it returns one DNA string named genome_sequences


    features = read_gff(args.gff, genome)
    # read_gff is a function that I imported from gff_functions2.py
    # it passes args.gff through my read_gff function. 
    # This returns a list of sequence id and sequence pairs
    # the final product is stored as the features variable

    write_output(features)
    # features is the output of read_gff
    # write_output is a function that I imported from gff_functions2.py
    # calls my write_output function and passes through my list of features
    print(f"{len(features)} features written to covid_genes.fasta")

if __name__ == '__main__':
    main()