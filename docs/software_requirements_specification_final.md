# Overview
This is our software requirements specification. It's purpose is to specify 
functional and non-functional behavior about our software. A requirement is 
a capability (functionality) or a condition (constraint) to which our 
software must conform to. Requirements are specifications of what should 
be 
implemented. They are descriptions of how the system (the Database, the 
Database.py and the GUI) and its 
attributes should behave.



## Functional Requirements

### GUI's interactions with the database
| ID  | Requirement    |
| :-------------: | :---------- |
| FR1 | Execute: The pass_to_database function shall execute different actions  depending on the argument passed to the function. |
| FR2 | Delete data: the database.py shall delete the data at the specified ID passed as an argument to the pass_to_database function. |
| FR3 | Add data: The pass_to_database function shall add the data passed as an argument to the pass_to_database function. |
| FR4 | Edit Data: The database sall edit the data for a specified id number that's passed as an argument in the pass_to_database function. |
| FR5 | Format Data: The database will format the data passed as an argument to the pass_to_database_function so that it's in the correct format for the methods the database.py uses. |

## Non-Functional Requirements

### Database.py behavior
| ID  | Requirement |
| :-------------: | :---------- |
| NFR1 | The database.py code will protect against SQL injections |
| NFR2 | The database shall not allow for duplicate id numbers within individual tables |
| NFR3 | For any action executed (add/delete/edit data), only the specified data shall be changed/added/removed. No other data rows in any of the other tables shall be affected. |
| NFR4 | The database shall save any changes made to it. |
| NFR5 | Database will be saved as an actual local file on users laptop |

# Functional Requirements
### GUI Reqs
 1. FRG1: The GUI shall allow the user to submit a request to the database.
 2. FRG2: The GUI shall allow the user to view the results of their requests.
 3. FRG3: The GUI shall display a staus message based on the result of the 
request.
 4. FRG4: The GUI shall allow the user to save their changes.

## Database Reqs
 1. FRD1: Database shall construct SQL queries.
 2. FRD2: Database shall not directly use GUI arguments to execute SQL commands
 3. FRD3: Database shall create 3 tables and initialize them with the correct data upon instantiation of a Database object.
 4. FRD4: User shall be able to add items to inventory table.
 5. FRD5: User shall be able to add people to employee table.
 6. FRD6: User shall be able to add people to customer table.
 7. FRD7: The database shall read its data from a file.
 8. FRD8: The database shall write its data to a file.
 9. FRD
 
# Non-Functional Requirements
### GUI Reqs
 1. NFRG1: The GUI windows shall remain a fixed size.
 2. NFRG2: Buttons on the GUI shall be easily identifiable.
 3. NFRG3: The user shall only access the database through the provided GUI.
 4. NFRG4: The GUI text shall be clearly readable.
 5. NFRG5: The GUI shall be intuitive to use.
 6. NFRG6: The GUI shall not have delays longer than 5 seconds.
 7. NFRG7: The user shall be aware of what the program does.
 8. NFRG8: The GUI shall be compatible with Windows, MacOS, and Linux.
### Database Reqs
 1. NFRD1: User shall not be able to drop tables.
 2. NFRD2: User shall not be able to modify columns.
 3. NFRD3: The user's query shall be validated before being processed.
 4. NFRD4: The user shall not need prior SQL knowledge.
