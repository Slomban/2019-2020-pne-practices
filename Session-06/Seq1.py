class Seq:
    #a class for representing sequences
    def __init__(self):
        print("New sequence created!")
    def __str__(self):
        return self.bases
    def len(self):
        return len(self.bases)

class Gen(Seq):
    def __init__(self, bases, name =""):
        super().__init__(bases)
        self.name = name
        print("New gene created!")

s = Seq("AGTACACTGGT")
g = Gene("CGTAAC")
print("Testing...")

print(f"Sequence 1: {s}")
print(f"    Lenght: {s.len()}")
print(f"Sequence 2: {g}")
print(f"    Lenght: {g.len()}")