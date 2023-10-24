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
        self.buttons = {"Add":"+", "Delete":"-", "Alter":"a", "New":"n"}
        self.selected_buttons = tk.StringVar(value=["Add", "Delete", "Alter", "New"])
        table_frame = tk.Frame(master=self.main, width=100)
        tk.Label(master= table_frame, text="Select table:").pack()
        for text, value in self.tables.items():
            tk.Radiobutton(master= table_frame, text= text, variable= self.table, value= value).pack(side=tk.TOP, ipady=5)
        table_frame.place(x=0, y=0)
        button_frame = tk.Frame(master=self.main)
        tk.Listbox(master= button_frame, listvariable=self.selected_buttons, height=6).pack()
        button_frame.place(x=100,y=0)
        txt = tk.Text(master= self.main, height = 8, width= 35)
        txt.place(x=10, y=125)
        txt.insert(tk.END, "ITEM | QUANTITY | PRICE\nApple | 245 | $2.67\nOrange | 34 | $1\nPizza | 1,000,000 | $0\nPierogi | 57 | $3.25")
        self.main.mainloop()

    def clear_gui(self) -> None:
        pass

    def pass_to_database(self) -> None:
        #Send components of the SQL query the Databse object
        pass

    def display_buttons(self) -> None:
        pass

    def get_results(self):
        pass

    def print_table(self):
        pass

    def get_input(self):
        pass


test = GUI()


