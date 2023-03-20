import tkinter as tk

root = tk.Tk()

root.title("Kalkulacka")
root.geometry("600x400+50+50")

lable = tk.Label(text = "Kalkulacka")
lable.pack()

button1 = Button(root, text = "1")

root.mainloop()