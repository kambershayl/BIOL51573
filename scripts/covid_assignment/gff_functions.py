#!/usr/bin/env python3

def read_fasta(fasta_file):
    # basically says "someone will hand you a filename when you are called, refer to it as fasta_file"
    # so whatever I send into the function, the function will call fasta_file

    genome_sequence = ""
    # just creating an empty string so that I can gradually add to it

    with open(fasta_file, "r") as infile:
        # opens the file for reading and calls it "infile". With will also automatically close it

        next(infile)
        # "next" will skip the first line of the fasta file, per the instructions

        for line in infile:
            # loops through every remaining line in infile
            # again, infile is the fasta file I sent into the function after it has been read

            genome_sequence += line.strip()
            # all I'm doing here is stripping the newline characters and adding it into a variable called genome_sequence
            # At the end, genome_sequence will have my full covid genome sequence from the fasta file
    return genome_sequence
# sends the dna string back into parse_gff where it is stored as genome_sequence

def read_gff(gff_file, genome_sequence):
    # this defines the function, but this time, it is taking two inputs
    # the first input is the gff file, and second input is genome_sequence, 
    # which is the output of read_fasta()

    extracted_features = []
    # again, making a new list to sit empty. I will add into it next. 
    # I am putting sequence ID, sequence pairs into the list

    with open(gff_file, "r") as file:
        # this opens the gff file for reading. 
        # gff_file is going to be whatever input I call into the function first
        # the "r" is for reading
        # once I call it into the function, the function will refer to it as "file"

        for line in file:
            # this is going to loop through all the lines in the gff file

            line = line.strip()
            # this should strip all the newline characters
            # line is the name of the variable I chose for the loop
            # so this is going through each line and overwriting it with the stripped version of hat line
            
            if not line or line.startswith("#"):
                # in python, an empty string is considered false
                # so the "if not line" statement will take care of entirely blank lines
                # like .strip() but on a line-level scale
                # "or line.startswith('#')" is a way to filter out comments
                # comments start with a tag
                continue
                # since I want to filter out blank lines and comments, 
                # "continue" is basically just saying to skip them in the loop
                # the loop restarts at the next gff line when "continue" is used

            cols = line.split("\t")
            # so this splits each line of the gff file into a list of columns
            # the "\t" is what I chose to split it by. Here, that is a tab character
            # this works for a gff file
            # but for a csv, I would probably choose a comma. 

            if len(cols) < 9:
                continue
            # this isn't an incredibly important line. It just skips the row if it doesn't have 9 columns 
            # the code might not work if it runs into this issue

            #if cols[2] != "gene":  
            #    continue
            # I only want columns that are genes, not CDS or whatever else
            # I am saying if the 3rd column is not equal to gene, ignore it or "continue"
            # but this isn't actually needed

            begin = int(cols[3])
            end = int(cols[4])
            # this is me choosing columns 4 and 5, per the directions
            # I changed them to integers
            # I need them to be actual numbers so that I can slice the dna string
            # you can't slice with text

            attributes = cols[8]
            # this is grabbing the 9th column which includes the sequence id in the gff file

            sequence_id = ""
            # making an empty string this time. I am about to add into it

            for item in attributes.split(";"):
                # so first, I split the attributes variable (which is just column 9) by semicolons
                # then I created a loop 

                if item.startswith("ID="):
                    # not all parts of attributes are the ID

                    sequence_id = item.replace("ID=", "")
                    # so it is cutting off the ID= portion of the gff file
                    # and it stores the actual sequence ID under the variable sequence_id
                    # sequence_id is an empty string I made above

                    break
                # break stops the loop once I find what I need
                # don't forget this whole thing is one giant loop
                # so that's why sequence_id is okay with just one sequence id inside, yet I still end up with multiple in the end

            extracted_sequence = genome_sequence[begin - 1:end]
            # Use the start and end coordinates to slice out the dna from the genome
            # genome_sequence is the second part of the input that I gave to the function
            # you have to do begin - 1 because python indexing starts at 0, 
            # but gff indexing starts at 1
            # if the gene starts at position 266 in the gff file, python would find that base at position 265 in the string

            extracted_features.append((sequence_id, extracted_sequence))
            # I made an empty list named extracted_features towards the top of the function
            # .append() is finally adding content into the list
            # the content is 1) the sequence ID I got from one of the loops above
            # and 2) the extracted sequence that I just created in the coding line above
    return extracted_features
# I return the list that I made with the sequence id and the sliced sequence piece
# I chose to make extracted_features a list and not a string because I needed to store two pieces of information together
# It's like every point I appended is a list of two within a larger list

def write_output(features, output_file='covid_genes.fasta'):
    # my last function in the script
    # so technically, it takes two inputs
    # in parse_gff.py, I only give it one input
    # the other output, I am defining at the same time I am defining the function
    # it needs to have the value for output_file input,
    # but I set this equal to 'covid_genes.fasta'

    with open(output_file, 'w') as genes:
        # the reason I don't have to have a returned variable here is because I said 'w'
        # my machine knows that I am writing into a file with this
        # so this will open covid_genes.fasta
        # the 'w' indicates that it is opening it for writing 
        # genes is an opened file object which will allow me to write into the file
        # I have to have a file object to interact with the opened file

        for seq_id, sequence in features:
            # this loops through the features list

            genes.write('>' + seq_id + '\n')
            # .write() is a built-in python method that belongs to file objects 
            # here, I am adding a carrot + the seq_id portion of the list, 
            # and then I'm adding a new line with \n
            genes.write(sequence + '\n')
            # this inputs the sequence portion of the string and at the end of the sequence, 
            # it makes a new line

# mainly used methods on file objects
# .split()
# .strip()
# .startswith()
# .open()
# .replace()