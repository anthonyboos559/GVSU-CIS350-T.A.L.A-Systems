import tkinter as tk
import src.Database as db

class GUI:
    """Displays the GUI that will utilize the backend Logic"""
    def __init__(self):
        self._db = db.Database()
        self._main = tk.Tk()
        self._main.title("T.A.L.A Data Management")

        self._tables = {0:"Inventory", 1:"Employee", 2:"Member"}
        self._actions = {0:"Add", 1:"Delete", 2:"Edit", 3:"View"}
        self._configs = {"Table": {0: [2, 3, 4], 1: [2, 5, 6, 7, 8], 2:[2, 5, 6, 9]}, "Action": {0: [1], 1: [0], 2: [0], 3: []}}
        
        
        self._init_table_buttons()
        self._init_action_buttons()
        self._init_fields()
        self._init_data_box()
        self._variables = {2: self._name, 3: self._count, 4: self._price, 5:self._email, 6: self._phone, 7: self._position, 8: self._salary, 9: self._points}
        self._configure_fields()
        self._main.mainloop()

    def _init_table_buttons(self):
        self._table_var = tk.IntVar(self._main, 0)
        self._table_frame = tk.LabelFrame(master=self._main, text= "Table:")
        self._table_frame.grid(row=0, column=0, sticky="NW")
        for i, (value, text) in enumerate(self._tables.items()):
            tk.Radiobutton(master= self._table_frame, text= text, variable= self._table_var, value= value, command= self._configure_fields).grid(row=i, column=0, sticky="W")

    def _init_action_buttons(self):
        self._action_var = tk.IntVar(self._main, 0)
        self._action_frame = tk.LabelFrame(master= self._main, text="Action:")
        self._action_frame.grid(row=0, column=1, sticky="N")
        for i, (value, text) in enumerate(self._actions.items()):
            tk.Radiobutton(master= self._action_frame, text= text, variable= self._action_var, value= value, command= self._configure_fields).grid(row=i, column=0, sticky="W")

    def _init_fields(self):
        self._field_frame = tk.LabelFrame(master= self._main, text="Fields:")
        self._field_frame.grid(row= 0, column= 2)
        self._fields = []
        tk.Button(master = self._field_frame, text= "Submit\nRequest", command= self._submit_query).grid(row= 0, column= 0, sticky = "W")
        ID_frame = tk.LabelFrame(master= self._field_frame, text= "ID:")
        self._ID_var = tk.StringVar(master= ID_frame, value="1")
        self._ID_menu = tk.OptionMenu(master= ID_frame, variable=self._ID_var, value="1")
        self._ID_menu.grid(row= 0, column= 0)
        ID_frame.grid(row=0, column=0, sticky= "E")
        self._fields.append(ID_frame)

        static_id_frame = tk.LabelFrame(master= self._field_frame, text= "ID:")
        self._static_ID = tk.Label(master = static_id_frame, text= "1")
        self._static_ID.grid(row= 0, column= 0)
        static_id_frame.grid(row=0, column=0, sticky = "E")
        self._fields.append(static_id_frame)

        name_frame = tk.LabelFrame(master= self._field_frame, text="Name:")
        self._name = tk.StringVar(master=name_frame, value="")
        tk.Entry(master=name_frame, textvariable= self._name).grid(row= 0, column= 0)
        name_frame.grid(row=0, column=1)
        self._fields.append(name_frame)

        count_frame = tk.LabelFrame(master= self._field_frame, text="Count:")
        self._count = tk.StringVar(master= count_frame, value="")
        tk.Entry(master= count_frame, textvariable= self._count).grid(row= 0, column= 0)
        count_frame.grid(row= 1, column= 0)
        self._fields.append(count_frame)

        price_frame = tk.LabelFrame(master= self._field_frame, text="Price:")
        self._price = tk.StringVar(master= price_frame, value="")
        tk.Entry(master= price_frame, textvariable= self._price).grid(row= 0, column= 0)
        price_frame.grid(row= 1, column= 1)
        self._fields.append(price_frame)

        email_frame = tk.LabelFrame(master= self._field_frame, text="Email:")
        self._email = tk.StringVar(master= email_frame, value="")
        tk.Entry(master= email_frame, textvariable= self._email).grid(row= 0, column= 0)
        email_frame.grid(row= 1, column= 0)
        self._fields.append(email_frame)

        phone_frame = tk.LabelFrame(master= self._field_frame, text="Phone:")
        self._phone = tk.StringVar(master= phone_frame, value="")
        tk.Entry(master= phone_frame, textvariable= self._phone).grid(row= 0, column= 0)
        phone_frame.grid(row= 1, column= 1)
        self._fields.append(phone_frame)

        position_frame = tk.LabelFrame(master= self._field_frame, text="Position:")
        self._position = tk.StringVar(master= position_frame, value="")
        tk.Entry(master= position_frame, textvariable= self._position).grid(row= 0, column= 0)
        position_frame.grid(row= 2, column= 0)
        self._fields.append(position_frame)

        salary_frame = tk.LabelFrame(master= self._field_frame, text="Salary:")
        self._salary = tk.StringVar(master= salary_frame, value="")
        tk.Entry(master= salary_frame, textvariable= self._salary).grid(row= 0, column= 0)
        salary_frame.grid(row= 2, column= 1)
        self._fields.append(salary_frame)

        points_frame = tk.LabelFrame(master= self._field_frame, text="Points:")
        self._points = tk.StringVar(master= points_frame, value="")
        tk.Entry(master= points_frame, textvariable= self._points).grid(row= 0, column= 0)
        points_frame.grid(row= 2, column= 0)
        self._fields.append(points_frame)

    def _init_data_box(self):
        self._data_frame = tk.Frame(master= self._main)
        self._data_frame.grid(row=1, column=0, columnspan= 3, sticky="NSEW")
        self._text_box = tk.Text(self._data_frame, height= 6, state= tk.DISABLED)
        self._text_box.grid(row= 0, column= 0, columnspan= 3, rowspan= 2, sticky="NSEW")
        scroll_y = tk.Scrollbar(self._data_frame)
        scroll_y.grid(row= 0, column= 3, rowspan= 2, sticky= 'NSE')
        scroll_y.config(command=self._text_box.yview)
        self._text_box.config(yscrollcommand=scroll_y.set)

        scroll_x=tk.Scrollbar(self._data_frame, orient=tk.HORIZONTAL)
        scroll_x.grid(row= 2, column= 0, sticky= 'EWN', columnspan= 3)
        scroll_x.config(command= self._text_box.xview)
        self._text_box.config(xscrollcommand=scroll_x.set)

    def _submit_query(self):
        self.display_table(self._db.pass_to_database({"Table": self._tables[self._table_var.get()],
                                                      "Action": self._actions[self._action_var.get()],
                                                      "Args": [self._ID_var.get()] + \
                                                        [self._variables[var_id].get() for var_id in self._configs["Table"][self._table_var.get()]]}))

    def display_table(self, data):
        self._text_box.config(state=tk.NORMAL)
        self._text_box.delete('1.0', tk.END)
        displayed_text = ''
        for row in data:
            displayed_text += ', '.join(str(i) for i in row) + '\n'
        self._text_box.insert(tk.END, displayed_text)
        self._text_box.config(state=tk.DISABLED)

    def _set_data(self, index):
        self._ID_var.set(index)
        if self._action_var.get() == 0:
            for var_id in self._configs["Table"][self._table_var.get()]:
                self._variables[var_id].set(value="")
            return None
        data = self._db._view_data([self._tables[self._table_var.get()]])
        data = data[int(index)-1]
        for i, var_id in enumerate(self._configs["Table"][self._table_var.get()]):
            self._variables[var_id].set(value=data[i+1])

    def _update_ids(self):
        new_ids = self._db.get_all_ids(self._tables[self._table_var.get()])
        if self._action_var.get() == 0:
            self._static_ID.config(text= str(new_ids[-1][0]+1))
        else:
            menu = self._ID_menu['menu']
            menu.delete(0, tk.END)
            for id in new_ids:
                menu.add_command(label=id, command=lambda val=id[0]: self._set_data(val))

    def _get_config(self):
        if self._action_var.get() == 3:
            return []
        else:
            return self._configs["Action"][self._action_var.get()] + self._configs["Table"][self._table_var.get()]

    def _configure_fields(self):
        config = self._get_config()
        self._update_ids()
        self._set_data(self._ID_var.get())
        for index, field in enumerate(self._fields):
            if index not in config:
                field.grid_remove()
            else:
                field.grid()
    


