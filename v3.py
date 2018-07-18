from random import randint

# print("Rock")
# print("Paper")
# print("Scissors")
#
# player1 = input("Player1, make your move ")

rand_num = randint(0, 2)

if rand_num == 0:
    computer = "sulinys"
elif rand_num == 1:
    computer = "popierius"
else:
    computer = "zirkles"

print(f"Computer plays {computer}")


# if player1 == player2:
#     print("tie!")
# elif player1 == "rock":
#     if player2 == "scissors":
#         print("player1 wins")
#     elif player2 == "paper":
#         print("player2 wins")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("player1 wins")
#     elif player2 == "scissors":
#         print("player2 wins")
# elif player1 == "scissors":
#         if player2 == "paper":
#             print("player1 wins")
#         elif player2 == "rock":
#             print("player2 wins")
# else:
#     print("something wrong")
