import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = None #Initialize conn to None

try:
   #establishing the connection
   conn = psycopg2.connect(
      database="postgres", user='postgres', password='12345', host='172.17.0.1', port= '5432'
   )
   conn.autocommit = True
   conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

   #Creating a cursor object using the cursor() method
   cursor = conn.cursor()

   #Preparing query to create a database
   dbname = 'inman'
   username = 'inman'
   password = 'inman'
   create_db_sql = f"""CREATE database {dbname};
            """
   #Creating a database
   cursor.execute(create_db_sql)

   # Creating a user and granting privileges
   create_user_sql = f"""
      CREATE USER {username} WITH ENCRYPTED PASSWORD '{password}';
      GRANT ALL PRIVILEGES ON DATABASE {dbname} TO {username};
   """
   cursor.execute(create_user_sql)

   print("Database created successfully........")

except psycopg2.OperationalError as e:
    print("Unable to connect to the database.")
    print(e)
finally:
    if conn:
        # Closing the connection
        conn.close()