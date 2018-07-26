from csv import reader
with open("titanic.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(f"{row[0]} is from {row[2]}")