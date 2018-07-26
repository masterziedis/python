import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import uniform, choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com/"

def read_quotes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses != 0:
        guess = input(
            f"Who saif this quote? Guesses remaining: {remaining_guesses} ")
        if guess.lower() == quote["author"].lower():
            print("YES")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            response = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(
                f"Here's the hint: The author was born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Author's first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Author's first name starts with {last_initial}")
        else:
            print(f"Sorry no guess, the author is {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again? (y/n)")
    if again.lower() in ('yes', 'y'):
        print("YOU PLAY AGAIN")
        return start_game(quotes)
    else:
        print("BYE")


quotes = read_quotes("quotes.csv")
start_game(quotes)
