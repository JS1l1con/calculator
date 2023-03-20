import tkinter as tk
from lib.lib import *

root = tk.Tk()

root.title("Kalkulacka")
root.geometry("600x400+1000+500")

lable = tk.Label(text = "Kalkulacka")
lable.pack()

# Buttons
button1 = tk.Button(root, text="1", command=pressedKey("1"))
button1.pack()
button2 = tk.Button(root, text="2", command=pressedKey("2"))
button2.pack()
button3 = tk.Button(root, text="3", command=pressedKey("3"))
button3.pack()
button4 = tk.Button(root, text="4", command=pressedKey("4"))
button4.pack()
button5 = tk.Button(root, text="5", command=pressedKey("5"))
button5.pack()
button6 = tk.Button(root, text="6", command=pressedKey("6"))
button6.pack()
button7 = tk.Button(root, text="7", command=pressedKey("7"))
button7.pack()
button8 = tk.Button(root, text="8", command=pressedKey("8"))
button8.pack()
button9 = tk.Button(root, text="9", command=pressedKey("9"))
button9.pack()
plus = tk.Button(root, text="+", command=pressedKey("+"))
plus.pack()
minus = tk.Button(root, text="-", command=pressedKey("-"))
minus.pack()
multiply = tk.Button(root, text="*", command=pressedKey("*"))
multiply.pack()
divide = tk.Button(root, text="÷", command=pressedKey("÷"))
divide.pack()

root.mainloop()