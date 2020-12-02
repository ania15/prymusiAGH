marks = [1.0,2.0,3.0,4.0,5.0]
# for (i=0; len(marks); i++)
for value in marks:
    #value
    print(value)


for index, value in enumerate(marks):
    print("index = ", index, "value = ", value)
    break
else:
    print("koniec")

for i in range(10+1):
    print(i)

print("x" not in "ala ma kota")

x=input("Podaj wartość:")
print("podana wartość= ", x)

import random

foo = [ 'ala', 'beata', 'c', 'd', 'e']

selected_word = random.choice(foo)
print("wylosowano: ", selected_word)

while(warunek):
    pass