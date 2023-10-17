import sqlite3 as sql
class Database:

    def __init__(self):
        self.query = None
        employee_database_tables = None
        inventory_database_tables = None
        # This is a test


    def edit_row(self, items: list):
        pass

    def add_row(self, items: list):
        "INSERT INTO Inventory VALUES(id, product_name, count, price);"
        "INSERT INTO Employee VALUES(emp_id, name, position, email, phone_num, salary);"
        "INSERT INTO Member VALUES(member_id, name, email, phone_num, points);"
        pass

    def delete_row(self, items: list):
        pass

    # receive inputs from GUI and store the passed information in the instance variables and format the correct
    # SQL command
    def pass_to_database(self, action: list[str, str, str]):
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

    def create_table(self, str: str):
        "CREATE TABLE Inventory(ID INT PRIMARY KEY, Product_name VARCHAR(30), Count INT, Price NUMERIC(5, 2));"
        "CREATE TABLE Employee(emp_id INT PRIMARY KEY, Name VARCHAR(30), Position VARCHAR(5), Email VARCHAR(40) Phone_num VARCHAR(22) Salary NUMERIC(6, 2));"
        "CREATE TABLE Member(member_id INT PRIMARY KEY, Name VARCHAR(30), Email VARCHAR(40), Phone_num VARCHAR(22), Points INT);"

        """
        Creates the items database table

        Params:
            str: A string that represents what table we would like to make. This argument
                should only ever be employee, member, or items
        """
        pass

    def create_tables(self):
        """Create both tables employees and items tables."""
        pass

    def create_original_tables(self):
        """Create the original employee and items table which will be used in the innit method.
         """
        pass
    # should we store the original data in a file, or within the code?

    def ensure_changes_are_safe(self):
        """Ensures that the SQL command to be executed is safe and doesn't contain things like dropping tables"""
        invalid_values = ["'", '"', ';', 'employee_database_tables', 'inventory_database_tables']
        pass



