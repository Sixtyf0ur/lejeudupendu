# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:36:50 2021

@author: MLL-
"""

import os
import pickle
import random
import string

def playerprompt():
    """Prompt for player's name"""
    while 1:
        player = input("Please enter your player Name:")

        if player=="":
            continue
        else:
            break
             
    #print(player)        
    return player

def verifypath(path=""):
    if path=="":
        path=os.getcwd()+"//lejeudupenduscores"#binary so no extensions
        newgame=True
    return path, newgame

def getplayersdata(path,newgame):
    """"Gets players scores"""
    if newgame:
        my_tbl={}#empty dictionnary 1st instance of the game
    else:
        with open(path,"rb+") as fscores:
            my_unpick=pickle.Unpickler(fscores)
            my_tbl=my_unpick.load()
    return my_tbl
def singleplayerscore(player, table):
    try:
        pscore = table[player]
        keyExists=True
    except KeyError:
        keyExists=False
    if keyExists==False:
        table[player]=0 # add new player to the table and give him a score of 0
    return table

def updatescore(player, table, score):
    table[player]=max(score, table[player]) #Keeps top score history vs new score
    return table

def wplayersdata(path,table):
    with open(path,"wb") as fscores:
        my_pickler=pickle.pickler(fscores)
        my_pickler.dump(table)
    return None

def lemot():
    wd=input("Choisissez un mot [not case sensitive] a faire deviner, ou alors laissez vide pour obtenir un mot aleatoirement:")
    if wd =="":
        with open(os.getcwd()+"//lejeudupendumots","r") as mots:
            
            wd=mots.read().split("\n")#liste tous les mots
            wd=wd[random.randrange(0, len(wd))]#choisi un mot aleatoirement
    else:
        with open(os.getcwd()+"//lejeudupendumots","a") as mots:
            mots.write(wd)
    return wd

# def lejeu(player,table,path,lemot):
#     displ=""
#     for i in range(len(lemot)):
#         displ+="_ "
#     i=0
#     k=0
#     lettrestentees=[""]
#     while i<8:
        
#         print("Devinez le(s) mot(s):\n",displ)
#         lettre=input("Entrez une lettre [not case sensitive]:")
#         blntente=True
        
#         for u in range(len(lettrestentees)):
#             if lettre.upper()==lettrestentees[u]:
#                 print("vous avez deja tente cette lettre...")
#                 break
#                 blntente=False
                
#         if blntente==True: # Si cest une nouvelle tentative, dans ce cas, on affiche le nouveau resultat
#             lettrestentees.append(lettre.upper())
#             bln_gagne=False
#             for j in range(len(lemot)):
#                 #print(lemot[j].lower(),lettre.lower(),lemot[j].lower()==lettre.lower())
#                 if lemot[j].lower()==lettre.lower():
#                     bln_gagne=True
#                     k+=1
#                     if k==len(lemot):
#                         print("Felicitations! vous avez decouvert le mot")
#                     ls=list(displ)
#                     ls[2*j]=lettre.lower()
#                     displ="".join(ls)
#                     #displ=displ[:j] + lettre.lower() + displ[j+1:]
#             if bln_gagne==False:
#                 i+=1
#                 print("dommage, il ne vous reste plus que {} tentatives".
#                       format(8-i))

#     return None


def lejeu(lemot):
    displ=""
    lm=list(lemot)
    k=0
    for i in range(len(lemot)):
        displ+="_ "
        k+=1
    i=0
    lstlettre=[""]
    
    while i<8: #8vies
        bln_routine = True
        print("Devinez le(s) mot(s):\n",displ)
        l=input("Entrez une lettre [not case sensitive]:")

        try:
            l=l.lower()
             
        except Exception:
            print("Vous avez rentre un mauvais format de caractere")
            bln_routine = False
        for p in range(len(lstlettre)):
            if l==lstlettre[p]:
                print("Vous avez deja joue ce caractere '{}'...".format(l))
                bln_routine = False
        
        if bln_routine == True:
            lstlettre.append(l)#Update the lettre list
            if lemot.count(l)>0:
                k=k-lemot.count(l)
                if k<1:
                    pendu(9)
                    print("Felicitations! vous avez decouvert le mot: '{}' avec {} tentatives restantes".format(lemot,8-i))
                    return 8-i #end routine and return the score
                    
                else:
                    pendu(i)
                ls=list(displ)
                for j in range(len(lemot)):
                    if lm[j]==l:
                        ls[2*j]=l
                        
                displ="".join(ls)
            else:
                i+=1 
                pendu(i)
                print("dommage, il ne vous reste plus que {} tentatives".
                                      format(8-i))
        
    return -1

def pendu(score):
    dico={
        0:" o\n"+"/|\\\n"+"/ \\",
        1:" o\n"+"/|\\\n"+"/ \\",
        2:"  o\n"+" /|\\\n"+"_/ \\",
        3:"   o\n"+"  /|\\\n"+"|_/ \\",
        4:"   o\n"+"| /|\\\n"+"|_/ \\",
        5:"|  o\n"+"| /|\\\n"+"|_/ \\",
        6:"_\n"+"|  o\n"+"| /|\\\n"+"|_/ \\",
        7:"__\n"+"|  o\n"+"| /|\\\n"+"|_/ \\",
        8:"__\n"+"|  |o <couic>\n"+"| /|\\\n"+"|_/ \\", 
        9:"\o/\n"+" |\n"+"/ \\",
        }

    
    print(dico[score])
    return None


if __name__=="__main__":
    
    lejeu("aime")
    #playerprompt()
    #pendu(9)
    
    
    
    
    
