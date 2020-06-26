import sqlite3

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS tbl_persons(id Integer Primary Key Autoincrement, \
        col_fname Text, col_lname Text, col_email Text)"
    )
    conn.commit()
conn.close()

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    cur.execute(
        "Insert Into tbl_persons(col_fname, col_lname, col_email) Values (?, ?, ?) \
                    ",
        ("Sarah", "Jones", "sjones@gmail.com"),
    )
    cur.execute(
        "Insert Into tbl_persons(col_fname, col_lname, col_email) Values (?, ?, ?) \
                    ",
        ("Sally", "May", "sallymay@gmail.com"),
    )
    cur.execute(
        "Insert Into tbl_persons(col_fname, col_lname, col_email) Values (?, ?, ?) \
                    ",
        ("Kevin", "Bacon", "kbacon@rocketmail.com"),
    )
    conn.commit()
conn.close()

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    cur.execute(
        'Select col_fname, col_lname, col_email From tbl_persons Where col_fname = "Sarah"'
    )
    var_person = cur.fetchall()
    for item in var_person:
        msg = "First Name: {}\nLastName: {}\nEmail: {}".format(
            item[0], item[1], item[2]
        )
    print(msg)
conn.close()
