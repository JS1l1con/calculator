from tkinter import *
from tkinter import messagebox
class Gui:
    def __init__(self, title, x, y):
        self.root = Tk()
        self.title = title
        self.x = x
        self.y = y

        self.root.grid_rowconfigure(0, weight =1 )
        self.root.grid_columnconfigure(0, weight =1 )
        self.root.resizable(False,False)

        self.entryText = StringVar()

        self.setTitle()
        self.makeWindow()

        # Make entry
        self.makeEntry(0, 0)

        self.makeButton(".", 2, 0)
        self.makeButton("x³", 2, 1)
        self.makeButton("1/x", 2, 2)
        self.makeButton("²√x", 2, 3)

        self.makeButton("x²", 3, 0)
        self.makeButton("AC", 3, 1)
        self.makeButton("⌫", 3, 2)
        self.makeButton("/", 3, 3)

        self.makeButton("7", 4, 0)
        self.makeButton("8", 4, 1)
        self.makeButton("9", 4, 2)
        self.makeButton("*", 4, 3)

        self.makeButton("4", 5, 0)
        self.makeButton("5", 5, 1)
        self.makeButton("6", 5, 2)
        self.makeButton("-", 5, 3)

        self.makeButton("1", 6, 0)
        self.makeButton("2", 6, 1)
        self.makeButton("3", 6, 2)
        self.makeButton("+", 6, 3)

        # Numbers
        self.makeButton("0", 7, 0)
        self.makeButton("(", 7, 1)
        self.makeButton(")", 7, 2)
        self.makeButton("=", 7, 3)

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
        Button(self.root, text = key, height = 3, width = 5, command = lambda: self.pressed(key)).grid(row = row, column = column, columnspan = 1)
    
    def makeEntry(self, row, column):
        self.entry = Entry(self.root, textvariable = self.entryText, width = 50)
        self.entryText.set("")
        self.entry.bind("<Key>", self.typed)
        
        self.entry.grid(row = row, column = column, columnspan = 4)

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
        elif key == "x²":
            self.entry.insert("end", "**2")
        elif key == "²√x":
            self.entry.insert("end", "**(1/2)")
        elif key == "x³":
            self.entry.insert("end", "**3")
        elif key == "1/x":
            self.entry.insert("end", "/2")
        else:
            self.entry.insert("end", key)

    def typed(self, event):
        acceptableChars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "=", "(", ")", "."]
        currentText = self.entry.get()
        deleteKeyCode = 855638143

        if event.keycode == deleteKeyCode:
            self.entry.delete(len(self.entry.get()) - 1, END)

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
        except:
            messagebox.showerror("Error", "Syntax Error")
        else:
            self.entryText.set(self.operation)
            