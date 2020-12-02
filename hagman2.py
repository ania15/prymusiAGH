import random
import string

letter = random.choice(string.ascii_lowercase)
print("Random letter: ",letter)

ok = False
attempts = 0
used_characters = set()
while not ok:
    guess = input("Guess: ")
    if guess not in used_characters:
        attempts += 1
        used_characters += guess
    else:
        print("Already used:", guess, "->", used_characters)
    attempts += 1
    print("Your guess: ", guess)
    ok = (guess == letter)

print("Attempts: ", attempts)
while odkryte_litery < len(hasło):
        litera=input("Podaj literę:")
        if litera in hasło:
                print("Dobrze! Ta litera jest w haśle")
                odkryte_litery+=1
        else:
                print("Niestety tej litery nie ma w haśle")

    





   


