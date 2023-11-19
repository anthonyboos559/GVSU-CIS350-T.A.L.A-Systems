import tkinter as tk
import sys
import Database
class GUI:
    """Displays the GUI that will utilize the backend Logic"""
    def __init__(self):
        self.db = Database.Database()
        self.main = tk.Tk()
        self.main.title("T.A.L.A Data Management")
        #self.main.geometry("300x300")

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

        self.field_frame = tk.LabelFrame(master= self.main, text="Fields:")

        self.fields = self.init_fields()
        self.field_frame.grid(row= 0, column= 2)


        self.data_frame = tk.Frame(master= self.main)
        self.data_frame.grid(row=1, column=0, columnspan=3)
        self.text_box=tk.Text(self.data_frame,width=50, height=5)
        self.text_box.grid(row=0, column=0, columnspan=3)
        scroll_y=tk.Scrollbar(self.data_frame)
        scroll_y.grid(row=0, column=3, sticky='NS')
        scroll_y.config(command=self.text_box.yview)
        self.text_box.config(yscrollcommand=scroll_y.set)

        scroll_x=tk.Scrollbar(self.data_frame, orient=tk.HORIZONTAL)
        scroll_x.grid(row=1, column=0, sticky='EW', columnspan=3)
        scroll_x.config(command=self.text_box.xview)
        self.text_box.config(xscrollcommand=scroll_x.set)

        self.main.mainloop()

    def display_table(self):
        selected_value = self.table.get()

        if selected_value == 0:
            data = self.db._view_data(['Inventory'])
            displayed_text = ''
            for row in data:
                displayed_text += ', '.join(map(str, row)) + '\n'
            self.text_box.insert(tk.END, displayed_text)
        elif selected_value == 1:
            data = self.db._view_data(['Employee'])
            displayed_text = ''
            for row in data:
                displayed_text += ', '.join(map(str, row)) + '\n'
            self.text_box.insert(tk.END, displayed_text)
        elif selected_value == 2:
            data = self.db._view_data(['Member'])
            displayed_text = ''
            for row in data:
                displayed_text += ', '.join(map(str, row)) + '\n'
            self.text_box.insert(tk.END, displayed_text)


    def init_fields(self):
        fields = []
        ID_frame = tk.LabelFrame(master= self.field_frame, text= "ID:")
        ID = tk.StringVar(master= ID_frame, value="0")
        tk.OptionMenu(master= ID_frame, variable=ID, value="0").grid(row= 0, column= 0)
        ID_frame.grid(row=0, column=0)
        fields.append(ID_frame)
        name_frame = tk.LabelFrame(master= self.field_frame, text="Name:")
        tk.Entry(master=name_frame).grid(row= 0, column= 0)
        name_frame.grid(row=1, column=0)
        fields.append(name_frame)
        count_frame = tk.LabelFrame(master= self.field_frame, text="Count:")
        tk.Entry(master= count_frame).grid(row= 0, column= 0)
        count_frame.grid(row= 2, column= 0)
        fields.append(count_frame)
        price_frame = tk.LabelFrame(master= self.field_frame, text="Price:")
        tk.Entry(master= price_frame).grid(row= 0, column= 0)
        price_frame.grid(row= 3, column= 0)
        fields.append(price_frame)
        return fields

test = GUI()


