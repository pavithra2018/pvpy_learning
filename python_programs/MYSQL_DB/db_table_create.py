import mysql.connector as mysql

db_conn = mysql.connect(
            host    = "localhost",
            user    = "root",
            passwd  = "welcome123"
          )
cursor = db_conn.cursor()

## Create a Database named 'learner' if it is not present
cursor.execute("CREATE DATABASE IF NOT EXISTS learner;")
## Show the databases using SQL
cursor.execute("SHOW DATABASES;")

## Fetch all and print the databases one by one
print("INFO: The databases available are as below:")
databases = cursor.fetchall()
for db in databases:
    print(db)

print("INFO: Switching to 'learner' dabatase")
cursor.execute("USE learner;")
print("INFO: Dropping existing table with name 'books'")
cursor.execute("DROP TABLE IF EXISTS books;")
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

print("Listing tables in the database")
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
print( tables)
print("INFO: Showing the schema of the table created")
cursor.execute("DESCRIBE books;")
print(cursor.fetchall())

