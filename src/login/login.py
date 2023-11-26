import json
import sys
import os

def read_user_credentials():
    try:
        with open('api/json/login.json', 'r') as user_file:
            return json.load(user_file)
    except FileNotFoundError:
        print("File not found: api/json/login.json")
        return None

def get_user_input():
    if not sys.stdin.isatty():
        # Running in non-interactive mode (e.g., Docker)
        print("Non-interactive mode: Using environment variables if available.")
        username = os.getenv("DOCKER_USERNAME", "default_username")
        password = os.getenv("DOCKER_PASSWORD", "default_password")
        return username, password

    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def login():
    username, password = get_user_input()

    if username == "default_username" and password == "default_password":
        print("Using default credentials.")
    else:
        print(f"Entered username: {username}")
        print(f"Entered password: {password}")

    user_credentials = read_user_credentials()

    if user_credentials:
        if user_credentials['login']['username'] == username and user_credentials['login']['password'] == password:
            print("Login successful")
        else:
            print("Login failed. Check your username and password.")
    else:
        print("Cannot perform login due to missing credentials.")
