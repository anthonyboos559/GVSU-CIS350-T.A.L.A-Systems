import sqlite3
import os

class Database:
    def __init__(self):
        self._emp_id = 1
        self._mem_id = 1
        self._inv_id = 1
        self.slash = os.sep
        self._connection = sqlite3.connect(f".{self.slash}data{self.slash}T.A.L.A. System Database")
        self._cursor = self._connection.cursor()
        # if the database file (since sqlite3 is through a db file) does not currently exist, create one based off
        # the default data from our files
        if not self._tables_exist():
            self._create_tables()
            self._load_tables_original_data()

        # This is a test to add DB Branch
        # this is another test to see if I'm pulling stuff correctly

    def _tables_exist(self):
        """Returns True if all 3 of our tables exist. Returns False otherwise."""
        for table in ["Inventory", "Employee", "Member"]:
            self._cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
            result = self._cursor.fetchone()
            self._connection.commit()
            if not result:
                return False
        return True

    def _view_data(self, data: list[str]) -> list[tuple[str]]:
        """Returns the contents of this table in the database.

        Params:
            table: A string representing the table we want to view the contents of.

        Returns:
            Returns the contents of the specified table.
        """
        table = data[0]
        if table.isidentifier() and (table == 'Inventory' or table == 'Employee' or table == 'Member'):
            rows = self._cursor.execute(f"SELECT * FROM {table};")
            self._connection.commit()
            contents = rows.fetchall()
            return contents


    def _load_tables_original_data(self):
        """Method to load the original data tables of each table"""
        self._load_inventory_table()
        self._load_employee_table()
        self._load_member_table()

    def _load_member_table(self):
        """Loads member data with data from files."""
        with open(f'.{self.slash}data{self.slash}memberOriginalData', 'r') as mem_file:
            all_data = mem_file.readlines()
            for line in all_data:
                items = []
                data_split = line.split()
                items.append("Member"), items.append("add")
                items += data_split
                self._add_row(items)

    def _load_employee_table(self):
        """Loads employee data with data from starting files."""
        with open(f'.{self.slash}data{self.slash}employeeOriginalData', 'r') as empFile:
            empFileLines = empFile.readlines()
            for line in empFileLines:
                items = []
                emp_split = line.split()
                items.append("Employee"), items.append("add")
                items += emp_split
                self._add_row(items)

    def _load_inventory_table(self):
        """The method that will load the inventory table with the correct original data based upon the file data.
        """
        with open(f'.{self.slash}data{self.slash}inventoryOriginalData', 'r') as inv_file:
            all_data = inv_file.readlines()
            for line in all_data:
                items = []
                line_split = line.split()
                items.append("Inventory"), items.append("add")
                items += line_split
                self._add_row(items)

    def _edit_row(self, data: list[str]):
        """edit a specific item in a specific row specified by the third index of the list

        Params:
            data: a list of strings. First element is table, second element is action (edit), third element
            is what column we are editing, fourth element is what we are changing it to."""

        table = data[0]
        if table == "Inventory":
            id = data[2]
            name = data[3]
            count = data[4]
            price = data[5]
            query = "UPDATE Inventory SET item_id=?, Product_name=?, Count=?, Price=? WHERE item_id=?;"
            query_data = (id, name, count, price, id)
            self._execute_sql_command(query, query_data)
        elif table == "Employee":
            id = data[2]
            name = data[3]
            position = data[4]
            email = data[5]
            phone_num = data[6]
            salary = data[7]
            query = "UPDATE Employee SET emp_id=?, Name=?, Position=?, Email=?, Phone_num=?, Salary=? WHERE emp_id=?;"
            query_data = (id, name, position, email, phone_num, salary, id)
            self._execute_sql_command(query, query_data)
        elif table == "Member":
            "CREATE TABLE Member(member_id INT PRIMARY KEY, Name VARCHAR(30), Email VARCHAR(40), Phone_num VARCHAR(22), Points INT);"
            id = data[2]
            name = data[3]
            email = data[4]
            phone_num = data[5]
            points = data[6]
            query = "UPDATE Member SET member_id=?, Name=?, Email=?, Phone_num=?, Points=? WHERE member_id=?"
            query_data = (id, name, email, phone_num, points, id)
            self._execute_sql_command(query, query_data)
        return self._view_data([table])

    def _add_row(self, items_to_add: list[str]):
        """Allows us to add a row/insert a new item and it's corresponding fields.

        Params:
            table: A string to represent the table we want to insert into.
            items_to_add: A list of strings holding the values we want to add to our database."""
        table = items_to_add[0]
        if table.isidentifier() and table == 'Inventory':
            # set id to inv_num_id value + 1. This is initially 0, so if a completely new database is being created.
            # The smalled value possible is 1.
            id = self.assign_id(table)
            name = items_to_add[3]
            count = items_to_add[4]
            price = items_to_add[5]
            self._cursor.execute('INSERT INTO Inventory (item_id, Product_name, Count, Price) VALUES (?, ?, ?, ?)',
               (id, name, count, price))
            self._connection.commit()
        elif table.isidentifier() and table == 'Employee':
            id = self.assign_id(table)
            name = items_to_add[3]
            position = items_to_add[4]
            email = items_to_add[5]
            phone_num = items_to_add[6]
            salary = items_to_add[7]
            insertion_stat = 'INSERT INTO Employee (emp_id, Name, Position, Email, Phone_num, Salary) VALUES (?, ?, ?, ?, ?, ?)'
            items_to_be_inserted = (id, name, position, email, phone_num, salary)
            self._cursor.execute(insertion_stat, items_to_be_inserted)
            self._connection.commit()
        # "INSERT INTO Employee VALUES(emp_id, Name, Position, Email, Phone_num, Salary);"
        elif table.isidentifier() and table == 'Member':
            id = self.assign_id(table)
            name = items_to_add[3]
            email = items_to_add[4]
            phone_num = items_to_add[5]
            points = items_to_add[6]
            insertion_stat = 'INSERT INTO Member (member_id, Name, Email, Phone_num, Points) VALUES (?, ?, ?, ?, ?)'
            items_to_insert = id, name, email, phone_num, points
            self._cursor.execute(insertion_stat, items_to_insert)
            self._connection.commit()
        # "INSERT INTO Member VALUES(member_id, name, email, phone_num, points);"
        return self._view_data([table])

    def _delete_row(self, items: list[str]):
        """Deletes the row with the specified id passed in.

        Params:
            id: A string representing the id number for the row we want to delete
        """
        table = items[0]
        row_id = items[2]
        if table.isidentifier() and table == 'Inventory':
            statement_to_execute = "DELETE FROM Inventory WHERE item_id=?;"
            self._cursor.execute(statement_to_execute, (row_id,))
            self._connection.commit()
        elif table.isidentifier() and table == 'Employee':
            statement_to_execute = 'DELETE FROM Employee WHERE emp_id=?'
            self._cursor.execute(statement_to_execute, (row_id,))
            self._connection.commit()
        elif table.isidentifier() and table == "Member":
            statement_to_execute = "DELETE FROM Member WHERE member_id=?;"
            self._cursor.execute(statement_to_execute, (row_id,))
            self._connection.commit()
        return self._view_data([table])

    # receive inputs from GUI and store the passed information in the instance variables and format the correct
    # SQL command
    def pass_to_database(self, data_unparsed:dict[str: str, str: list[str]]):
        """Receive command and table the command corresponds to from the GUI and execute that command."""

        table = data_unparsed["Table"]
        action = data_unparsed["Action"]
        args = data_unparsed["Args"]
        data_list = []
        data_list.append(table), data_list.append(action)
        for item in args:
            data_list.append(item)

        commands = {"Delete": self._delete_row,
                   "Edit": self._edit_row,
                   "Add": self._add_row,
                   "View": self._view_data,
                   "get data": self._get_data_based_off_primary_key,
                    "primary keys": self.get_all_ids}
        return commands[action](data_list)

    # use command line format to execute the different sql commands.
    # So a dictionary with pointers to the methods will be needed.
    def _execute_sql_command(self, query: str, user_input: tuple[str | int] = None):
        """executes the command our user wants (edit row, add row, delete row) based on what's in the list at
    index 1. Index 0 is the table we want to mess with, index 1 is the command we want to execute.
    index 3, 4, ... are the required parameters for that command."""
        # If user_input is empty: this is not a paremtized query so it has different structure for SQL Command
        # So if it is a parametized query, we will pass the tuple, if it's not, then we only pass the query.
        if not user_input:
            rows = self._cursor.execute(query)
            self._connection.commit()
        else:
            rows = self._cursor.execute(query, user_input)
            self._connection.commit()
        contents = rows.fetchall()
        return contents

    def _create_tables(self):
        """Create the original tables."""
        # Once we have all the bahaviors working. Our innit method should have an if statement that will check if the
        # db and tables exist, if not, read from that file with default values. If it does exist, then use the values
        # from the previous db creation/usage.
        create_inventory_table = "CREATE TABLE Inventory(item_id INT PRIMARY KEY, Product_name VARCHAR(30), Count INT, Price NUMERIC(5, 2));"
        create_employee_table = "CREATE TABLE Employee(emp_id INT PRIMARY KEY, Name VARCHAR(30), Position VARCHAR(20), Email VARCHAR(35), Phone_num INT, Salary NUMERIC(6, 2));"
        create_member_table = "CREATE TABLE Member(member_id INT PRIMARY KEY, Name VARCHAR(30), Email VARCHAR(40), Phone_num VARCHAR(22), Points INT);"
        self._cursor.execute(create_inventory_table)
        self._cursor.execute(create_employee_table)
        self._cursor.execute(create_member_table)
        self._connection.commit()

    def _get_data_based_off_primary_key(self, table: str, id_num: int):
        """Returns the data for the specified data row. The specified data row is by the row id (the primary key)

        Params:
            table: A string representing the name of the table we want to view the data for
            id_num (int | str): An integer or string representing the id number for the row the user to interact with.
        """
        id_name: dict[str[str]] = {"Inventory": "item_id", "Employee": "emp_id", "Member": "member_id"}
        # Return the data for the specified row.
        return self._execute_sql_command(f"SELECT * from {table} WHERE {id_name[table]}=?", (id_num,))



    def get_all_ids(self, table: str):
        """Returns the ids of all elements of the specified table

        Params:
            table: (str): A string that represents the table we want to view all the ids for."""
        if type(table) == type(list):
            # if the pass to database method was used to view all the primary keys, then a list where the first element
            # is the table we want to mess with will be passed as the argument. So code nested in this if statement
            # will handle that scenario
            table = table[0]
            primary_keys_names = {"Inventory": "item_id", "Employee": "emp_id", "Member": "member_id"}
            query = f"SELECT {primary_keys_names[table]} FROM {table};"
            return self._execute_sql_command(query)
        else:
            # if the method was called directly then a string representing the table should be passed and we can just
            # directly place that table name in our string.
            primary_keys_names = {"Inventory": "item_id", "Employee": "emp_id", "Member": "member_id"}
            query = f"SELECT {primary_keys_names[table]} FROM {table};"
            return self._execute_sql_command(query)

    def assign_id(self, table: str):
        """Gets the next valid ID value for the specified table.

        Params:
            table (str): A string is the table we want to get an ID value for."""
        all_ids = self.get_all_ids(table)
        ids = {"Employee": self._emp_id, "Inventory": self._inv_id, "Member": self._mem_id}
        specified_id = ids[table]
        while specified_id in [this_id[0] for this_id in all_ids]:
            specified_id += 1
        return specified_id



