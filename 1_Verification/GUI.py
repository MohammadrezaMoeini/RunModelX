#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:59:20 2024

@author: mohammadrezamoeini
"""


import tkinter as tk
from tkinter import filedialog
from read_csvFile import read_csv, give_matrix_form, Coord_Disp
from PlotFunctions import plot_One




def Plot_data():
    csv_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    total = read_csv(csv_path)
    total_m = give_matrix_form(total)
    
    x, y = Coord_Disp(total_m)
    
    
    x_label = 'x'
    y_label = 'y'
    x_min = 0.0; x_max = max(x)
    y_min = -2.0; y_max = min(y)
    title_f = 'Plot data'
    leg1 = 'Test Data'
    x_legend = 0.5; y_legend = 0.3
    save = False
    save_file = None


    
    plot_One(x, y, leg1, 
             x_label, y_label,
             y_min, y_max,
             x_min, x_max,
             title_f,
             x_legend, y_legend,
             save,
             save_file)
                      
                      


def Verification():
    print("This is the verification function")
    
    
def Validation():
    print("This is the validation function")
        
                

# Create the main window
root = tk.Tk()
root.title("RunModelX v0.0.01")
root.geometry("700x700")

# Create a button to open the CSV file
open_button = tk.Button(root, text="Plot data", command=Plot_data)
open_button.place(x=10, y=10)

# Create a button for verification
open_button = tk.Button(root, text="Verification", command=Verification)
open_button.place(x=10, y=60)


# Create a button for validation
open_button = tk.Button(root, text="Validation", command=Validation)
open_button.place(x=10, y=100)



# Run the Tkinter event loop
root.mainloop()




# master=tk.Tk()
# master.title("place() method")
# master.geometry("450x350")
# button1=tk.Button(master, text="button1")
# button1.place(x=25, y=100)
# button2=tk.Button(master, text="button2")
# button2.place(x=100, y=25)
# button3=tk.Button(master, text="button3")
# button3.place(x=175, y=100)
# master.mainloop()

