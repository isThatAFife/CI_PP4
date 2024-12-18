import psycopg2
from psycopg2 import sql

try:
    # Establishing the connection
    connection = psycopg2.connect(
        database="postgresql://neondb_owner:6viqIRPgmh8y@ep-tight-dew-a25ojf2o.eu-central-1.aws.neon.tech/keg_come_rut_654270",  # Replace with your database name
        user="dylank",  # Replace with your username
        password="C14ru5M3d1a",  # Replace with your password
        host="localhost",  # Replace with your host (e.g., localhost)
        port="5432",  # Default PostgreSQL port
    )

    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Executing a SQL query
    cursor.execute(
        "SELECT * FROM gamelibrary_game WHERE metascore = 'tbd';"
    )  # Replace with your table name

    # Fetching all results from the executed query
    records = cursor.fetchall()

    # Printing fetched results
    for row in records:
        print(row)

except Exception as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()  # Closing the cursor
        connection.close()  # Closing the connection
        print("PostgreSQL connection closed.")
