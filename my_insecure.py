import sqlite3

# Setting up a simple in-memory database for demonstration purposes
def setup_database():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    # Insert some sample data
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'securepassword')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'mypassword')")
    connection.commit()
    return connection

# Insecure SQL Query Execution
def insecure_lookup(connection, username):
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # INSECURE QUERY
    print(f"Executing Query: {query}")
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"Found User: ID={row[0]}, Username={row[1]}, Password={row[2]}")
        else:
            print("No user found.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

def main():
    print("Insecure SQL Lookup Demo")
    connection = setup_database()
    
    # User input
    username = input("Enter a username to search: ")
    
    # Perform insecure SQL lookup
    insecure_lookup(connection, username)

if __name__ == "__main__":
    main()