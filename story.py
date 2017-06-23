# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:02:51 2017

@author: KovalevAI
"""

def get_word(word_type):
    """ Get a word from a user and return that word."""
    if word_type.lower() == 'adjective':
        a_or_an = 'an'
    else:
        a_or_an = 'a'
    return input(' Enter a word that is {0} {1}: '.format(a_or_an, word_type)) 

def fill_in_the_blanks(noun,verb,adjective): 
	""" Fills in the blanks and returns a completed story.""" 
	story = "In this book you will learn how to {1}. It's so easy even a {0} can do it. Trust me, it will be very {2}.".format(noun,verb,adjective) 
	return story 

def display_story(story):
    """ Displays a story."""
    print()
    print(' Here is the story you created. Enjoy!')
    print() 
    print(story) 

def create_story():
    """ Creates a story by capturing the input and displaying a finished story."""
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')
    
    the_story = fill_in_the_blanks(noun,verb,adjective)
    display_story(the_story) 

create_story()
