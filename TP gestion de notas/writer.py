class writer:
     def __init__(self, note="notes.txt"):
        self.notes= note

     def addNote(self, note: str):
         with open("notes.txt", "a") as file:
            file.writer(note + "\n")


#ejemplo de uso
if __name__ == "__main__":
    writer = writer()
    writer.addNote("Primera nota")
    writer.addNote("Segunda nota")