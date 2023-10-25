import sqlite3
class Database:
    def __init__(self):
        """Alec tested code: From here"""
        self.connection = sqlite3.connect("T.A.L.A. System Database")
        self.cursor = self.connection.cursor()
        # Once we have all the bahaviors working. Our innit method should have an if statement that will check if the
        # db and tables exist, if not, read from that file with default values. If it does exist, then use the values
        # from the previous db creation/usage.
        self.create_tables()
        self.load_tables_original_data()
        """To here: end Alec tested code"""

        self.query = None
        employee_database_tables = None
        inventory_database_tables = None
        # This is a test to add DB Branch
        # this is another test to see if I'm pulling stuff correctly

    def view_data(self, table: str):
        """Returns the contents of this table in the database.

        Params:
            table: A string representing the table we want to view the contents of."""
        if table.isidentifier():
            rows = self.cursor.execute(f"SELECT * FROM {table};")
            self.connection.commit()
            contents = rows.fetchall()
            print(contents)
            return contents, f"Successfully returned contents of table: {table}"
        else:
            return False, f"That was not a valid table name"


    def load_tables_original_data(self):
        """Method to load the original data tables of each table"""
        self.load_inventory_table()
        # self.load_employee_table()
        # self.load_member_table()

    def load_inventory_table(self):
        """The method that will load the inventory table with the correct original data based upon the file data.
        """
        with open('inventoryOriginalData', 'r+') as inv_file:
            all_data = inv_file.readlines()
            for line in all_data:
                print(line.split())
                line_split = line.split()
                self.add_row("Inventory", line_split)




    def edit_row(self, items: list):
        pass

    def add_row(self, table: str, items_to_add: list[str]):
        """Allows us to add a row/insert a new item and it's corresponding fields.

        Params:
            table: A string to represent the table we want to insert into.
            items_to_add: A list of strings holding the values we want to add to our database."""
        if table.isidentifier() and table == 'Inventory':
            id = items_to_add[0]
            name = items_to_add[1]
            count = items_to_add[2]
            price = items_to_add[3]
            self.cursor.execute('INSERT INTO Inventory (item_id, Product_name, Count, Price) VALUES (?, ?, ?, ?)',
               (id, name, count, price))
            self.connection.commit()
        # "INSERT INTO Employee VALUES(emp_id, name, position, email, phone_num, salary);"
        # "INSERT INTO Member VALUES(member_id, name, email, phone_num, points);"

    def delete_row(self, items: list):
        pass

    # receive inputs from GUI and store the passed information in the instance variables and format the correct
    # SQL command
    def pass_to_database(self, action: list[str]):
        """Receive command and table the command coresponds to from the GUI and execute that command."""
        commands = {"delete": self.delete_row,
                   "edit": self.edit_row,
                   "add": self.add_row}
        command = action[0]
        commands[command](action[1:])



        pass

    def format_sql_command(self, query: str):
        pass

    # use command line format to execute the different sql commands.
    # So a dictionary with pointers to the methods will be needed.
    def execute_command(self):
        pass

    def create_tables(self):
        """Create the original tables."""
        # Once we have all the bahaviors working. Our innit method should have an if statement that will check if the
        # db and tables exist, if not, read from that file with default values. If it does exist, then use the values
        # from the previous db creation/usage.
        create_inventory_table = "CREATE TABLE Inventory(item_id INT PRIMARY KEY, Product_name VARCHAR(30), Count INT, Price NUMERIC(5, 2));"
        create_employee_table = "CREATE TABLE Employee(emp_id INT PRIMARY KEY, Name VARCHAR(30), Position VARCHAR(5), Email VARCHAR(40), Phone_num INT, Salary NUMERIC(6, 2));"
        create_member_table = "CREATE TABLE Member(member_id INT PRIMARY KEY, Name VARCHAR(30), Email VARCHAR(40), Phone_num VARCHAR(22), Points INT);"
        self.cursor.execute(create_inventory_table)
        self.cursor.execute(create_employee_table)
        self.cursor.execute(create_member_table)
        self.connection.commit()



    def create_original_tables(self):
        """Create the original employee and items table which will be used in the innit method.
         """
        pass
    # should we store the original data in a file, or within the code?

    def ensure_changes_are_safe(self):
        """Ensures that the SQL command to be executed is safe and doesn't contain things like dropping tables"""
        invalid_values = ["'", '"', ';', 'employee_database_tables', 'inventory_database_tables']
        pass


# allowing me to test behaviors
s = Database()
s.view_data('Member')
s.view_data('Employee')
