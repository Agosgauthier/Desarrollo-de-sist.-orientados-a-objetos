Class writer:
      def addNote(self, note:str):
         with open("notes.txt", "a", encoding="utf-8") as file:
            file.writer(note + "\n")


ejemplo:
if __name__ == "__main__":
    writer = Writer()
    writer.addNote("Primera nota")
    writer.addNote("Segunda nota")