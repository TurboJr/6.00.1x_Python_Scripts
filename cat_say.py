# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:32:33 2017

@author: KovalevAI
"""
#Get the enter from the user
text = input('What would you like the cat to say: ')

#Determine the lenght of the input
lenght = len(text)+4

#Make the border same size as input
print('       {}'.format('-'*lenght))
print('       < {} >'.format(text))
print('       {}'.format('-'*lenght))

#Print the cat
print('      /') 
print('     /')
print(' /\_/\\')
print('( o.o )') 
print(' > ^ <')
input()
