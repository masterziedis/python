import requests
from random import choice
user_input = input("Ko nori ieskot? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term": user_input}
).json()

num_jokes = res['total_jokes']
results = res['results']
if num_jokes > 1:
    print(f"Is viso {num_jokes} prikis apie {user_input}")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"Is viso vienas prikis apie {user_input}")
    print(results[0]['joke'])
else:
    print(f"Nera prikiu apie {user_input}")
