import random
# choose random word in word list
easy_list = ['cat','dog','fish','sun','book','star','tree','milk','rain', 'jump']
medium_list = ['puzzle','garden','sailor','monkey','planet','yellow','castle','window','pencil', 'button']
hard_list = ['astronomy', 'excursion','submarine','dandelion','labyrinth','cathedral','quarantine','equilibrium','phenomenon', 'conundrum']

current_word = []

def game(guess,guessing_word, current_word, guessed_letters, count):
    idx_list = []
    guessing_bool = False
    # guessing the word
    if guess not in guessed_letters: # check what did you do before
        for num in range(len(guessing_word)):
            if guessing_word[num].lower() == guess.lower():
                idx_list.append(num)
                guessing_bool = True

        guessed_letters.append(guess)

        #changing the current word
        if guessing_bool: # if it is True
            for idx in idx_list:
                current_word[idx] = guess
            print(f"Good job! \'{guess}\' is in the word.")
        else: # False
            print(f"Sorry, \'{guess}\' is not in the word.")
            count -= 1
        idx_list.clear()
    else :
        print('you already did it.')
    return count # updated count


# shows the current status
def game_loop(guessing_word, count):
    # init
    count = count
    for _ in range(len(guessing_word)):
        current_word.append('_')
    guessed_letters = []
    
    while True:
        print('Current word:', ' '.join(current_word))
        print('Guessed letters:', ', '.join(guessed_letters))
        print('Incorrect guesses remaining:', count)
        
        try: 
            guess = input('Guess a letter:')
            if not guess.isalpha() or len(guess) > 1:
                print('Only letter are allowed.')
            else: 
                count = game(guess, guessing_word, current_word, guessed_letters, count)
        except ValueError:
            print('This application offer only English letter.')
        
        if not '_' in current_word:
            print('Congratulations! You guessed the word:', guessing_word)
            break
        if count <= 0:
            print('Game over! The word was:', guessing_word)
            break


def main():
    while True:
        # choose the level of the game
        level = input("Hi, you can choose hangman level(1. easy, 2. medium, 3. hard or randomly) : ").lower()
        if level in ['1', 'easy']:
            guessing_word = random.choice(easy_list)
            count = len(guessing_word)
            break
        elif level in ['2', 'medium']:
            guessing_word = random.choice(medium_list)
            count = len(guessing_word)
            break
        elif level in ['3', 'hard']:
            guessing_word = random.choice(hard_list)
            count = len(guessing_word)
            break
        elif level == 'randomly':
            random_game = random.choice([easy_list, medium_list, hard_list])
            guessing_word = random.choice(random_game)
            count = len(guessing_word)
            break
        else:
            print('you can choose only one level or put number')
    # set the number of incorrect guesses allowed
    count_cho = input('you can choose the the number of incorrect guesses allowed (if you want, put the number or no) : ')
    # if user wants to set regular number
    if count_cho == 'no' or count_cho.lower() == 'no':
        print('set the regular chance number', count)
    # set user's own number of incorrect
    else:
        try :
            count_cho = int(count_cho)
            if count_cho > 0:
                # if count_cho == 0 it will be regular number of count
                count = count_cho
                print('set the chance number which you can guess :', count)
        except ValueError:
            print('you can put the number or no')
    # start
    game_loop(guessing_word, count)

main()