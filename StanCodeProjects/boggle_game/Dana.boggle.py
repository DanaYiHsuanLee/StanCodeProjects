"""
File: boggle.py
Name: Dana
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	The game of boggle to find all the words.
	"""
	start = time.time()
	####################
	d = {}
	for i in range(4):
		l = input(f'{i+1} row of letters: ')
		l = l.split(' ')
		if ' ' in l or len(l) != 4:
			print('Illegal input ')
			exit()
		ll = []
		for j in l:
			if j.isalpha():
				ll.append(j.lower())
		d[i] = ll   # {1:[ll]}
	l = find_vocabulary(d)
	print(f'There are {l} words in total.')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_vocabulary(d):
	"""
	:param d: dict, i:[ll]
	:return: int, amount of words found in dictionary
	"""
	a = []  # list, words can be found in dictionary
	s = ''
	for xx in range(1, 3):
		for yy in range(1, 3):
			con = helper(d, a, s, xx, yy)
	return len(con)


def helper(d, a, s, xx, yy):
	for y in range(yy - 1, yy + 2, 1):
		for x in range(xx-1, xx+2, 1):
			if len(s) >= 4 and s in read_dictionary() and s not in a:
				a.append(s)
				print(f'Found: "{s}"')
			elif 3 >= x >= 0 and 3 >= y >= 0 and d[y][x] is not '':
				s += d[y][x]
				if has_prefix(s):
					b = d[y][x]
					d[y][x] = ''
					helper(d, a, s, x, y)
					s = s[:len(s) - 1]
					d[y][x] = b
				else:
					s = s[:len(s) - 1]
	return a


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	with open(FILE, 'r') as f:
		for line in f:
			line_d = line.strip()
			if len(line_d) >= 4:
				dictionary.append(line_d)
	return dictionary


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	switch = False
	for dic in read_dictionary():
		if dic.startswith(sub_s):
			switch = True
			break
	return switch


if __name__ == '__main__':
	main()
