for liczba in range(1,100):
    if liczba % 3 == 0 and liczba % 5 == 0:
        print("FizzBuzz")
    elif liczba % 5 == 0:
        print("Buzz")
    elif liczba % 3 == 0:
        print("Fizz")
    else:
        print(liczba)
