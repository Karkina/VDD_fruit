# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:24:34 2021

@author: Nicolas
"""
from tkinter import * 
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import numpy_indexed as npi
from functools import partial
import tkinter.font as font
from PIL import Image, ImageTk
#from IPython import get_ipython

def newFile():
    return 0
def openFile():
    return 0
def closeFile():
    return 0

def get_np_array(fruit,boolTest):
    
    date_path='data/food-price-weight.csv'
    #OUVERTURE DU DOCUMENT CSV
    with open(date_path,'r') as f:
        reader = csv.reader(f,delimiter=',')
        headers= next(reader)
        data=np.array(list(reader))
    
    #PRENDRE LES COLONNES QUI MINTERESSE
    data_fruit=np.column_stack((data[:,1],data[:,2],data[:,7]))
    #PRENDRE SEULEMENT LA COLONNE DU FRUIT
    test_orange=data_fruit[np.char.startswith(data_fruit[:,2],fruit)]
    #ANNE 
    first=np.char.ljust(test_orange[:,0],4).astype(float)
    #STRING TO FLOAT
    second=test_orange[:,1].astype(float)
    #COMBINE LES COLONNES
    final=np.column_stack((first,second))
    res=average_fruit(final)
    if boolTest: plot_fruit(final,res,fruit)
    return final
    
def average_fruit(final):
    #ON REGROUPE LES LIGNES PAR ANNEE
    groupby=npi.group_by(final[:, 0]).split(final[:,1])
    
    #SOMME DES FRUIT
    res=[sum(groupby[i]/len(groupby[i])) for i in range(0,len(groupby))]
    return res
'''FONCTION QUI AFFICHE LEVOLTION DUN FRUIT'''
def plot_fruit(final,res,fruit):
     fig,axs=plt.subplots(1)
     axs.plot(np.unique(final[:,0]),res)
     fig.suptitle(fruit)
     axs.set_xlabel("ANNEE",fontsize='15')	#adds a label in the x axis
     axs.set_ylabel("Moyenne Euros",fontsize='15')	#adds a label in the y axis
     plt.show()
     
def plot_mutliple_fruit(axs,fruit):
    #Random Color
    r = random.random()
    b = random.random()
    g = random.random()
    color_plot= (r, g, b)
    #Avoir la liste pour les années
    x=get_np_array(fruit,False)
     
    y=average_fruit(x)
    axs.plot(np.unique(x[:,0]), y, 'o-',color=color_plot,linewidth=5,markersize=12, label=fruit)
    
    plt.legend(loc="upper left", title="Legend fruit", frameon=False) 
    plt.show()
    
def button_plot_evol():
    #SOUS WINDOW
    evol_fruit=Toplevel(window)
    evol_fruit.geometry("1200x1600")
    date_path='data/food-price-weight.csv'
    #OUVERTURE DU DOCUMENT CSV
    with open(date_path,'r') as f:
        reader = csv.reader(f,delimiter=',')
        headers= next(reader)
        data=np.array(list(reader))
    #PRENDRE LES COLONNES QUI MINTERESSE
    data_fruit=np.column_stack((data[:,7]))
    #PRENDRE SEULEMENT LA COLONNE DU FRUIT
    test_fruit=(np.unique(data_fruit).astype(str))
    #CREATION LISTE BUTTONS
    button=list()
    x=0
    y=0
    #CREATION DES BUTTONS
    for i in test_fruit:
        button.append(ttk.Button(evol_fruit,text=i, command=partial(get_np_array,i,True)))
        
    for ind in range(0,test_fruit.size):
        
        #PLACEMENT BUTTON
        button[ind].place(x=x,y=y,anchor=NW)
        y+=25
        #ON LES ESPACES PAR QUARTILES
        if ind==int(test_fruit.size*0.25):
           x+=300
           y=0
        elif ind==int(test_fruit.size*0.5):
            x+=300
            y=0
        elif ind==int(test_fruit.size*0.75):
            x+=300
            y=0

def button_mult_plot_evol():
    '''WINDOW DAFFICHAGE '''
    evol_mult_fruit=Toplevel(window)
    evol_mult_fruit.geometry("1200x1600")
    
   
    
    date_path='data/food-price-weight.csv'
    #OUVERTURE DU DOCUMENT CSV
    with open(date_path,'r') as f:
        reader = csv.reader(f,delimiter=',')
        headers= next(reader)
        data=np.array(list(reader))
    #PRENDRE LES COLONNES QUI MINTERESSE
    data_fruit=np.column_stack((data[:,7]))
    #PRENDRE SEULEMENT LA COLONNE DU FRUIT
    test_fruit=(np.unique(data_fruit).astype(str))
    #CREATION LISTE BUTTONS
    button_mult=list()
    x=0
    y=0
    
    fig_mult,axs_mult=plt.subplots(1)
    fig_mult.suptitle('Multiple fruit in the same drawing', fontsize=15)
    
    #CREATION DES BUTTONS
    for i in test_fruit:
        button_mult.append(ttk.Button(evol_mult_fruit,text=i, command=partial(plot_mutliple_fruit,axs_mult,i)))
        
    for ind in range(0,test_fruit.size):
        
        #PLACEMENT BUTTON
        button_mult[ind].place(x=x,y=y,anchor=NW)
        y+=25
        #ON LES ESPACES PAR QUARTILES
        if ind==int(test_fruit.size*0.25):
           x+=300
           y=0
        elif ind==int(test_fruit.size*0.5):
            x+=300
            y=0
        elif ind==int(test_fruit.size*0.75):
            x+=300
            y=0
#test_fruit=(np.char.ljust(np.unique(data_fruit).astype(str),10))[0:50]
#get_ipython().run_line_magic('matplotlib', 'qt')
#get_ipython().run_line_magic('matplotlib', 'qt') 
date_path='data/food-price-weight.csv'
    #OUVERTURE DU DOCUMENT CSV
with open(date_path,'r') as f:
    reader = csv.reader(f,delimiter=',')
    headers= next(reader)
    data=np.array(list(reader))
#PRENDRE LES COLONNES QUI MINTERESSE
data_fruit=np.column_stack((data[:,7]))
#PRENDRE SEULEMENT LA COLONNE DU FRUIT
test_fruit=(np.unique(data_fruit).astype(str))
#test_fruit=(np.char.ljust(np.unique(data_fruit).astype(str),10))[0:50]
#get_ipython().run_line_magic('matplotlib', 'qt')

#WINDOW BUTTON
window = Tk()
#TAILLE DE LA WINDOW
window.geometry("1200x1600")
window.title("FOOD IN NEW ZELAND")

load = Image.open("photo/food_newZe.jpg")
render = ImageTk.PhotoImage(load)

background = Label(window, image=render)
background.place(relx=0.5, rely=0.85,anchor=CENTER)
          
window.config(bg='slate blue')

'''#WINDOW CONTAINER
mainframe =ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
'''


createur=Label(window,text="KarkinaFrost")

button_font=font.Font(size=13)

title=Label(window,text="La Nourriture en Nouvelle Zélande",width=250,height=5,bg='green')
title.config(font=("Courier", 19))
title.place(relx=0.5,rely=0.1,anchor=CENTER)
#BUTTON MAIN WINDOw
a=Button(window,text="L'evolution des fruits ",height=5,width=100,command=button_plot_evol,bg='dark orange')
a.place(relx=0.5,rely=0.65,anchor=CENTER)
a['font']=button_font

b=Button(window,text="Comparaison de fruit",height=5,width=100,command=button_mult_plot_evol,bg='dodger blue')
b.place(relx=0.5,rely=0.35,anchor=CENTER)
b['font']=button_font

'''
canvas = Canvas(window, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="photo/food_newZe.jpg")      
canvas.create_image(20,20, anchor=NW, image=img)'''





   
window.option_add('*tearOff', FALSE)
window.tk.call('tk', 'windowingsystem')   
#win = Toplevel(window)

menubar = Menu(window)
window['menu'] = menubar
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
#menu_file = Menu(menu_file.add_command(label='New', command=newFile))
menu_file.add_command(label='Open...', command=openFile)
menu_file.add_command(label='Close', command=closeFile)





'''T = Text(window, height=10, width=30)
T.pack(side='top')
T.insert(END, "Just a text Widget\nin two lines\n")'''


window.mainloop()