def seq_ping():
    print("Ok")

def valid_filename():
    exit = False
    while not exit:
        filename = input("What file do you want to open?")
        try:
            FOLDER = "./MyFiles/"
            gene = input("Choose a gene:")
            f = open(FOLDER + gene + ".txt")
            exit = True
            return f.read()
        except FileNotFoundError:
            print("File does not exist. Provide another.")


def seq_read_fasta(gene):
    full_seq = open(gene, "r").read()
    full_seq = seq[seq.find("\n")].replace("\n", "")
    return full_seq