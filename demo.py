import pandas as pd
from sqlalchemy import create_engine





import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# Function to import data from CSV into SQLite
def import_csv_to_sqlite(csv_file_path, sqlite_db_path):
    # Create a SQLAlchemy engine for SQLite
    engine = create_engine(f'sqlite:///{sqlite_db_path}')

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Import the data into the "Tour" table (create it if it doesn't exist)
    df.to_sql('Tour', con=engine, if_exists='replace', index=False)

    print(f"Data imported successfully into '{sqlite_db_path}' database, table 'Tour'.")

# Function to check and display data from SQLite database
def check_data_in_db(sqlite_db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db_path)
    cursor = conn.cursor()

    # Query to fetch all data from the 'Tour' table
    cursor.execute("SELECT * FROM Tour")

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Print the data
    print("\nData in 'Tour' table:")
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

# Main function
def main():
    # Path to your CSV file and SQLite database
    # csv_file_path = 'tour_data.csv'  # Update with your CSV file path
    # sqlite_db_path = 'my_database.db'  # Update with your SQLite database path
    sqlite_db_path = 'C:/Users/RAG/OneDrive/Desktop/flyandfeel/db.sqlite3'
    csv_file_path = "C:/Users/RAG/Downloads/accounts_tour_202501242120.csv"

    # Step 1: Import data from CSV to SQLite
    import_csv_to_sqlite(csv_file_path, sqlite_db_path)

    # Step 2: Check and display data in the 'Tour' table
    check_data_in_db(sqlite_db_path)

if __name__ == "__main__":
    main()
