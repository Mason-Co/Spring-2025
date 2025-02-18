# Programmer: Mason Colacicco
# Date: February
# Program: Tech Time

import sqlite3 as lite
import sys

# Use the conn connector to connect SQLite to the techTime database
conn = lite.connect('techTime.db')

with conn:
    # Create a cursor
    cur = conn.cursor()

    # Insert a new row specifically with PK as 4
    cur.execute('INSERT INTO employee VALUES ("4", "3", "Corrie", "ten Boom", "Roseville", "MN", "4/15/2024")')
    # Execute the SQL SELECT statement to retrieve rows from employee
    cur.execute("SELECT * FROM employee")

    # Fetchall method retrieves all rows in the table
    rows = cur.fetchall()
    # Loop through the rows that were selected; print each row
    for row in rows:
        print(row)
    print()

    cur.execute('UPDATE employee SET city = "Shoreview" WHERE emp_id = "3"')
    cur.execute('SELECT * FROM employee')

    rows = cur.fetchall()

    for row in rows:
        print(row)
    print()

    cur.execute('DELETE FROM employee WHERE emp_id = "4"')

    cur.execute('SELECT * FROM employee')

    rows = cur.fetchall()
    for row in rows:
        print(row)

# Close the connector
conn.close()