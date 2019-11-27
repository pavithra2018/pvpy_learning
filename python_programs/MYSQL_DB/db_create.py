import mysql.connector as mysql

db_conn = mysql.connect(
            host    = "localhost",
            user    = "root",
            passwd  = "welcome123"
          )
cursor = db_conn.cursor()

## Create a Database named 'learner' if it is not present
cursor.execute("CREATE DATABASE IF NOT EXISTS delete_this;")
## Show the databases using SQL
cursor.execute("SHOW DATABASES;")

## Fetch all and print the databases one by one
print("The databases available")
databases = cursor.fetchall()
for db in databases:
    print(db)

print("Using 'delete_this' database")
cursor.execute("USE delete_this;")
print("Listing tables in the database")
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
print( tables)


