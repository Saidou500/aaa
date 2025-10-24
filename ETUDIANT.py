# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 09:53:35 2025

@author: PC
"""

#Etudiant.py
import numpy as np
class Etudiant:
    def __init__(self,matricule,nom,prenom,nbrNotes):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.nbrNote=nbrNotes
        self.tabNotes=[]
    def get_matricule(self):
        return self.matricule
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_nbrNotes(self):
        return self.nbrNotes
    def get_tabNotes(self):
        return self.tabNotes
    def set_matricule(self,matricule):
        self.matricule=matricule
    def set_nom(self,nom):
        self.nom=nom
    def set_prenom(self,prenom):
        self.prenom=prenom
    def set_nbrNotes(self,nbrNotes):
        self.nbrNotes=nbrNotes
    def saisie(self):
        for i in range(self.nbrNotes):
             note=float(input(f"entrez la note {i+1}:"))
        self.tabNotes.append.note()
    def saisie(self):                     
        print(f"matricule:{self.matricule},nom:{self.nom},Prenom:{self.Prenom}")
        print(f"Notes:{self.tabNotes}")
        print(f"Moyenne:{self.moyenne()}")
        print(f"Admis:{'oui' if self.admis() else 'Ajourne'}")
    def moyenne(self):
        return sum(self.tabNotes)/ len(self.tabNotes)
    def admis(self):
        return (sum(self.tabNotes)/ len(self.tabNotes)) >=10     
            
        