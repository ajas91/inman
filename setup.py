import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='12345', host='127.0.0.1', port= '5433'
)
conn.autocommit = True

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
dbname = 'inman'
username = 'inman'
password = 'inman'
sql = f"""CREATE database {dbname};
          """
#Creating a database
cursor.execute(sql)
cursor.execute(f"""
         create user {username} with encrypted password '{password}';
         grant all privileges on database {dbname} to {username};"""
         )
print("Database created successfully........")

#Closing the connection
conn.close()