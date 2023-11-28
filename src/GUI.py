import tkinter as tk
import Database as db

class GUI:
    """Displays the GUI that will utilize the backend Logic"""
    def __init__(self):
        self.db = db.Database()
        self.main = tk.Tk()
        self.main.title("T.A.L.A Data Management")
        #self.main.geometry("300x300")

        self.tables = {0:"Inventory", 1:"Employee", 2:"Member"}
        self.table = tk.IntVar(self.main, 0)
        self.table_frame = tk.LabelFrame(master=self.main, text= "Table:")
        i = 0
        for value, text in self.tables.items():
            tk.Radiobutton(master= self.table_frame, text= text, variable= self.table, value= value, command= self.configure_fields).grid(row=i, column=0, sticky="W")
            i+=1
        tk.Button(master= self.table_frame, text="Get data", command=self.display_table).grid(row=i, column=0)
        self.table_frame.grid(row=0, column=0, sticky="NW")
        
        self.actions = {0:"Add", 1:"Delete", 2:"Edit", 3:"View"}
        self.action = tk.IntVar(self.main, 0)
        self.action_frame = tk.LabelFrame(master= self.main, text="Action:")
        i = 0
        for value, text in self.actions.items():
            tk.Radiobutton(master= self.action_frame, text= text, variable= self.action, value= value, command= self.configure_fields).grid(row=i, column=0, sticky="W")
            i+=1
        self.action_frame.grid(row=0, column=1, sticky="N")

        self.field_frame = tk.LabelFrame(master= self.main, text="Fields:")
        self.init_fields()
        self.field_frame.grid(row= 0, column= 2)

        self.configs = {"Table": {0: [2, 3, 4], 1: [2, 5, 6, 7, 8], 2:[2, 5, 6, 9]}, "Action": {0: [1], 1: [0], 2: [0], 3: []}}

        self.configure_fields()


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
        self.text_box.config(state=tk.NORMAL)
        selected_value = self.table.get()
        self.text_box.delete('1.0', 'end')
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
        self.text_box.config(state=tk.DISABLED)


    def init_fields(self):
        self.fields = []
        ID_frame = tk.LabelFrame(master= self.field_frame, text= "ID:")
        self.ID = tk.StringVar(master= ID_frame, value="0")
        tk.OptionMenu(master= ID_frame, variable=self.ID, value="0").grid(row= 0, column= 0)
        ID_frame.grid(row=0, column=0)
        self.fields.append(ID_frame)

        static_id_frame = tk.LabelFrame(master= self.field_frame, text= "ID:")
        tk.Label(master = static_id_frame, text= self.ID.get()).grid(row= 0, column= 0)
        static_id_frame.grid(row=0, column=0)
        self.fields.append(static_id_frame)

        name_frame = tk.LabelFrame(master= self.field_frame, text="Name:")
        self.name = tk.StringVar(master=name_frame, value="")
        tk.Entry(master=name_frame, textvariable= self.name).grid(row= 0, column= 0)
        name_frame.grid(row=0, column=1)
        self.fields.append(name_frame)

        count_frame = tk.LabelFrame(master= self.field_frame, text="Count:")
        self.count = tk.StringVar(master= count_frame, value="")
        tk.Entry(master= count_frame, textvariable= self.count).grid(row= 0, column= 0)
        count_frame.grid(row= 1, column= 0)
        self.fields.append(count_frame)

        price_frame = tk.LabelFrame(master= self.field_frame, text="Price:")
        self.price = tk.StringVar(master= price_frame, value="")
        tk.Entry(master= price_frame, textvariable= self.price).grid(row= 0, column= 0)
        price_frame.grid(row= 1, column= 1)
        self.fields.append(price_frame)

        email_frame = tk.LabelFrame(master= self.field_frame, text="Email:")
        self.email = tk.StringVar(master= email_frame, value="")
        tk.Entry(master= email_frame, textvariable= self.email).grid(row= 0, column= 0)
        email_frame.grid(row= 1, column= 0)
        self.fields.append(email_frame)

        phone_frame = tk.LabelFrame(master= self.field_frame, text="Phone:")
        self.phone = tk.StringVar(master= phone_frame, value="")
        tk.Entry(master= phone_frame, textvariable= self.phone).grid(row= 0, column= 0)
        phone_frame.grid(row= 1, column= 1)
        self.fields.append(phone_frame)

        position_frame = tk.LabelFrame(master= self.field_frame, text="Position:")
        self.position = tk.StringVar(master= position_frame, value="")
        tk.Entry(master= position_frame, textvariable= self.position).grid(row= 0, column= 0)
        position_frame.grid(row= 2, column= 0)
        self.fields.append(position_frame)

        salary_frame = tk.LabelFrame(master= self.field_frame, text="Salary:")
        self.salary = tk.StringVar(master= salary_frame, value="")
        tk.Entry(master= salary_frame, textvariable= self.salary).grid(row= 0, column= 0)
        salary_frame.grid(row= 2, column= 1)
        self.fields.append(salary_frame)

        points_frame = tk.LabelFrame(master= self.field_frame, text="Points:")
        self.points = tk.StringVar(master= points_frame, value="")
        tk.Entry(master= points_frame, textvariable= self.points).grid(row= 0, column= 0)
        points_frame.grid(row= 2, column= 0)
        self.fields.append(points_frame)
    
    def get_config(self):
        if self.action.get() == 3:
            return []
        else:
            return self.configs["Action"][self.action.get()] + self.configs["Table"][self.table.get()]

    def configure_fields(self):
        config = self.get_config()
        for index, field in enumerate(self.fields):
            if index not in config:
                field.grid_remove()
            else:
                field.grid()

        

test = GUI()


