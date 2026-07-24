import sqlite3


def get_connection():
    conn = sqlite3.connect("incidents.db", check_same_thread=False)
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        category TEXT
    )
    """)

    # Add columns if they don't exist
    columns = [
        ("location", "TEXT"),
        ("incident_date", "TEXT"),
        ("incident_time", "TEXT"),
        ("reported_time", "TEXT"),
        ("status", "TEXT DEFAULT 'Pending'"),
        ("remarks", "TEXT")
    ]

    for column_name, column_type in columns:
        try:
            cursor.execute(f"ALTER TABLE incidents ADD COLUMN {column_name} {column_type}")
        except sqlite3.OperationalError:
            pass

    conn.commit()
    conn.close()


def add_incident(description, category, location,
                 incident_date, incident_time, reported_time):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO incidents(
        description,
        category,
        location,
        incident_date,
        incident_time,
        reported_time,
        status,
        remarks
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        description,
        category,
        location,
        incident_date,
        incident_time,
        reported_time,
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
        incident_date,
        incident_time,
        reported_time,
        status,
        remarks
    FROM incidents
    """)

    data = cursor.fetchall()

    conn.close()
    return data


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