if __name__ == "__main__":
    # allowing me to test behaviors
    s = Database()

    # testing that the edit works for the Employee table (works for this test)
    x = s.pass_to_database({"table": "Employee", "action": "view", "args":[]})
    print(x)
    s.pass_to_database({"table": "Employee", "action": "edit", "args": ["18", "APPLE JACK", "ceo", "joemama@gmail.com", "6161616762737", "2000000"]})
    y = s.pass_to_database({"table": "Employee", "action": "view", "args": ["s", "sds", "sdds"]})
    print(y)

    # testing that edit works for Inventory. (Works in this test)
    print(s.pass_to_database({"table": "Inventory", "action": "view", "args": []}))
    print(s.pass_to_database(({"table": "Inventory", "action": "edit", "args": ["11", "DROP BALL", "20", "26.99"]})))
    print(s.pass_to_database({"table": "Inventory", "action": "view", "args": []}))

    print(s.pass_to_database(({"table": "Inventory", "action": "edit", "args": ["13", "DROP TABLE Inventorysfdfdsfmnds fnmds fnm dnmsfnmdfnnf,n,dnf,nds;", "20", "26.99"]})))
    print(s.pass_to_database({"table": "Inventory", "action": "view", "args": []}))

    print(s.pass_to_database(({"table": "Inventory", "action": "add", "args": ["100", "YOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOMYOURMOM", "20", "26.99"]})))
    print(s.pass_to_database({"table": "Inventory", "action": "view", "args": []}))



