class Reader:
    def getAllNotes(self):
        try:
            with open("notes.txt", "r", encoding="utf-8") as file:
                notes = file.readlines()
            return [note.strip() for note in notes]
        except FileNotFoundError:
            return []
        

ejemplo:
if __name__ == "__main__":
    reader = Reader()
    print(reader.getAllNotes())