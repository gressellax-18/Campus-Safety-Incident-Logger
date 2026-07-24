import sqlite3

def get_connection():
    conn = sqlite3.connect("incidents.db", check_same_thread=False)
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        category TEXT
    )
    """)

    # Add location column if it does not exist
    try:
        cursor.execute("ALTER TABLE incidents ADD COLUMN location TEXT")
    except sqlite3.OperationalError:
        # Column already exists
        pass

    conn.commit()
    conn.close()


def add_incident(description, category, location):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO incidents(description, category, location)
    VALUES (?, ?, ?)
    """, (description, category, location))

    conn.commit()
    conn.close()


def get_incidents():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, description, category, location
    FROM incidents
    """)

    data = cursor.fetchall()

    conn.close()
    return data
