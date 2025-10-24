# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 11:12:22 2025

@author: PC
"""

#Matrice.py
import numpy as np
class Matrice:
     def __init__(self,A,b):  
         self.A=np.array(A,dtype=float)
         self.b=np.array(b,dtype=float)
     def affiche(self):
           print("Matrice A=\n",self.A)
           print("Matrice b=",self.b)
     def resoudre(self):
            x=np.linalg.solve(self.A,self.b)
            return x
