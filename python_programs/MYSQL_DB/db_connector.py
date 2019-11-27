import mysql.connector as mysql

db_conn = mysql.connect(
            host    = "localhost",
            user    = "root",
            passwd  = "welcome123"
          )
cursor = db_conn.cursor()
cursor.execute("SHOW DATABASES;")
## Fetch all and print the databases one by one
print("The databases available are:")
for db in cursor:
    print(db)



