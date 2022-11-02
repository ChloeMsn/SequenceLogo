#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys 
import numpy as np 
import math 


'''
Function printing the hekp 

'''
def help() : 
    print("*****************************************************")
    print("*" + "\t" + " HOW TO RUN sequence_logo.py "+"\t" + "            *")
    print("*****************************************************")
    print('\n')

    print("\t" + "The script must be launched with at least one argument." + '\n' + '\t'+ "A file containing aligned sequences must be given" + '\n')
    print("Example : ./sequence_logo.py exemple.txt")
    print('\n')





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
Create a matrix containing the number of representations of each letter of the alphabet for each column in the alignment

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

"""
Create a matrix containing the frequency of each letter of the alphabet for each column in the alignment

Input : 
    matrix containing the number of representations of each letter of the alphabet for each column in the alignment
    int equals to the number of sequences 
    NB : we're assuming that each sequence has the same length (and if there are gap, it is represented with the symbol "-")

Output : 
    matrix 
"""

def freqMatrix(matrice, count_seq) : 
    #parcours par colonne 
    for j in range(len(matrice[0])) : 
    #parcours par ligne             
        for i in range(len(matrice)) : 

            #stock the number of apperances of a given letter in the column j 
            effectif = matrice[i][j]

            #calculate frequency
            matrice[i][j] = round(effectif / count_seq, 2)

    return matrice



"""
Function to print the matrix 

Input : 
    matrix to print
    list containing all the letters of the alphabet 
    int corresponding to the length of the alignement

Output : 
    No output
"""
def affichage(matrice, alphabet, longueur_seq) : 

    #to print the number of the columns 
    num_colonne = []
    for i in range(longueur_seq) : 
        num_colonne.append(i)
    print("" + "\t" + str(num_colonne) +"\n")

    #to print the value 
    for i in range(len(alphabet)) : 
        print(str(alphabet[i])+ "\t" + str(matrice[i]))


"""
Calculate the entropy os Shannon and a correction factor for each column

Input : 
    matrix containing the frequency of each letter of the alphabet for each column in the alignment
    matrix containing the number of representations of each letter of the alphabet for each column in the alignment
    list containing all the letters of the alphabet 

Output : 
    list containing the value of the entropy for each column

"""

def entropie(matrice_freq, matrice_comptage, alphabet) : 

    #create list of entropy 
    liste_R = []
     #parcours par colonne 
    for j in range(len(matrice_freq[0])) : 

        #intialize entropy to 0 for each column 
        H = 0 
        count_symbol = 0 
     
    #parcours par ligne             
        for i in range(len(matrice_freq)) :

            #to assure that we dont count "-" as a symbol if there is a "-" in the alignment  
            if "-" in alphabet and alphabet.index("-") != i : 

                #if the letter appears in the column 
                if matrice_freq[i][j] != 0 : 

                    #increment number of symbols 
                    count_symbol += matrice_comptage[i][j]

                    #calculate H for the current character 
                    H += matrice_freq[i][j] * math.log2(matrice_freq[i][j])

        #size of the alphabet, as "-" is not counted as a symbol we have to retrieve 1 
        if "-" in alphabet : 
            alphabet_size = len(alphabet) -1 
        else : 
            alphabet_size = len(alphabet)
        
        #calculate correction factor 
        e = (alphabet_size - 1) / (2*count_symbol*math.log(count_symbol))

        #calculate R 
        R = math.log2(alphabet_size) - (H+e)

        #update the list 
        liste_R.append(R)

    return liste_R

    
def size(matrice_freq, alphabet, liste_R) : 

    matrice_size = M = [[0]*len(matrice_freq[0]) for i in range(len(alphabet))]

    #parcours par colonne 
    for j in range(len(matrice_freq[0])) : 

        #parcours par ligne 
        for i in range(len(matrice_freq)) : 

            matrice_size[i][j] = matrice_freq[i][j]*liste_R[j]
    
    
    return matrice_size


        
            

"""
MAIN FUNCTION
"""
def main(arg1) : 
    print("\n")
    print("######################################################################################")
    print("################################# DEBUT DU PROGRAMME #################################")
    print("######################################################################################")
    print("\n")
    alphabet, nb_seq, longueur_seq = readFile(arg1)
    print("Il y a " + str(nb_seq) + str( " séquences"))
    print("l'alphabet est : " + str(alphabet))
    print("\n")

    print("Matrice de comptage : ")
    matrice_comptage = countMatrix(alphabet, arg1, longueur_seq)
    M = np.copy(matrice_comptage)
    affichage(matrice_comptage,alphabet,longueur_seq)

    print("\n" + "Matrice de fréquence : ")
    matrice_freq = freqMatrix(matrice_comptage, nb_seq)
    affichage(matrice_freq, alphabet, longueur_seq)
    print("\n")

    print("Calcul de l'entropie : ")
    #print(M)
    liste_R = entropie(matrice_freq, M, alphabet)
    print(liste_R)
    print("\n")

    taille = size(matrice_freq,alphabet,liste_R) 
    print("Taille des lettres dans le graphe : ")
    affichage(taille,alphabet,longueur_seq) 
    print("\n")  

    print("######################################################################################")
    print("################################## FIN DU PROGRAMME ##################################")
    print("######################################################################################")
    print("\n")



if __name__ == "__main__":
    if len(sys.argv) <= 1 : 
        print("Missing arguments : use -h or --help to get some informations")
    else : 
        if sys.argv[1] == "-h" or sys.argv[1] == "--help" : 
            help()
        else : 
            main(sys.argv[1])