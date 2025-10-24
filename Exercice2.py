# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 21:08:51 2025

@author: PC
"""

#matrice py
import numpy as np
class matrice:
    def matrice(self,A,b):
     self._A=np.array(A,dtype=float)
     self._b=np.array(b,dtype=float)
     def affiche(self):
         print("Matrice A=\n",self.A)
         print("Matrice B=",self.b)
     def resoudre(self):
         return np.linalg.solve(self.A,self.b)
     