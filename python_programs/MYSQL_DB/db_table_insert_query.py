import mysql.connector as mysql

def create_table_in_database( db_conn, cursor):
    cursor.execute("DROP TABLE IF EXISTS books")
    print("INFO: Creating a new table 'books'")
    cursor.execute("CREATE TABLE books (\
                            id              INT(11) NOT NULL AUTO_INCREMENT, \
                            title           VARCHAR(255) NOT NULL, \
                            author          VARCHAR(255) NOT NULL, \
                            price           FLOAT(10,2), \
                            language        VARCHAR(25), \
                            PRIMARY KEY (id), \
                            CONSTRAINT uc_id_title UNIQUE(id, title))" 
                  )
    print("INFO: Showing the schema of the table created")
    cursor.execute("DESCRIBE books;")
    print(cursor.fetchall())
    print("INFO: Inserting data in to table")
    table_sql_cmd = "INSERT INTO books(title, author, price, language) VALUES(%s, %s, %s, %s)"
    table_values  = [
                ("Word Power Made Easy","Lewis Norman", "125.0", "English"),
                ("The Alchemist", "Paulo Coelho", "99.99", "English"),
                ("Kanya Shulkam", "Sri Sri", '180.0', "Telugu"),
                ("Python Programming", "Bhaskara", "999.00", "English")
            ]
    cursor.executemany(table_sql_cmd, table_values)
    db_conn.commit()
    print( cursor.rowcount, "records inserted.")
    print("INFO: Displaying the records added to the table")
    query = "SELECT * FROM books ORDER BY title;"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print( record)

if __name__ == '__main__':
    db_conn = mysql.connect(
            host    = "localhost",
            user    = "root",
            passwd  = "welcome123",
            database = 'learner'
          )
    cursor = db_conn.cursor()

    create_table_in_database( db_conn, cursor)


