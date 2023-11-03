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
        self.data_frame.grid(row=1, column=0)
        text_box=tk.Text(self.data_frame,width=50, height=5)
        text_box.grid(row=0, column=0)
        scroll_y=tk.Scrollbar(self.data_frame)
        scroll_y.grid(row=0, column=1, sticky='NS')
        scroll_y.config(command=text_box.yview)
        text_box.config(yscrollcommand=scroll_y.set)

        scroll_x=tk.Scrollbar(self.data_frame, orient=tk.HORIZONTAL)
        scroll_x.grid(row=1, column=0, sticky='EW')
        scroll_x.config(command=text_box.xview)
        text_box.config(xscrollcommand=scroll_x.set)

        self.main.mainloop()

    def display_table(self):
        pass

test = GUI()


