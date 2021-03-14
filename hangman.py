import random

words = ["python", "java", "kotlin", "javascript"]
word = random.choice(words)
word = list(word)  # gets swapped out for dashes
old_word = "".join(word)

num_dash = len(word)
dash = []  # gets swapped out for letters

for i in range(num_dash):
    dash.append("-")

old_dash = "".join(dash)

guesses = set()  # letters already guessed

lives = 8

repeat = "nothing"  # weather to repeat the game or not

# game
print("H A N G M A N")

while repeat != "exit":
    repeat = input('Type "play" to play the game, "exit" to quit: ')
    if repeat == "play":
        while lives > 0:
            if old_word == "".join(dash):  # if all the dashes are filled in: you win
                print("You guess the word!")
                print("You survived!")
                break
            else:  # game continues
                print("")
                print("".join(dash))
                letter = input("Input a letter: ")
                if len(letter) == 1:  # checks if letter is 1 letter
                    if letter.isalpha() and letter.islower():  # checks if letter is lowercase english
                        if word.count(letter) != 0:  # if letter is in word
                            while word.count(letter) != 0:  # while letter is in word, in case of multiples
                                index = word.index(letter)  # finds letters index
                                word.pop(index)  # gets rid of letter in word
                                word.insert(index, "-")  # replaces letter with dash in word
                                dash.pop(index)  # gets rid of dash in dash
                                dash.insert(index, letter)  # replaces dash with letter in dash
                                guesses.update(letter)  # adds letter to guessed letters
                        else:  # if the letters not in the word
                            if letter not in old_word:  # if the letter was never in the word
                                if letter in guesses:  # if the letter has already been guessed
                                    print("You've already guessed this letter")
                                else:  # if the letter has never been guessed
                                    print("That letter doesn't appear in the word")
                                    guesses.update(letter)  # adds letter to guessed letters
                                    lives -= 1
                            else:  # if the letter used to be in the word, already guessed
                                print("You've already guessed this letter")
                    else:
                        print("Please enter a lowercase English letter")
                else:
                    print("You should input a single letter")
        else:  # if you run out of lives
            print("You lost!")
