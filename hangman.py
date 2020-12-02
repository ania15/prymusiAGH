import random
import string
from words import word_list


imię = input("Jak masz na imię?")
print("Witaj",imię, ",zagrajmy w wisielca!")

hasło=random.choice(word_list)
print("Wylosowane hasło ma", len(hasło), "znaków")
litera = random.choice(string.ascii_lowercase)
odgadniete = False
wyswietlane_haslo = "_" *len(hasło)
ilosc_prob=3
poprzednie_litery=[]

while not odgadniete and ilosc_prob > 0:
    litera = input("Podaj literę:")
    if len(litera) == 1:
        if litera in poprzednie_litery:
            print("Już wcześniej podałeś literę ", litera)
        elif litera not in hasło:
            print("Litery" , litera, "nie ma w haśle")
            ilosc_prob-=1
            poprzednie_litery.append(litera)
        else:
            print("Dobrze",litera,"znajduje się w haśle")
            poprzednie_litery.append(litera)
            hasło_lista = list(wyswietlane_haslo)
            indeksy = [idx for idx, letter in enumerate(hasło) if letter == litera] #????
            print(indeksy)
            for idx in indeksy:
                hasło_lista[idx]=litera
            wyswietlane_haslo = "".join(hasło_lista)
            print(wyswietlane_haslo)
            if "_" not in wyswietlane_haslo:
                odgadniete = True
    
    else:
        print("Nieprawidłowy znak - podaj literę")
              
        if odgadniete:
            print("Gratulacje, wygrałeś, udało Ci się odgadnąć hasło!")
        else:
            print("Niestety, skończyły ci się próby. Hasło to", hasło)






