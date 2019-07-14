# import of the random library
import random

# definicion of functons
# generating of random number


def nahodne_cislo():
    """This function defines random number"""
    i = 0
    cisla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nahodne_cislo = []

    while i <= 3:
        cislo = cisla.pop(random.randint(0, len(cisla) - 1))
        nahodne_cislo.append(cislo)
        i += 1

    return nahodne_cislo

# Input from the player


def vstup(text_zadani, text_chyba):
    """This function takes the input from player"""
    pokracovat = True

    while pokracovat:
        vstupni_cisla = list(input(text_zadani))
        if len(vstupni_cisla) != 4:
            print(text_chyba)
            pokracovat = True
        else:
            return vstupni_cisla
            pokracovat = False

# definiton of main function


def main():
    """This function defines main function"""

    # Introduction of game
    print(""" Hi there!
 I've generated a random 4 digit number for you.
 Let's play a bulls and cows game.
 Enter a number""")

    # Generating of random number
    nahodne = nahodne_cislo()
    pokracovat = True
    pocet_cyklu = 1

    # starting of the cycle
    while pokracovat:
        i = 0
        bulls = 0
        cows = 0

        # Entering of the input and checking of the lenght
        vstupni_cislo = vstup(" >>>", "Spatne zadano")

        # checking of the input, counting of bulls and cows
        while i <= 3:
            if int(vstupni_cislo[i]) == nahodne[i]:
                bulls += 1
            elif int(vstupni_cislo[i]) in nahodne:
                cows += 1
            i += 1

        # bulls = 4, printing of final sentence with number of cycles
        if bulls == 4:
            print("Correct, you've guessed the right number in " +
                str(pocet_cyklu) + " guesses")
            pokracovat = False
        # printing of number of bulls and cows and going back
        # to the beginning of cycle
        else:
            pokracovat = True
            print(str(bulls) + "bulls", str(cows) + "cows")
            pocet_cyklu += 1

# main funktion
main()
