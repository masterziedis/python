from csv import DictReader, DictWriter

def cm_to_in(cm):
    return round(float(cm) * 0.393701, 2)

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_fighters", "w") as file:
    headers = ("Character", "Move", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Character": f["Character"],
            "Move": f["Move"],
            "Height": cm_to_in(f["Height"])
        })
