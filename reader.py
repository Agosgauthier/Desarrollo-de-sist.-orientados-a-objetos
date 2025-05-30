class Reader:
    def __init__(self, note="notes.txt"):
       self.note = note 
    
    def getAllNotes(self):
        try:
            with open(self.note, "r") as file:
                notes = file.readlines()
            return [note.strip() for note in notes]
        except FileNotFoundError:
            return []
        
#ejemplo
if __name__ == "__main__":
    reader = Reader()
    print(reader.getAllNotes())