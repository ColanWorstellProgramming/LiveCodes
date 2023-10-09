#!/usr/bin/env python3
"""Imports"""
import mysql.connector


def MySQL():
    """Create a Database Using MySQL"""

    # Replace these values with your MySQL server configuration
    host = "localhost"
    user = "debian-sys-maint"
    password = "oi6emFdFIuHiZGbM"
    database = "example_db"

    # Create a connection to the MySQL server
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Create the database if it doesn't exist
        print("Task : Add Data To Table\n")

        create_db_query = f"CREATE DATABASE IF NOT EXISTS {database}"
        cursor.execute(create_db_query)

        # Switch to the database
        cursor.execute(f"USE {database}")

        # Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255)
        )
        """

        cursor.execute(create_table_query)

        # Insert some dummy data
        insert_data_query = """
        INSERT INTO customers (name, email) VALUES (%s, %s)
        """
        dummy_data = [
            ("John Doe", "john@example.com"),
            ("Jane Smith", "jane@example.com"),
            ("Bob Johnson", "bob@example.com")
        ]

        cursor.executemany(insert_data_query, dummy_data)

        # Commit changes to the database
        conn.commit()

        # Select and print some information
        select_query = "SELECT name, email FROM customers"
        cursor.execute(select_query)
        for (name, email) in cursor:
            print(f"Name: {name}, Email: {email}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection in the finally block
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("\nMySQL connection is closed\n---------------------------------------\n")


def remove_all_records_from_table():
    try:
        # Create a connection to the MySQL server
        conn = mysql.connector.connect(
            host = "localhost",
            user = "debian-sys-maint",
            password = "oi6emFdFIuHiZGbM",
            database = "example_db"
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Build the DELETE query to remove all records from the specified table
        print("Task : Remove Data From Table\n")
        delete_query = f"DELETE FROM customers"

        # Execute the DELETE query to remove all records
        cursor.execute(delete_query)

        # Commit the changes to the database
        conn.commit()
        print(f"All records removed from customers.\n")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection in the finally block
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection is closed\n")
