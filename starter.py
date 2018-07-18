from random import randint

random_number = randint(1, 10)

guess = None

while guess != random_number:
    guess = int(input("Issirink numeri: "))
    if guess == random_number:
        print("Teisingai")
    elif guess < random_number:
        print("Daugiau")
    else:
        print("Maziau")
