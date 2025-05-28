from writer import Writer
from reader import Reader

def main():
    writer = Writer()
    writer.addNote("Nueva nota desde el programa principal")
    
    reader = Reader()
    notas = reader.getAllNotes()
    
    print("📌 Notas guardadas:")
    for nota in notas:
        print(f"- {nota}")

if __name__ == "__main__":
    main()