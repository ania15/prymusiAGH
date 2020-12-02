import math

print("Witaj świecie!")

input_text = "testowy tekst"  # str, string
pi = 3.14 # float
test = 2 # int
b,c=20,30

print(math.sqrt(9))

print(type(input_text))
print(type(test))
print(input_text)
print(pi)
print(type(pi))


marks = [1.0,2.0,3.0,4.0,5.0] # list
#         0    1   2  3   4

marks[0] #pierwszy
marks[1] # drugi
marks [len(marks)-1] # ostatni, Źle]
marks[-1] # ostatni
marks[-2] # przedostatni

print(marks[0:2])
print(marks[0:-1:2])
#          [od:do:krok]
print(marks[1])


# zbior = {1, 30, 120}   dict
cities = {"Kraków": 771000, "Warszawa": 1777000, 314:"pi"}
print(cities["Kraków"]) # wypisze 771000
print(cities[314])


True
False
# str, int, float, list, dict, bool

liczba = 314 # int
print("Moja liczba to: " + str(liczba))
print(bool([]))

print(bool(0))

# new_variable
# Tracebacl (most recent call last):
# NameError: name 'new_variable' is not defined

new_variable = None
if new_variable is None:
    print("mamy pusta wartosc")