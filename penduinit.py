# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:16:26 2021

@author: MLL
"""
import lejeudupendu as ljp


def lejeudupenduinit():
    
    # chemin=""
    # joueur=""
    # score=0
    # table={}
    # mot=""
    while True:
        
        qYno = input("Press 'Enter' to play or Type 'Q' to quit: ")
        if qYno.upper()=="Q":
            break
        
        joueur = ljp.playerprompt()
        chemin,bln = ljp.verifypath()
        table = ljp.singleplayerscore(joueur, ljp.getplayersdata(chemin,bln))
        mot = ljp.lemot()
        score = ljp.lejeu(mot)
        table = ljp.updatescore(joueur, table, score)
        ljp.wplayersdata(chemin,table)
    return None

if __name__=="__main__":
    lejeudupenduinit()
