import sqlite3 as sq
class Database:

    def __init__(self):
        self.query = None

    def edit_row(self):
        pass

    def add_row(self):
        pass

    def delete_row(self):
        pass

    # receive inputs from GUI and store the passed information in the instance variables and format the correct
    # SQL command
    def pass_to_database(self, query: str,):
        pass

    def format_sql_command(self, query: str):
        pass

    # use command line format to execute the different sql commands.
    # So a dictionary with pointers to the methods will be needed.
    def execute_command(self):
        pass

    def create_table(self, str: str):
        """
        Creates the items database table

        Params:
            str: A string that represents what table we would like to make. This argument
                should only ever be employee or items
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


