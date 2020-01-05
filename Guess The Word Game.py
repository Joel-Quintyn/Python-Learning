import random

# import time

easy_words = ['pizza', 'fairy', 'teeth', 'shirt',
              'otter', 'plane']

normal_words = ['envelope'
                ]

hard_words = ['mississippi', 'photosynthesis',
              'mitochondria']

secret_word = str

lives = int
heart_symbol = u'\u2764'

while True:
    difficulty = int(input('Choose Difficulty (Input 1, 2 or 3):\n '
                           '1 - Easy: 6 Lives, Easier Words\n '
                           '2 - Normal: 8 Lives, Moderately Difficult Words\n '
                           '3 - Hard: 10 Lives, More Difficult Words\n\n> '))

    if difficulty == 1:
        secret_word = random.choice(easy_words).lower()
        lives = 6
        break
    elif difficulty == 2:
        secret_word = random.choice(normal_words).lower()
        lives = 8
        break
    elif difficulty == 3:
        secret_word = random.choice(hard_words).lower()
        lives = 10
        break
    else:
        print('Not An Option, Try Again')
        continue

unknown_letters = len(secret_word)

clue = list()
for letter in secret_word:
    clue.append('?')

guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    for i, letter in enumerate(secret_word):
        if guessed_letter == letter:
            clue[i] = guessed_letter
            unknown_letters -= 1
    return unknown_letters


while lives > 0:
    print('\n\n\n\n\nLives left: ' + heart_symbol * lives)
    print(clue)
    guess = input('Guess a letter or the whole word: ').lower()

    if guess == secret_word:
        guessed_word_correctly = True
        break
    elif guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
        continue
    elif unknown_letters == 0:
        guessed_word_correctly = True
        break
    else:
        print('Incorrect. You Lose A Life')
        lives = lives - 1

if guessed_word_correctly:
    print('You Won! The Secret Word Was: ' + secret_word.capitalize())
else:
    print('You Lost! The Secret Word Was: ' + secret_word.capitalize())

# end = input("\nWould You Like The Play Again? Yes or No?\n> ").lower()
# if 'y' in end:
#     print(f"Alright Let's Go...")
#     time.sleep(1)
#     print("{}".format('\n' * 5))
#     continue
# elif 'n' in end:
#     print("{}Thank You For Playing!!!".format('\n' * 5))
#     break
