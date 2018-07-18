def colorize(text, color):
    colors = ("red", "yellow", "blue", "green", "magenta", "black")
    if type(text) is not str:
        raise TypeError("text and color must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

colorize("hello", "red")
colorize("hello", "red")
