def divide(a, b):
    try:
        return a/b
    except (ZeroDivisionError, TypeError) as err:
        print("kazka cia pridirbai")
        print(err)

print(divide(1, 0))
