def seq_ping():
    print("Ok")


from pathlib import Path

def first_20_basis():
    filename = input("DNA file: ")
    try:
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[0:20]
        return body
    except FileNotFoundError:
        print(f"[Error]: file '{filename}' not found ")
    except IndexError:
        print(f"file '{filename}' is empty")