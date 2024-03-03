#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:42:22 2024

@author: mohammadrezamoeini


This script includes the funciton to read a given csv file. 
"""
import pandas as pd 
import numpy as np


# =============================================================================
# Read csv file
# =============================================================================
def read_csv(csv_path):
    """
    Return a list including all data int he given csv file.
    
    input:
        csv_path: The path of the csv file
        (ex.: give_total(r'Folder\results.csv'))
        
    output:
        total: a list including all data
        
    """
    df = pd.read_csv(csv_path) 
    
    header_temp = df.head(0)
    header=[]
    for h in header_temp:
        header.append(h)
        
    total=[]
    for h_temp in range(len(header)):   
        a = df[header[h_temp]][:]
        b=[]
        b.append(0.0) # adding to the force/time/displcement 
        # vector at the initial
        
        #b.append(h_temp) adding the first component of the list
        # This works well when you don't have a string header
        for i in a:
            b.append(i)
                
        total.append(b)
    
    return total



def give_matrix_form(total):
    """returns matrix form of list Total"""
    m = np.array(total)
    mm = m.transpose()
    return mm


def Coord_Disp(total):
    """
    Return values x and y in a list resulted from the csv file
    input:
        Total: list generated from abaqus in a csv file.
    output:
        data (x, y) 
    """
    
    Total = give_matrix_form(total)
    
    x = np.array([])
    y = np.array([])
    
        
    for i in range(len(Total)):            
        x = np.append(x, Total[i, 0])
        y = np.append(y, Total[i, 1])
    
    return x, y
