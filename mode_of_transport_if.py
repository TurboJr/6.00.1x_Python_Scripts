# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:58:24 2017

@author: KovalevAI
"""
#Ask for the distance.
dist = input('How far would you like to travel in miles: ')

#Convert the distance to an integer.
dist = int(dist)

#Determine what mode of transport to use.
if dist < 3:
    mode_of_transport = 'walking'
elif dist < 300:
    mode_of_transport = 'driving'
else: 
    mode_of_transport = 'flying'
    
#Display the result.  
print('I suggest {} to your distanation'.format(mode_of_transport))    