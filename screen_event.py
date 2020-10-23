import cv2
import pandas as pd
import tkinter as tk
from tkinter import *

def screen_rgb(red, blue, green, red_map, blue_map, green_map):

        root=tk.Tk()
        text = Text(root)
        root.title('Infos')
        root.geometry("300x150")

        r_label = tk.Label(root, text = str(red) + ' : ' + str(red_map[red]) ,font=('calibre', 20, 'bold'), foreground = 'red', justify = 'left') 
        g_label = tk.Label(root, text = str(green) + ' : ' + str(red_map[green]) ,font=('calibre', 20, 'bold'), foreground = 'green', justify = 'left') 
        b_label = tk.Label(root, text = str(blue) + ' : ' + str(red_map[blue]) ,font=('calibre', 20, 'bold'), foreground = 'blue' , justify = 'left')

        r_label.grid(row=0,column=0, sticky = 'NW') 
        g_label.grid(row=1,column=0, sticky = 'NW') 
        b_label.grid(row=2,column=0, sticky = 'NW')

        root.mainloop() 



def takeclick(event, x,y, flag, params):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        from main import img, red_map, blue_map, green_map
        print(x,y)
        print(img[y][x])
        blue, green, red = img[y][x]
        print('red: %d - %s' % (red, red_map[red]))
        print('green: %d - %s' % (green, green_map[green]))
        print('blue: %d - %s' % (blue, blue_map[blue]))
        
        screen_rgb(red, blue, green, red_map, blue_map, green_map)
        

def huffmap_red(filename):
    mp = {}
    huffmap = pd.read_csv("./dict_rgb/" + filename, header = None,  sep =" ")
    
    for i in range(len(huffmap)):
    	mp[int(huffmap[0][i])] =  str(huffmap[1][i])

    return mp

def huffmap_blue(filename):
    mp = {}
    huffmap = pd.read_csv("./dict_rgb/" + filename, header = None,  sep =" ")
    
    for i in range(len(huffmap)):
    	mp[int(huffmap[0][i])] =  str(huffmap[1][i])

    return mp

def huffmap_green(filename):
    mp = {}
    huffmap = pd.read_csv("./dict_rgb/" + filename, header = None,  sep =" ")
    
    for i in range(len(huffmap)):
    	mp[int(huffmap[0][i])] =  str(huffmap[1][i])

    return mp
