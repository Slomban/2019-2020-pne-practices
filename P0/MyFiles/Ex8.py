
from Seq0 import *

FOLDER = "./sesion4/"
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

for gene in GENES:
    filename = gene + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene}: {most_frecuent_base(sequence)}")
    print()