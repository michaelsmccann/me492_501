#hw3p3_piglatin.py
#Michael McCann

from matplotlib.pyplot import *
from numpy import *

word = raw_input('Please enter a single word:')

print('The word to be converted to Pig Latin is '+str(word)+'.')

try:
	if word[0] in 'aeiou':
		print(word+'hay')
	else:
		print(word[1:]+word[0]+'ay')
except KeyboardInterrupt:
	print('closed')
