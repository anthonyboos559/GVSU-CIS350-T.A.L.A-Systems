import tkinter as tk
import sys

class GUI:
    """Displays the GUI that will utilize the backend Logic"""
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("T.A.L.A Data Management")
        self.main.geometry("300x300")

        self.tables = {"Inventory":0, "Employee":1, "Member":2}
        self.table = tk.IntVar(self.main, 0)
        self.table_frame = tk.LabelFrame(master=self.main, text= "Table:")
        i = 0
        for text, value in self.tables.items():
            tk.Radiobutton(master= self.table_frame, text= text, variable= self.table, value= value).grid(row=i, column=0, sticky="W")
            i+=1
        tk.Button(master= self.table_frame, text="Get data", command=self.display_table).grid(row=i, column=0)
        self.table_frame.grid(row=0, column=0, sticky="NW")
        
        self.actions = {"Add":0, "Delete":1, "Edit":2, "View":3}
        self.action = tk.IntVar(self.main, 0)
        self.action_frame = tk.LabelFrame(master= self.main, text="Action:")
        i = 0
        for text, value in self.actions.items():
            tk.Radiobutton(master= self.action_frame, text= text, variable= self.action, value= value).grid(row=i, column=0, sticky="W")
            i+=1
        self.action_frame.grid(row=0, column=1, sticky="N")

        self.data_frame = tk.Frame(master= self.main)
        self.main.mainloop()

    def display_table(self):
        pass

test = GUI()


