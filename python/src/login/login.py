import psycopg2
from psycopg2 import sql

# Replace these with your PostgreSQL credentials
DB_NAME = 'mydatabase'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Function to create the users table if not exists
def create_users_table(conn):
    with conn.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL
            )
        ''')
    conn.commit()

# Function to add a new user
def add_user(conn, username, password):
    with conn.cursor() as cursor:
        cursor.execute(
            sql.SQL("INSERT INTO users (username, password) VALUES ({}, {})")
            .format(sql.Literal(username), sql.Literal(password))
        )
    conn.commit()

# Function to authenticate a user
def authenticate_user(conn, username, password):
    with conn.cursor() as cursor:
        cursor.execute(
            sql.SQL("SELECT * FROM users WHERE username = {} AND password = {}")
            .format(sql.Literal(username), sql.Literal(password))
        )
        user = cursor.fetchone()

    return user

# login function
def login():
    conn = None  # Initialize conn to None
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        # Create the users table if not exists
        create_users_table(conn)

        # Example: Add a user
        add_user(conn, 'admin', 'admin')

        # Example: Authenticate a user
        authenticated_user = authenticate_user(conn, 'admin', 'admin')

        if authenticated_user:
            print(f"User {authenticated_user[1]} authenticated.")
        else:
            print("Authentication failed.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if conn is not None:
            conn.close()

