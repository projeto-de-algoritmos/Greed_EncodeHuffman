import numpy as np
from screen_event import takeclick, huffmap_blue, huffmap_green, huffmap_red
import cv2
import queue
import time
from huffman import Node
from huffman import huffman_encoding, tree
import pandas as pd

#Read image
img = cv2.imread('images/ney.jpg')


scale = 80
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
new_origin = (width, height)

img = cv2.resize(img, new_origin)
shape = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blue_channel = []
green_channel = []
red_channel = []

window = 'Image'


i = 0
while(i < height):
	j = 0
	blue = []
	green = []
	red = []
	while(j < width):
		blue.append(img[i][j][0])
		green.append(img[i][j][1])
		red.append(img[i][j][2])
		j+=1
	blue_channel.append(blue)
	green_channel.append(green)
	red_channel.append(red)	
	i+=1

blue_channel = np.array(blue_channel)
green_channel = np.array(green_channel)
red_channel = np.array(red_channel)

""" #Verify Histogram specif value
cont = 0
for i in range(height):
	for j in range(width):
		if(red_channel[i][j] == 187):
			cont+=1
"""

# Blue Channel
hist = np.bincount(blue_channel.ravel(),minlength=256)
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)	
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('dict_rgb/blue.txt','w')
huffman_encoding(root_node,tmp_array,file)

# Green Channel
hist = np.bincount(green_channel.ravel(),minlength=256)
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)	
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('dict_rgb/green.txt','w')
huffman_encoding(root_node,tmp_array,file)

# Red Channel
hist = np.bincount(red_channel.ravel(),minlength=256)
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)	
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('dict_rgb/red.txt','w')
huffman_encoding(root_node,tmp_array,file)

# Neutral Channel
hist = np.bincount(red_channel.ravel(),minlength=256)
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)	
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('dict_rgb/buffer.txt','w')
huffman_encoding(root_node,tmp_array,file)


"""
#Debbug
red_map = {}
huffmap = pd.read_csv("./dict_rgb/red.txt", header = None,  sep =" ")

print(huffmap[0][0], huffmap[1][0])
red_map[int(huffmap[0][0])] =  str(huffmap[1][0])

for i in range(len(huffmap)):
	red_map[int(huffmap[0][i])] =  str(huffmap[1][i])

print(red_map[29])
#print(red_map[int(huffmap[0][0])])
"""

red_map = huffmap_red('red.txt')
blue_map = huffmap_blue('blue.txt')
green_map = huffmap_green('green.txt')

cv2.namedWindow(window)
cv2.setMouseCallback(window, takeclick)

while(True):
    cv2.imshow(window, img)
    if cv2.waitKey(20) == 27:
        break
