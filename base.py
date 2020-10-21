import numpy as np
import cv2
import queue
from huffman import Node
from huffman import huffman_encoding, tree


#Read image
img = cv2.imread('images/op.jpg')

shape = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scale = 80
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)

new_origin = (width, height)
blue_channel = shape
green_channel = shape
red_channel = shape


img = cv2.resize(img, new_origin)		
blue_channel, red_channel, 

cv2.imshow('teste', img)
cv2.waitKey(0)

i = 0
while(i < height):
	j = 0
	while(j < width):
		blue_channel[i][j] = img[i][j][0]
		green_channel[i][j] = img[i][j][1]
		red_channel[i][j] = img[i][j][2]
		j+=1
	i+=1


cont = 0

""" #Verify Histogram specif value
for i in range(height):
	for j in range(width):
		if(red_channel[i][j] == 187):
			cont+=1
"""


hist = np.bincount(red_channel.ravel(),minlength=256)
#print(hist[187], cont, sep = ' - ')
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)	
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('red.txt','w')
huffman_encoding(root_node,tmp_array,file)

