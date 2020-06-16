## About

I tried to decouple as much as possible. I'm not super happy how it's done now, as many things can be simplified/unified, but within given timeframe it's all I can do for now :)


All the 'backend' is inside project/backed/ folder:

~~~~
./backend/keyboard_input.py     # just takes in the input from the console
~~~~
~~~~
./backend/serialization.py      # reads in the sqlite3 database and spits out what's inside
                                # works fine with a single table. Not tested vs multiple
                                # as you can see every method is a bit different
                                # this should be unified
                                # for output files look into:
                                    ./output/
~~~~
~~~~
./backend/sqliteStuff.py        # all the sqlite3 stuff and the core base of the project
                                # !!! calling SQLite() will return a different path for
                                # the sqlite3 database, dependable on where you call it !!!
~~~~
~~~~
./backend/table.py              # the table for sqlite3
~~~~

## Unit Testing

To run unit tests just run the python file with tests:
~~~~
py unit_tests.py                # Tests run vs methods in sqliteStuff.py
                                # Tests use different temporary database,
                                # so nothing is overwritten
~~~~
