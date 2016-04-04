import random, os
import time

# Python 3
# The game selects a random sentence and censors one word for the user to
# guess. If the guess matches the censored word, then one point is added to the
# score.

def build_data(idioms_file):
    idioms = open(idioms_file).read().splitlines()
    data = []
    for line in idioms:
        for word in line.split():
        # If there's more than two words and the length of a word is > 3
            if len(line.split()) > 2 and len(word) > 3 and line not in data:
                data.append(line)
    data = sorted(data)
    idioms = data
    return idioms

def game_type():
    while True:
        choice = input('Easy or hard version? ').lower()
        if choice == 'easy':
            idioms_file = 'idioms.txt'
            return idioms_file
        elif choice == 'hard':
            idioms_file = 'full_idioms.txt'
            return idioms_file
        else:
            print('I don\'t know what that means.')


def restart(attempts, idioms):
    while True:
        choice = input('\nPlay again: Y or N? ').lower()
        if choice[0] == 'y':
            game(attempts, idioms)
        elif choice[0] == 'n':
            os._exit(1)
        else:
            print ("I don't know what that means.")
            

def censor(word):
    return '_' * len(word)

def joiner(sentence):
    words = sentence.split()
    answer = ''
    while len(answer) < 4:
        answer = random.choice(words).strip(' ,.!?')
    answer_idx = words.index(answer)
    words[answer_idx] = censor(answer)
    result = ' '.join(words)
    return (result, answer.lower())

def game(attempts, idioms):
    wins = 0
    for i in range(attempts):
        sentence = random.choice(idioms)
        idioms.remove(sentence)
        result, answer = joiner(sentence)
        print ('\n' + result )
        turns = 0
        while turns < 3:
            guess = input('\n> ').lower()
            turns += 1
            if guess == answer:
                print ('Correct!')
                wins += 1
                break
            else:
                print ('Incorrect')
                if turns == 3:
                    print ('\nThe answer was', answer)
    print ('Your score: %i/%i' % (wins, attempts))

    restart(attempts, idioms)

def start():
    choice = game_type()
    idioms = build_data(choice)
    while True:
        try:
            attempts = int(input('\nHow many questions would you like? '))
        except Exception:
            print ('That is not a valid number.')
            continue
        break
    print ('\nYou have 3 tries to guess the word in the blank for these',
           'common expressions. \nGood luck!')
    time.sleep(2)
    game(attempts, idioms)

start()
