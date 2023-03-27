# Imports
from tkinter import *
from tkinter import messagebox

class Gui:
    def __init__(self, title, x, y):
        # Assign variables
        self.root = Tk()
        self.title = title
        self.x = x
        self.y = y

        # Responsive window
        self.root.grid_rowconfigure(0, weight =1)
        self.root.grid_columnconfigure(0, weight =1)

        # Ban resazing
        self.root.resizable(False,False)

        # Value - value of the entry
        self.entryText = StringVar()

        # Set title of the window
        self.setTitle()

        # Make the window
        self.makeWindow()

        # 1. Row
        self.makeEntry(0, 0)

        # 3. Row
        self.makeButton(".", 2, 0)
        self.makeButton("x³", 2, 1)
        self.makeButton("1/x", 2, 2)
        self.makeButton("²√x", 2, 3)

        # 4. Row
        self.makeButton("x²", 3, 0)
        self.makeButton("AC", 3, 1)
        self.makeButton("⌫", 3, 2)
        self.makeButton("/", 3, 3)

        # 5. Row
        self.makeButton("7", 4, 0)
        self.makeButton("8", 4, 1)
        self.makeButton("9", 4, 2)
        self.makeButton("*", 4, 3)

        # 6. Row
        self.makeButton("4", 5, 0)
        self.makeButton("5", 5, 1)
        self.makeButton("6", 5, 2)
        self.makeButton("-", 5, 3)

        # 7. Row
        self.makeButton("1", 6, 0)
        self.makeButton("2", 6, 1)
        self.makeButton("3", 6, 2)
        self.makeButton("+", 6, 3)

        # 8. Row
        self.makeButton("0", 7, 0)
        self.makeButton("(", 7, 1)
        self.makeButton(")", 7, 2)
        self.makeButton("=", 7, 3)

    # Set title of the window
    def setTitle(self):
        self.root.title(self.title)

    # Make the window
    def makeWindow(self):
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # Calculate X and Y center
        centerX = int((screenWidth/2) - (self.x/2))
        centerY = int((screenHeight/2) - (self.y/2))

        self.root.geometry(f"{self.x}x{self.y}+{centerX}+{centerY}")

    # Make button
    def makeButton(self, key, row, column):
        Button(self.root, text = key, height = 3, width = 5, command = lambda: self.pressed(key)).grid(row = row, column = column, columnspan = 1)
    
        # Make entry
    def makeEntry(self, row, column):
        self.entry = Entry(self.root, textvariable = self.entryText, width = 50)
        
        # Empty the value of the entry
        self.entryText.set("")

        # Bind - when user types in entry self.typed function executed
        self.entry.bind("<Key>", self.typed)
        
        # Set grid of the entry
        self.entry.grid(row = row, column = column, columnspan = 4)

    # Execute after button is pressed
    def pressed(self, key):
        if key == "=":
            # Calculate
            self.calculate()
        elif key == "AC":
            # Delete whole entry text
            self.entry.delete(0, END)
        elif key == "⌫":
            # Delete last char in entry
            self.entry.delete(self.entry.index("end") - 1)
        elif key == "x²":
            # Added squre
            self.entry.insert("end", "**2")
        elif key == "²√x":
            # Added squre root
            self.entry.insert("end", "**(1/2)")
        elif key == "x³":
            # Added cube
            self.entry.insert("end", "**3")
        elif key == "1/x":
            # Added half
            self.entry.insert("end", "/2")
        else:
            # Number added to entry
            self.entry.insert("end", key)

    def typed(self, event):
        # Chars that are acceptable in entry
        acceptableChars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "=", "(", ")", "."]

        # Get current text of the entry
        currentText = self.entry.get()

        # Key code of the backspace
        deleteKeyCode = 855638143

        if event.keycode == deleteKeyCode:
            # Backspace pressed - delete last char in entry
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
            # Trying to calc
            self.operation = eval(self.entry.get())
        except:
            # There is syntax error
            messagebox.showerror("Error", "Syntax Error")
        else:
            # No error
            self.entryText.set(self.operation)
