#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:27:44 2024
@author: mohammadrezamoeini


This script inlcudes all my functions to plot the data. 
"""

import matplotlib.pyplot as plt

def plot_One(x1, y1, leg1, 
             x_label, y_label,
             y_min, y_max,
             x_min, x_max,
             title_f,
             x_legend, y_legend,
             save,
             save_file):
    
    same_font=22
    plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k') 
    plt.rc('xtick', labelsize=same_font-4) 
    plt.rc('ytick', labelsize=same_font-4)
    plt.title(title_f, fontsize=same_font+3)
    plt.xlabel(x_label, fontsize=same_font+3)
    plt.ylabel(y_label, fontsize=same_font+3)

    plt.plot(x1, y1,  'k-', markersize=7, linewidth = 2)

    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    
    plt.legend((leg1,),
               shadow = True,
               loc=(x_legend, y_legend), handlelength = 1.5,
               fontsize = same_font-5)

    if save:
        plt.savefig(save_file, format='eps')
        
    plt.show() 
    
def plot_TWO(x1, y1, leg1, 
             x2, y2, leg2,
             x_label, y_label,
             y_min, y_max,
             x_min, x_max,
             title_f,
             x_legend, y_legend,
             save,
             save_file):
    
    same_font=22
    plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k') 
    plt.rc('xtick', labelsize=same_font-4) 
    plt.rc('ytick', labelsize=same_font-4)
    plt.title(title_f, fontsize=same_font+3)
    plt.xlabel(x_label, fontsize=same_font+3)
    plt.ylabel(y_label, fontsize=same_font+3)

    plt.plot(x1, y1,  'k-o', markersize=7, linewidth = 2)
    plt.plot(x2, y2,  'b--s', markersize=7, linewidth = 2)

    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    
    plt.legend((leg1, leg2),
               shadow = True,
               loc=(x_legend, y_legend), handlelength = 1.5,
               fontsize = same_font-5)

    if save:
        plt.savefig(save_file, format='eps')
        
    plt.show() 