# -*- coding: utf-8 -*-

"""

Created on Fri Jul 5 15:36:35 2024
@author: Marina Moro López

"""

from tkinter.filedialog import askopenfile

def main():
    
    print('Please select the file with the virus you want to modify')
    virus_file = askopenfile(mode='r')
    virus_seq = virus_file.readlines()[1:]
    virus_seq = ''.join(virus_seq).replace('\n', '')

    DNA_guide, mutated_virus_seq, mold = knock_in(virus_seq)
            
    mutated_virus_file = open('MUTATED_SEQUENCE.txt', 'w')
    mutated_virus_file.write(mutated_virus_seq)
    mutated_virus_file.close()

    guide_file = open('GUIDE.txt', 'w')
    guide_file.write(DNA_to_RNA(DNA_guide))
    guide_file.close()

    mold_file = open('MOLD.txt', 'w')
    mold_file.write(mold)
    mold_file.close()


def knock_in(virus_seq):

    print('Please select the file with the gene you want to add to the virus')
    added_gene_file = askopenfile(mode='r')
    added_gene_seq = added_gene_file.readlines()[1:]
    added_gene_seq = ''.join(added_gene_seq).replace('\n', '')
    
    mutation_position = int(input("Introduce the numeric position where you want to enter the new gene (e.g. 1, 25, 203): "))
    while mutation_position <= 0:
        print('Invalid input. Introduce positive number. ')
        mutation_position = int(input("Introduce the numeric position where you want to enter the new gene (e.g. 1, 25, 203): "))
            
    DNA_guide = virus_seq[mutation_position-25:mutation_position+25]
    mutated_virus_seq = virus_seq[:mutation_position] + added_gene_seq + virus_seq[mutation_position:]
    mold = virus_seq[mutation_position-25:mutation_position] + added_gene_seq + virus_seq[mutation_position:mutation_position+25]
    
    return DNA_guide, mutated_virus_seq, mold


def DNA_to_RNA(DNA_guide):
    
    RNA_guide = ""
    for base in DNA_guide:
        if base == "T":
            RNA_guide += "A"
        elif base == "A":
            RNA_guide += "U"
        elif base == "C":
            RNA_guide += "G"
        elif base == "G":
            RNA_guide += "C"
    
    return RNA_guide


main()
