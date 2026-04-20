#!/usr/bin/env python3

def read_fasta(fasta_file):
    genome_sequence = ""
    with open(fasta_file, 'r') as f:
        next(f)
        for line in f:
            genome_sequence = genome_sequence + line.strip()
    return genome_sequence


def read_gff(gff_file, genome_sequence):
    features = []
    with open(gff_file, 'r') as f:
        for line in f:
            cols = line.strip().split('\t')
            start = int(cols[3]) - 1
            end = int(cols[4])
            attributes = cols[8]
            attr_list = attributes.split(';')
            seq_id = None
            for attr in attr_list:
                if attr.startswith('ID='):
                    seq_id = attr[3:]
            sequence = genome_sequence[start:end]
            features.append((seq_id, sequence))
    return features


def write_output(features, output_file='covid_genes.fasta'):
    with open(output_file, 'w') as f:
        for seq_id, sequence in features:
            f.write('>' + seq_id + '\n')
            f.write(sequence + '\n')