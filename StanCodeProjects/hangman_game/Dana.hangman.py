"""
File: hangman.py
Name:Dana
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This is a hangman game.
    """
    ans = random_word()
    print('The word looks like: ',end="")
    d = dashed(ans)
    print(d)
    guess(ans,d)


def guess(ans,d):
    """

    :param ans: random word
    :param d: the length of random word with dashes
    :return: the results of the game
    """
    print('You have '+str(N_TURNS)+' guesses left')
    l=N_TURNS
    while True:
        anss = ""
        if d!=ans:
            if l!=0:
                input_ch = input('Your guess: ')
                input_ch = input_ch.upper()
                if input_ch.isalpha():
                    if not len(input_ch)>1:
                        i = 0
                        while True:
                            if ans[i:].find(input_ch) > -1:
                                w = ans[i:].find(input_ch)
                                for ch in d[i:i+w]: # find more the same ch
                                    if ch=='_':
                                        anss += '_'
                                    elif ch.isalpha():
                                        anss += ch
                                anss += input_ch
                                i += w + 1
                            else:
                                for ch in d[i:len(d)]:
                                    if ch == '_':
                                        anss += '_'
                                    else:
                                        anss += ch
                                break
                        d=anss
                        if ans.find(input_ch) > -1:
                            print('You are correct!')
                            if d != ans:
                                print('The word looks like: ', end="")
                                print(d)
                                print('You have ' + str(l) + ' guesses left')

                            elif d==ans:
                                print('You win!!')
                                print('The word was ' + ans)

                        else:
                            print('There is no ' + input_ch + "'s in the word.")
                            l -= 1
                            if l != 0:
                                print('The word looks like: ', end="")
                                print(d)
                                print('You have ' + str(l) + ' guesses left')

                            elif l==0:
                                print('You are completely hung : (')
                                print('The word was ' + ans)

                    else:
                        print('illegal format.')
                else:
                    print('illegal format.')

            elif l==0:
                return True


        elif d==ans:
            return True




def dashed(ans):
    ans1=""
    for i in range(len(ans)):
        ans1+='_'
    return ans1




def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
