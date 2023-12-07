
# Overview
This is our software requirements specification. It's purpose is to specify 
functional and non-functional behavior about our software. A requirement is 
a capability (functionality) or a condition (constraint) to which our 
software must conform to. Requirements are specifications of what should be 
implemented. They are descriptions of how the system (the Database, the 
Database.py and the GUI) and its 
attributes should behave.

# Artifact Links
[windows.PNG](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/windows.PNG)
[MacOS.png](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/MacOS.png)
[Linux(GNOME).png](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/Linux(GNOME).png)
[gui_progress.png](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/gui_progress.png)
[gui_progress2.png](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/gui_progress2.png)
[GUI_DB.jpg](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/use_case_diagrams/use_case_diagrams/GUI_DB.jpg)
[GUI_User_DB.jpg](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/use_case_diagrams/use_case_diagrams/GUI_User_DB.jpg)
[User_GUI.jpg](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/use_case_diagrams/use_case_diagrams/User_GUI.jpg)
[tasks_n_time](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/time_line_stuff/tasks_n_time)

# Software Requirements

Below you will find our functional software requirements first, and then below that you will find our non-functional requirements. There's 15 functional 
and 15 non-functional requirements making a total of 30 requirements. FR stands for functional requirement and NFR stands for non-functional 
requirement.

## Functional Requirements

### GUI's interactions with the database
| ID  | Requirement    |
| :-------------: | :----------:|
| FR1 | Execute: The pass_to_database function shall execute different actions  depending on the argument passed to the function. |
| FR2 | Delete data: the database.py shall delete the data at the specified ID passed as an argument to the pass_to_database function. |
| FR3 | Add data: The pass_to_database function shall add the data passed as an argument to the pass_to_database function. |
| FR4 | Edit Data: The database shall edit the data for a specified id number that's passed as an argument in the pass_to_database function. |
| FR5 | Format Data: The database will format the data passed as an argument to the pass_to_database_function so that it is in the correct format for the methods the database.py uses. |

### GUI Data Handling
| ID  | Requirement    |
| :-------------: | :----------:|
| FR6 | GUI shall populate the input fields with relevant data when editing/deleting/adding. |
| FR7 | When adding data, the GUI shall display the next ID the added data will be assigned.|
| FR8 | Viewing data shall only display selected table's data.|
| FR9 | The request shall not be processed until user hits submit request. |
| FR10 | The input fields shall be cleared when the add action is selected.|

| FR7 | When adding data, the GUI shall display the ID number that the added data will be assigned.|
| FR8 | Viewing data shall only display the selected table's data.|
| FR9 | The request shall not be processed until the user hits 'submit request'. |
| FR10 | The input fields shall be cleared when the 'add' action is selected.|

### Database.py Instantiation
| ID  | Requirement    |
| :-------------: | :----------:|
| FR11 | Databse.py shall check if the database already exists. |
| FR12 | Database.py shall construct the database if it does not exist. |
| FR13 | Database.py shall populate the database with the default data when constructing the database. |
| FR14 | Database.py shall load data from the database if it exists. |
| FR15 | Database.py shall title the database file T.A.L.A System Database. |

## Non-Functional Requirements

### Database.py behavior
| ID  | Requirement |
| :-------------: | :----------: |
| NFR1 | The database.py code will protect against SQL injections. |
| NFR2 | The database shall not allow for duplicate id numbers within individual tables. |
| NFR3 | For any action executed (add/delete/edit data), only the specified data shall be changed/added/removed. No other data rows in any of the other tables shall be affected. |
| NFR4 | The database shall save any changes made to it. |
| NFR5 | Database will be saved as an actual local file on user's computer. |

### GUI Layout
| ID  | Requirement |
| :-------------: | :----------: |
| NFR6 | All needed widgets shall be presented on user's screen. |
| NFR7 | The widgets shall not overlap. |
| NFR8 | The GUI main window shall handle all needed resizing. |
| NFR9 | The displayed input fields shall update based on the selected table. |
| NFR10 | The GUI updates shall not take longer than 5 seconds. |

### User Experience
| ID  | Requirement |
| :-------------: | :----------: |
| NFR11 | The GUI shall be compatible with Windows, MacOS, and Linux (GNOME). |
| NFR12 | All widgets shall be easily identifiable. |
| NFR13 | All text shall be clearly readable. |
| NFR14 | The GUI shall be intuitive to use. |
| NFR15 | The user shall only access the database through the provided GUI. |

