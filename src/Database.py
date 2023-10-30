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

    def pass_data_to_gui(self, table: str):
        """Pass informaiton on the specified database to the gui."""

    def view_data(self, table: str) -> list[tuple[str]]:
        """Returns the contents of this table in the database.

        Params:
            table: A string representing the table we want to view the contents of.

        Returns:
            Returns either the contents of the specified table and a success message, or a boolean of False
            and a failure message for the GUI to use to tell the user a satus update.
        """
        if table.isidentifier() and (table == 'Inventory' or table == 'Employee' or table == 'Member'):
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
        self.load_employee_table()
        self.load_member_table()

    def load_member_table(self):
        """Loads member data with data from files."""
        with open('memberOriginalData', 'r') as mem_file:
            all_data = mem_file.readlines()
            for line in all_data:
                data_split = line.split()
                self.add_row("Member", data_split)



    def load_employee_table(self):
        """Loads employee data with data from starting files."""
#         create_employee_table = "CREATE TABLE Employee(emp_id INT PRIMARY KEY, Name VARCHAR(30),
#                                       Position VARCHAR(20), Email VARCHAR(35), Phone_num INT,
#                                       Salary NUMERIC(6, 2));"
        with open('employeeOriginalData', 'r') as empFile:
            empFileLines = empFile.readlines()
            for line in empFileLines:
                emp_split = line.split()
                self.add_row('Employee', emp_split)



    def load_inventory_table(self):
        """The method that will load the inventory table with the correct original data based upon the file data.
        """
        with open('inventoryOriginalData', 'r') as inv_file:
            all_data = inv_file.readlines()
            for line in all_data:
                line_split = line.split()
                self.add_row("Inventory", line_split)

    def edit_row(self, items: list[str]):
        """edit a specific item in a specific row

        Params:
            items: a list of strings. First element is table, second element is action (edit), third element
            is what column we are editing, fourth element is what we are changing it to."""
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
        elif table.isidentifier() and table == 'Employee':
            id = items_to_add[0]
            name = items_to_add[1]
            position = items_to_add[2]
            email = items_to_add[3]
            phone_num = items_to_add[4]
            salary = items_to_add[5]
            insertion_stat = 'INSERT INTO Employee (emp_id, Name, Position, Email, Phone_num, Salary) VALUES (?, ?, ?, ?, ?, ?)'
            items_to_be_inserted = (id, name, position, email, phone_num, salary)
            self.cursor.execute(insertion_stat, items_to_be_inserted)
            self.connection.commit()
        # "INSERT INTO Employee VALUES(emp_id, Name, Position, Email, Phone_num, Salary);"
        elif table.isidentifier() and table == 'Member':
            id = items_to_add[0]
            name = items_to_add[1]
            email = items_to_add[2]
            phone_num = items_to_add[3]
            points = items_to_add[4]
            insertion_stat = 'INSERT INTO Member (member_id, Name, Email, Phone_num, Points) VALUES (?, ?, ?, ?, ?)'
            items_to_insert = id, name, email, phone_num, points
            self.cursor.execute(insertion_stat, items_to_insert)
            self.connection.commit()
        # "INSERT INTO Member VALUES(member_id, name, email, phone_num, points);"

    def delete_row(self, items: list[str]):
        """Deletes the row with the specified id passed in.

        Params:
            id: A string representing the id number for the row we want to delete
        """
        table = items[0]
        row_id = items[2]
        if table.isidentifier() and table == 'Inventory':
            statement_to_execute = "DELETE FROM Inventory WHERE item_id=?;"
            self.cursor.execute(statement_to_execute, (row_id,))
            self.connection.commit()
        elif table.isidentifier() and table == 'Employee':
            statement_to_execute = 'DELETE FROM Employee WHERE emp_id=?'
            self.cursor.execute(statement_to_execute, (row_id,))
            self.connection.commit()
        elif table.isidentifier() and table == "Member":
            statement_to_execute = "DELETE FROM Member WHERE member_id=?;"
            self.cursor.execute(statement_to_execute, (row_id,))
            self.connection.commit()

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
    def execute_command(self, items: list[str]):
        """executes the command our user wants (edit row, add row, delete row) based on what's in the list at
    index 1. Index 0 is the table we want to mess with, index 1 is the command we want to execute.
    index 3, 4, ... are the required parameters for that command."""

        pass

    def create_tables(self):
        """Create the original tables."""
        # Once we have all the bahaviors working. Our innit method should have an if statement that will check if the
        # db and tables exist, if not, read from that file with default values. If it does exist, then use the values
        # from the previous db creation/usage.
        create_inventory_table = "CREATE TABLE Inventory(item_id INT PRIMARY KEY, Product_name VARCHAR(30), Count INT, Price NUMERIC(5, 2));"
        create_employee_table = "CREATE TABLE Employee(emp_id INT PRIMARY KEY, Name VARCHAR(30), Position VARCHAR(20), Email VARCHAR(35), Phone_num INT, Salary NUMERIC(6, 2));"
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
s.view_data('Inventory')
s.view_data('Employee')
s.view_data('Member')
s.delete_row(['Member', 'delete', '10'])
s.view_data('Member')
