"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'    # Controls when to stop the loop
dictionary = []



def main():
    """
    TODO:
    """
    print(f'welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input("Find anagrams for: ")
        start = time.time()
    ####################
        if s == EXIT:
            break
        elif s.isalpha():
            read_dictionary(s)
            print("Searching...")
        ss = []
        for i in s:
            ss.append(i)
        targets = find_anagrams(ss)

        print(f'{len(targets)} anagrams: {targets}')
    ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
        dictionary.clear()


def read_dictionary(s):
    with open(FILE, 'r') as f:
        for line in f:
            line_d = line.strip()
            if len(line_d) == len(s):
                for i in s:
                    if i in line_d:
                        dictionary.append(line_d)
                        break


def find_anagrams(ss):
    """
    :param s:
    :return:
    """
    return helper(ss, len(ss), [], '', ss.copy())


def helper(ss, l, anagram, st, ss_r):
    if len(st) == l and st in dictionary:
        if st in dictionary and st not in anagram:
            anagram.append(st)
            print(f'Found: {st}')
            print("Searching...")
    else:
        for i in range(l):
            if ss[i] == '':
                pass
            else:
                st += ss[i]
                ss[i] = ''
                helper(ss, l, anagram, st, ss_r)
                st = st[:len(st)-1]
                ss[i] = ss_r[i]

    return anagram


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    switch = False
    for x in dictionary:
        if str(x).startswith(sub_s):
            switch = True
            break
    return switch


if __name__ == '__main__':
    main()
