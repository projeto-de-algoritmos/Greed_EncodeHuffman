import numpy as np
import cv2
import queue
from huffman import Node
from huffman import huffman_encoding, tree


# Read image into a numpy array
img = cv2.imread('op.jpg')

shape = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scale = 80
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)

#print(shape)

new_origin = (width, height)
blue_channel = shape
green_channel = shape
red_channel = shape


img = cv2.resize(img, new_origin)		# resize to 10% (not strictly necessary - done for faster computation)
blue_channel, red_channel, 

cv2.imshow('teste', img)
cv2.waitKey(0)

#print(width, height)
#[height][width] R:80 G:49 B:44
#print(img[0][0])

i = 0
while(i < height):
	j = 0
	while(j < width):
		#print(img[i][j][0], end = ' ')
		blue_channel[i][j] = img[i][j][0]
		green_channel[i][j] = img[i][j][1]
		red_channel[i][j] = img[i][j][2]
		j+=1
	i+=1
	#print()


cont = 0

""" #Verify Histogram specif value
for i in range(height):
	for j in range(width):
		if(red_channel[i][j] == 187):
			cont+=1
"""

#print(red_channel[0][0])

hist = np.bincount(red_channel.ravel(),minlength=256)
#print(hist[187], cont, sep = ' - ')
probabilities = hist/np.sum(hist)		# a priori probabilities from frequencies
root_node = tree(probabilities)			# create the tree using the probs.
tmp_array = np.ones([128],dtype=int)
huffman_encoding.output_bits = np.empty(256,dtype=int) 
huffman_encoding.count = 0

file = open('red.txt','w')
huffman_encoding(root_node,tmp_array,file)		# traverse the tree and write the codes

#input_bits = img.shape[0]*img.shape[1]*8	# calculate number of bits in grayscale 
#compression = (1-np.sum(huffman_encoding.output_bits*hist)/input_bits)*100	# compression rate
#print('Compression is ',compression,' percent')

