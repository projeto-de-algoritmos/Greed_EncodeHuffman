import numpy as np
import cv2
import queue
from huffman import Node
from huffman import huffman_encoding, tree


#Read image
img = cv2.imread('images/op.jpg')


scale = 80
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
new_origin = (width, height)

img = cv2.resize(img, new_origin)
shape = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(type(shape))
blue_channel = []
green_channel = []
red_channel = []



cv2.imshow('teste', img)
cv2.waitKey(0)

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

#print(red_channel)
#print(blue_channel)
#print(green_channel)


""" #Verify Histogram specif value
cont = 0
for i in range(height):
	for j in range(width):
		if(red_channel[i][j] == 187):
			cont+=1
"""




# Red Channel
hist = np.bincount(red_channel.ravel(),minlength=256)
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)	
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('red.txt','w')
huffman_encoding(root_node,tmp_array,file)

# Blue Channel
hist = np.bincount(blue_channel.ravel(),minlength=256)
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)	
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('blue.txt','w')
huffman_encoding(root_node,tmp_array,file)

# Green Channel
hist = np.bincount(green_channel.ravel(),minlength=256)
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)	
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('green.txt','w')
huffman_encoding(root_node,tmp_array,file)


"""
input_bits = img.shape[0]*img.shape[1]*8	# calculate number of bits in grayscale 
compression = (1-np.sum(huffman_encoding.output_bits*hist)/input_bits)*100	# compression rate
print('Compression is ',compression,' percent')
"""
