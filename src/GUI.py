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

        tk.Label(master= self.table_frame, text="Select table:").pack()
        for text, value in self.tables.items():
            tk.Radiobutton(master= self.table_frame, text= text, variable= self.table, value= value).pack(side=tk.TOP, ipady=5)
        self.table_frame.place(x=0, y=0)
        
        self.test = {"This":0, "Is":1, "A":2, "Test!":3}
        
        testdict = {"text":"test!"}
        for child in self.table_frame.winfo_children():
            child.configure(testdict)
        
        
        self.field_frame = tk.Frame(master=self.main)

        #tk.Listbox(master= self.field_frame, listvariable=self.selected_buttons, height=6).pack()
        self.field_frame.place(x=100,y=0)
        txt = tk.Text(master= self.main, height = 8, width= 35)
        txt.place(x=10, y=125)
        txt.insert(tk.END, "ITEM | QUANTITY | PRICE\nApple | 245 | $2.67\nOrange | 34 | $1\nPizza | 1,000,000 | $0\nPierogi | 57 | $3.25")
        self.main.mainloop()




test = GUI()


