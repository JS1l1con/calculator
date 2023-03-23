from tkinter import *
from tkinter import messagebox
class GUI:
    def __init__(self, title, x, y):
        self.root = Tk()
        self.title = title
        self.x = x
        self.y = y

        self.setTitle()
        self.makeWindow()

    def setTitle(self):
        self.root.title(self.title)
    
    def startApp(self):
        self.root.mainloop()

    def makeWindow(self):
        self.root.geometry(f"{self.x}x{self.y}")
        self.root.eval("tk::PlaceWindow . center")

    def makeButton(self, key, row, column):
        Button(self.root, text = key, height = 3, width = 5, command = lambda: self.pressed(key)).grid(row = row, column = column)
    
    def makeEntry(self, row, column):
        self.entry = Entry(self.root)
        self.entry.grid(row = row, column = column)

    def pressed(self, key):
        if key == "=":
            try:
                self.operation = eval(self.entry.get())
                print(self.operation)
            except:
                messagebox.showerror("Error", "Syntax Error")
        elif key == "AC":
            self.entry.delete(0, END)
        elif key == "⌫":
            self.entry.delete(self.entry.index("end") - 1)
        else:
            self.entry.insert("end", key)