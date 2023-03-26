from tkinter import *
from tkinter import messagebox
class Gui:
    def __init__(self, title, x, y):
        self.root = Tk()
        self.title = title
        self.x = x
        self.y = y

        self.entryText = StringVar()

        self.setTitle()
        self.makeWindow()

        # Make entry
        self.makeEntry(0, 5)

        # Numbers
        self.makeButton("1", 6, 0)
        self.makeButton("2", 6, 1)
        self.makeButton("3", 6, 2)
        self.makeButton("4", 5, 0)
        self.makeButton("5", 5, 1)
        self.makeButton("6", 5, 2)
        self.makeButton("7", 4, 0)
        self.makeButton("8", 4, 1)
        self.makeButton("9", 4, 2)
        self.makeButton("0", 7, 0)

        # Operations
        self.makeButton("AC", 2, 2)
        self.makeButton("⌫", 2, 3)
        self.makeButton("/", 3, 3)
        self.makeButton("*", 4, 3)
        self.makeButton("-", 5, 3)
        self.makeButton("+", 6, 3)
        self.makeButton("=", 7, 3)
        self.makeButton("(", 7, 1)
        self.makeButton(")", 7, 2)

    def setTitle(self):
        self.root.title(self.title)

    def makeWindow(self):
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # Calculate X and Y center
        centerX = int((screenWidth/2) - (self.x/2))
        centerY = int((screenHeight/2) - (self.y/2))

        self.root.geometry(f"{self.x}x{self.y}+{centerX}+{centerY}")

    def makeButton(self, key, row, column):
        Button(self.root, text = key, height = 3, width = 5, command = lambda: self.pressed(key)).grid(row = row, column = column)
    
    def makeEntry(self, row, column):
        self.entry = Entry(self.root, textvariable = self.entryText)
        self.entryText.set("") # nově přidáno
        self.entry.bind("<Key>", self.typed)
        
        self.entry.grid(row = row, column = column)

    def makeLabel(self, text, row, column):
        self.label = Label(self.root,text = text)
        self.label.grid(row = row, column = column)

    def pressed(self, key):
        if key == "=":
            self.calculate()
        elif key == "AC":
            self.entry.delete(0, END)
        elif key == "⌫":
            self.entry.delete(self.entry.index("end") - 1)
        else:
            self.entry.insert("end", key)

    def typed(self, event):
        acceptableChars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "=", "(", ")"]
        currentText = self.entry.get()

        # If current text == entry text - can not delete numbers
        if currentText == self.entryText.get() and event.char not in acceptableChars:
            # Dont add character to entry
            return "break"
        self.entryText.set(currentText)

        # If user added not acceptable characters
        if event.char not in acceptableChars:
            # Delete the character
            self.entry.delete(len(currentText) - 1, END)
            # Dont add character to entry
            return "break"
        
        if event.char == "=":
            # Calculate
            self.calculate()
            # Dont add = to entry
            return "break"
        
    def calculate(self):
        try:
            self.operation = eval(self.entry.get())
            self.makeLabel(self.operation, 10, 10)
        except:
            messagebox.showerror("Error", "Syntax Error")