import sqlite3

def create_sqliteDB_table():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('playstore.db')
    cursor = conn.cursor()

    # Create a table to store the app details
    sql ='''CREATE TABLE IF NOT EXISTS app_details(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        package_name CHAR(500),
        title CHAR(500),
        developer CHAR(500),
        score FLOAT,
        reviews FLOAT,
        ratings FLOAT,
        genre CHAR(500),
        icon CHAR(500)
    )'''

    cursor.execute(sql)
    print("Table created successfully........")

    conn.commit()
    conn.close()
