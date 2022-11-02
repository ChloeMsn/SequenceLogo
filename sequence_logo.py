#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys 
import numpy as np 

def help() : 
    print("HELP")



'''
Read the file, count number of sequences and read the alphabet 

Input : 
    file containing the sequences, each sequence is written on one line 
Output : 
    list containing all the letters of the alphabet 
    int equals to the number of sequences 

'''
def readFile(fichier) :
    with open(fichier) as file : 

        #count number of sequences 
        count_seq = 0 
        #list containing all the letters of the alphabet
        alphabet = []

        #for each sequence
        for line in file :  

            #update the number of sequences 
            count_seq+=1 

            #for each letter in the sequence 
            for letter in line : 

                #update the alphabet 
                if letter not in alphabet : 
                    alphabet.append(letter)
    
    return alphabet, count_seq 


"""
Create a matrix containing the number of representations of each letter of the alphabet for each column of the alignment

Input : 
    list containing all the letters of the alphabet 
    file containing the sequences 
    int equals to the length of the alignment 
    NB : we're assuming that each sequence has the same length (and if there are gap, it is represented with the symbol "-")
"""
def countMatrix(alphabet, fichier, longueur) :

    #create matrix where each line represents a letter in the alphabet and each columns represent a column in the alignment of sequences 
    M = [[0]*longueur for i in range(alphabet)]
    with open(fichier) as file :  

        #for each sequence 
        for line in file : 

            #for each character in the sequence 
            for indice_colonne in range(len(line)) :
                char = line[indice_colonne]

                #if the character is in the alphabet we increase the count for this character in the column number 'indice_colonne'
                if char in alphabet : 

                    #the index of the line corresponds to the index of the index of the character in the list alphabet
                    indice_ligne = alphabet.index(char)
                    M[indice_ligne][indice_colonne] += 1
    return M 


def freqMatrix(matrice, count_seq) : 
    #parcours par colonne 
    for j in len(matrice[0]) : 
    #parcours par ligne             
        for i in len(matrice) : 
            effectif = matrice[i][j]
            matrice[i][j] = effectif / count_seq

        
            
            

             

    



def main(arg1) : 

    print("main")



if __name__ == "__main__":
    if len(sys.argv) <= 1 : 
        print("Missing arguments : use -h or --help")
    else : 
        if sys.argv[1] == "-h" or sys.argv[1] == "--help" : 
            help()
        else : 
            main(sys.argv[1])