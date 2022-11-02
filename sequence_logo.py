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
            length_sequence = len(line)

            #update the number of sequences 
            count_seq+=1 

            #for each letter in the sequence 
            for letter in line : 

                #update the alphabet 
                if letter not in alphabet and letter != "\n": 
                    alphabet.append(letter)
    
    return alphabet, count_seq, length_sequence 


"""
Create a matrix containing the number of representations of each letter of the alphabet for each column of the alignment

Input : 
    list containing all the letters of the alphabet 
    file containing the sequences 
    int equals to the length of the alignment 
    NB : we're assuming that each sequence has the same length (and if there are gap, it is represented with the symbol "-")

Output : 
    matrix 
"""
def countMatrix(alphabet, fichier, longueur) :

    #create matrix where each line represents a letter in the alphabet and each columns represent a column in the alignment of sequences 
    M = [[0]*longueur for i in range(len(alphabet))]
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
    for j in range(len(matrice[0])) : 
    #parcours par ligne             
        for i in range(len(matrice)) : 
            effectif = matrice[i][j]
            matrice[i][j] = effectif / count_seq
    return matrice



"""
Function to print the matrix 


"""
def affichage(matrice, alphabet, longueur_seq) : 
    num_colonne = []
    for i in range(longueur_seq) : 
        num_colonne.append(i)
    print("" + "\t" + str(num_colonne))
    for i in range(len(alphabet)) : 
        print(str(alphabet[i])+ "\t" + str(matrice[i]))


        
            

"""
MAIN FUNCTION
"""
def main(arg1) : 

    alphabet, nb_seq, longueur_seq = readFile(arg1)
    print("Il y a " + str(nb_seq) + str( " séquences"))
    print("l'alphabet est : " + str(alphabet))
    matrice_comptage = countMatrix(alphabet, arg1, longueur_seq)
    matrice_freq = freqMatrix(matrice_comptage, nb_seq)
    affichage(matrice_comptage,nb_seq)
    #affichage(matrice_freq, alphabet, longueur_seq)





if __name__ == "__main__":
    if len(sys.argv) <= 1 : 
        print("Missing arguments : use -h or --help")
    else : 
        if sys.argv[1] == "-h" or sys.argv[1] == "--help" : 
            help()
        else : 
            main(sys.argv[1])