#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:58:57 2021

@author: hyewon
"""

import izhikevich_cells as izh

class CCell(izh.izhCell):
    def __init__(self, stimVal):
        """
        Has different variable values
        """
        super().__init__(stimVal)
        self.celltype = 'Chattering' 
        self.C=50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
        
    def createCell():
        """
        overrides the izh function and creates CCell instead of izhikevich cell
        """
        myCell = CCell(stimVal=200)        
        myCell.simulate()
        izh.plotMyData(myCell)
        
        
#myCell = CCell(4000)
#myCell.simulate()

if __name__=='__main__':
    CCell.createCell()