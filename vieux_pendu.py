#coding:utf-8
from random import randrange
import os ,time
from fonction import *

word_list=get_words("mots.txt")

chosen_word=generate_random_word(word_list)

play_game()
