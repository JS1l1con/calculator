from classes.GUI import GUI

GUI = GUI("Kalkulačka", 400, 600)

GUI.makeEntry(0, 0)

# Numbers
GUI.makeButton("1", 5, 0)
GUI.makeButton("2", 5, 1)
GUI.makeButton("3", 5, 2)
GUI.makeButton("4", 4, 0)
GUI.makeButton("5", 4, 1)
GUI.makeButton("6", 4, 2)
GUI.makeButton("7", 3, 0)
GUI.makeButton("8", 3, 1)
GUI.makeButton("9", 3, 2)
GUI.makeButton("0", 6, 0)

# Operations
GUI.makeButton("AC", 1, 2)
GUI.makeButton("⌫", 1, 3)
GUI.makeButton("/", 2, 3)
GUI.makeButton("*", 3, 3)
GUI.makeButton("-", 4, 3)
GUI.makeButton("+", 5, 3)
GUI.makeButton("=", 6, 3)

GUI.startApp()