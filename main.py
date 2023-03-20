import tkinter as tk
from lib.lib import *

root = tk.Tk()
root.title("Kalkulacka")
root.geometry("600x400+1000+500")

lable = tk.Label(text = "Kalkulacka")
lable.pack()

# Buttons
tk.Button(root, text="1", command=lambda: pressedKey("1")).pack()
tk.Button(root, text="2", command=lambda: pressedKey("2")).pack()
tk.Button(root, text="3", command=lambda: pressedKey("3")).pack()
tk.Button(root, text="4", command=lambda: pressedKey("4")).pack()
tk.Button(root, text="5", command=lambda: pressedKey("5")).pack()
tk.Button(root, text="6", command=lambda: pressedKey("6")).pack()
tk.Button(root, text="7", command=lambda: pressedKey("7")).pack()
tk.Button(root, text="8", command=lambda: pressedKey("8")).pack()
tk.Button(root, text="9", command=lambda: pressedKey("9")).pack()
tk.Button(root, text="+", command=lambda: pressedKey("+")).pack()
tk.Button(root, text="-", command=lambda: pressedKey("-")).pack()
tk.Button(root, text="*", command=lambda: pressedKey("*")).pack()
tk.Button(root, text="÷", command=lambda: pressedKey("÷")).pack()

root.mainloop()