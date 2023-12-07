# Overview

This is our software requirements specification. Its purpose is to specify functional and non-functional behavior about our software. A requirement is a capability (functionality) or a condition (constraint) to which our software must conform to. Requirements are specifications of what should be implemented and descriptions of how the system (the Database, Database.py, and the GUI) and its attributes should behave.

# Software Requirements

Below you will find our functional software requirements first, and then below that you will find our non-functional requirements. There are 15 functional and 15 non-functional requirements for a total of 30 requirements. FR stands for functional requirement and NFR stands for non-functional requirement in the IDs.

## Functional Requirements

### GUI interactions with Database.py

| ID | Requirement |
| :-------------: | :----------:|
| FR1 | The pass_to_database function shall execute different actions depending on the argument passed to the function. |
| FR2 | When deleting, database.py shall delete the data at the specified ID passed as an argument to the pass_to_database function. |
| FR3 | When adding, database.py shall add the data passed as an argument to the pass_to_database function. |
| FR4 | When editing, database.py shall edit the data for the specified ID passed as an argument to the pass_to_database function. |
| FR5 | Database.py shall format the data passed as arguments to the pass_to_database_function to match its internal expectations. |

### GUI Data Handling

| ID | Requirement |
| :-------------: | :----------:|
| FR6 | The GUI shall populate the input fields with relevant data when editing/deleting. |
| FR7 | When adding data, the GUI shall display the ID number that the added data will be assigned. |
| FR8 | Viewing data shall only display the selected tables data. |
| FR9 | The request shall not be processed until the user hits the "Submit request button. |
| FR10 | The input fields shall be cleared when the "Add" action is selected. |
 
### Database.py Instantiation

| ID | Requirement |
| :-------------: | :----------:|
| FR11 | Database.py shall check if the database already exists. |
| FR12 | Database.py shall construct the database if it does not exist. |
| FR13 | Database.py shall populate the database with the default data when constructing the database. |
| FR14 | Database.py shall load data from the database if it exists. |
| FR15 | Database.py shall name the database file "T.A.L.A System Database". |

## Non-Functional Requirements

### Database.py behavior

| ID | Requirement |
| :-------------: | :----------: |
| NFR1 | The database.py code shall protect against SQL injections. |
| NFR2 | The database shall not allow for duplicate ID numbers within individual tables. |
| NFR3 | For any action executed (add/delete/edit data), only the specified data and table shall be affected. |
| NFR4 | The database shall save any changes made to it. |
| NFR5 | The database file shall be saved locally in the ./data directory. |

### GUI Layout

| ID | Requirement |
| :-------------: | :----------: |
| NFR6 | All needed widgets shall be presented on the screen. |
| NFR7 | The widgets shall not overlap. |
| NFR8 | The main GUI window shall handle all needed resizing. |
| NFR9 | The displayed input fields shall update based on the selected table and action. |
| NFR10 | The GUI updates shall not take longer than 5 seconds. |

### User Experience

| ID | Requirement |
| :-------------: | :----------: |
| NFR11 | The GUI shall be compatible with Windows, MacOS, and Linux (GNOME). |
| NFR12 | All widgets shall be easily identifiable. |
| NFR13 | All text shall be clearly readable. |
| NFR14 | The GUI shall be intuitive to use. |
| NFR15 | The user shall only access the database through the provided GUI. |

# Software Artifacts

Below are links to all produced artifacts for this project. They are: images of what the GUI looks like on a given OS, images of previous GUI implementations, images of use-case diagrams from the planning phase, or the proposed task checklist/timeline.

[windows.PNG](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/windows.PNG)

[MacOS.png](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/MacOS.png)

[Linux(GNOME).png](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/Linux(GNOME).png)

[gui_progress.png](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/gui_progress.png)

[gui_progress2.png](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/gui_progress2.png)

[GUI_DB.jpg](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/use_case_diagrams/use_case_diagrams/GUI_DB.jpg)

[GUI_User_DB.jpg](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/use_case_diagrams/use_case_diagrams/GUI_User_DB.jpg)

[User_GUI.jpg](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/use_case_diagrams/use_case_diagrams/User_GUI.jpg)

[tasks_n_time](https://github.com/anthonyboos559/GVSU-CIS350-T.A.L.A-Systems/blob/main/artifacts/time_line_stuff/tasks_n_time)
