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
        pass

    # Add status column if it does not exist
    try:
        cursor.execute("ALTER TABLE incidents ADD COLUMN status TEXT DEFAULT 'Pending'")
    except sqlite3.OperationalError:
        pass

    # Add remarks column if it does not exist
    try:
        cursor.execute("ALTER TABLE incidents ADD COLUMN remarks TEXT")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()


def add_incident(description, category, location):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO incidents(description, category, location, status, remarks)
    VALUES (?, ?, ?, ?, ?)
    """, (
        description,
        category,
        location,
        "Pending",
        ""
    ))

    conn.commit()
    conn.close()


def get_incidents():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        description,
        category,
        location,
        status,
        remarks
    FROM incidents
    """)

    data = cursor.fetchall()

    conn.close()
    return data


# NEW FUNCTION - Update Status & Remarks
def update_incident_status(incident_id, status, remarks):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE incidents
    SET status=?, remarks=?
    WHERE id=?
    """, (status, remarks, incident_id))

    conn.commit()
    conn.close()