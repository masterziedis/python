from random import randint

random_number = randint(1, 10)

guess = None

while True:
    guess = int(input("Issirink numeri: "))
    if guess < random_number:
        print("Daugiau")
    elif guess > random_number:
        print("Maziau")
    else:
        print("Teisingai")
        play_again = input("Dar? (y/n)")
        if play_again == "y":
            random_number = randint(1, 10)
            guess = None
        else:
            print("GGWP")
            break
