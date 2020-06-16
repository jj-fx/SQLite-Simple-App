### **How to run:**
1) clone the project
2) make virtualenv and install **requirements.txt**
3) I was using Python 3.8.2, but it should run on any 3+

#### ***WARNING***

Project was done on Windows, so some commands may be different

---

#### Using API

~~~~
py api.py --help
~~~~
Displays help for the api. You should start with:
~~~~
py api.py --makedb True
~~~~
Will create an empty sqlite3 database with a single table. Database 'animal.db' is created within root project folder
~~~~
py api.py --add X
~~~~
Where X stands for number of records you would like to add. Default table takes (name, address, phone_number)

Once you have some records, you can filter with:
~~~~
py api.py --filter TEXT
~~~~
Where TEXT is a glob pattern.

###### note: Does not test vs upper/lower cases

###### note: Api filters only 'name'. However the functionality to filter different columns is there

You can display the records with:
~~~~
py api.py --display True
~~~~
Records are displayed with primary key (id). So if you like you can remove the ones with ID:
~~~~
py api.py --remove ID
~~~~


#### Additional functionality:
- Serialization / Output files into project parent directory ./output/
~~~~
py api.py --output 1    # csv file
py api.py --output 2    # txt file
py api.py --output 3    # html file
~~~~
- Outside of the api you can run unit tests with:
~~~~
py unit_tests.py
~~~~