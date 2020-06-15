# Table
sql_create_personal_details_table = """ CREATE TABLE IF NOT EXISTS personal_details (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            address text NOT NULL,
                                            phone_number text NOT NULL
                                        ); """