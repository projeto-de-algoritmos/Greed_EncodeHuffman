import numpy as np
import cv2
import queue

class Node:
	def __init__(self):
		self.prob = None
		self.code = None
		self.data = None
		self.left = None
		self.right = None 	
	def __lt__(self, other):
		if (self.prob < other.prob):		
			return 1
		else:
			return 0
	def __ge__(self, other):
		if (self.prob > other.prob):
			return 1
		else:
			return 0


    
def tree(probabilities):
	prq = queue.PriorityQueue()
	for color,probability in enumerate(probabilities):
		leaf = Node()
		leaf.data = color
		leaf.prob = probability
		prq.put(leaf)

	while (prq.qsize()>1):
		newnode = Node()		
		l = prq.get()
		r = prq.get()			
		newnode.left = l 		
		newnode.right = r
		newprob = l.prob+r.prob	
		newnode.prob = newprob
		prq.put(newnode)	
	return prq.get()		

def huffman_encoding(root_node,tmp_array,f):	
	if (root_node.left is not None):
		tmp_array[huffman_encoding.count] = 1
		huffman_encoding.count+=1
		huffman_encoding(root_node.left,tmp_array,f)
		huffman_encoding.count-=1
	if (root_node.right is not None):
		tmp_array[huffman_encoding.count] = 0
		huffman_encoding.count+=1
		huffman_encoding(root_node.right,tmp_array,f)
		huffman_encoding.count-=1
	else:
		huffman_encoding.output_bits[root_node.data] = huffman_encoding.count		
		bitstream = ''.join(str(cell) for cell in tmp_array[1:huffman_encoding.count]) 
		color = str(root_node.data)
		wr_str = color+' '+ bitstream+'\n'
		f.write(wr_str)		# dicionario de codigos
	return