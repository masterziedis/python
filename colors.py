def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s megsta gerti {color}")

fav_colors(radzi='alus', vaidutis='irgi alaus')
