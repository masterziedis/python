class Grumpy(dict):
    def __repr__(self):
            print("NE TAVO REIKALAS")
            return super().__repr__()
    def __missing__(self, key):
        print(f"NORI {key}? NEGAUSI")
    
    def __setitem__(self, key, value):
            print("NORI KEIST?")
            print("NU PK")
            super().__setitem__(key, value)

data = Grumpy({"first": "radzi", "second": "alus"})
print(data)
data["city"] = "Tokyo"
print(data)
