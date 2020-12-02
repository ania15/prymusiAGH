import random
import string


def wybierz_hasło(hasła = ["kwiatki", "ptaszki", "cukierki", "bajki", "drzewka"]):
        hasło = random.choice(hasła)
        print("Wylosowane hasło ma", len(hasło), "znaków")

def graj(hasło):
        uzupełnianie_hasła = "_" *len(hasło)
        odgadniete = False
        odgadniete_litery = []
        ilosc_prob = 3
        imię = input("Jak masz na imię?")
        print("Witaj",imię, ",zagrajmy w wisielca!")
        print(uzupełnianie_hasła)
        while not odgadniete and ilosc_prob > 0:
                litera = input("Proszę podaj literę:")
                if len(litera) == 1:
                        if litera in odgadniete_litery:
                                print("Już podałeś tę literę ", litera)
                        elif litera not in hasło:
                                print(litera, "nie ma w haśle")
                                tries-=1
                                odgadniete_litery.append(litera)
                        else:
                                print("Dobrze,", litera, "znajduje się w haśle."
                                odgadniete_litery.append(litera)
                                hasło_lista = list(uzupełnianie_hasła)
                                indeksy = [i for i, letter in enumerate(hasło) if letter == guess]
                                for index in indeksy:
                                        hasło_lista = hasło
                                uzupełnianie_hasła = "".join(hasło_lista)
                                if "_" not in uzupełnianie_hasła:
                                        odgadniete = True
                else:
                    print("Nieprawidłowy strzał")
              
        if odgadniete:
            print("Gratulacje, wygrałeś, udało Ci się odgadnąć hasło!")
        else:
            print("Niestety, skończyły ci się próby. Hasło to", hasło)

def main():
    hasło = wybierz_hasło()
    graj(hasło)
    while input("Gramy jeszcze raz? (T/N)") == "T""
        hasło = wybierz_hasło
        graj(hasło)

if __name__ == "__main__":
        main()
                


