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
        for text, value in self.tables.items():
            tk.Radiobutton(master= self.table_frame, text= text, variable= self.table, value= value).pack(side=tk.TOP, ipady=5)
        self.table_frame.pack(side=tk.LEFT)
        
        self.actions = {"Add":0, "Delete":1, "Edit":2, "View":3}
        self.action = tk.IntVar(self.main, 0)
        self.action_frame = tk.LabelFrame(master= self.main, text="Action:")
        for text, value in self.actions.items():
            tk.Radiobutton(master= self.action_frame, text= text, variable= self.table, value= value).pack(side=tk.TOP, ipady=5)
        self.action_frame.pack(side= tk.LEFT)

        self.data_frame = tk.Frame(master= self.main)

        self.main.mainloop()

    def display_table(self):
        pass

    




test = GUI()


