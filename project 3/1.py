import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split()
word = random.choice(someWords)

if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of a fruit')

    display_word = ['_' for _ in word]  # List to display the word

    playing = True
    letterGuessed = []
    chances = len(word) + 2
    correct = 0

    try:
        while chances > 0:
            print(' '.join(display_word))
            print()

            guess = input('Enter a letter to guess: ').lower()

            if len(guess) != 1 or not guess.isalpha():
                print('Enter only a SINGLE letter')
                continue

            if guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            if guess in word:
                letterGuessed.append(guess)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    display_word[index] = guess
                correct += len(indices)
                if correct == len(word):
                    print(' '.join(display_word))
                    print('Congratulations, You won!')
                    break
            else:
                chances -= 1
                print('Oops! That letter is not in the word. Chances left:', chances)

            if chances == 0:
                print('You lost! The word was:', word)
                break

    except KeyboardInterrupt:
        print('\nBye! Try again.')

