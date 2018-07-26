# def add(x, y):
#     assert x > 0 and y > 0, "Both most be pos"
#     return x + y

# print(add(2,10))
# print(add(2,-10))

def eat_junk(food):
    assert food in [
        "alus", 
        "pica", 
        "kebabai", 
        "saldainiai"
        ], "food must be junk food!"
    return f"NOM NOM NOM I am eating {food}"

food = input("Ka esi?")
print(eat_junk(food))