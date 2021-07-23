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
    while 1:
        
        qYno = input("Type 'Q' to quit: ")
        if qYno.upper()=="Q":
            break
        
        joueur = ljp.playerpromt()
        chemin,bln = ljp.verifypath()
        table = ljp.getplayerdata(joueur,bln)
        table = ljp.singleplayerscore(joueur, table)
        ljp.wplayersdata(joueur,chemin)
        mot = ljp.lemot()
        score = ljp.lejeu(mot)
        table = ljp.updatescore(joueur, table, score)
        
    return None