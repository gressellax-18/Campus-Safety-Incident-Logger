import sqlite3


# -----------------------------
# Database Connection
# -----------------------------
def get_connection():
    return sqlite3.connect(
        "incidents.db",
        check_same_thread=False
    )


# -----------------------------
# Create Table
# -----------------------------
def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        category TEXT,
        location TEXT,
        incident_date TEXT,
        incident_time TEXT,
        reported_time TEXT,
        status TEXT DEFAULT 'Pending',
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Add Incident
# -----------------------------
def add_incident(
    description,
    category,
    location,
    incident_date,
    incident_time,
    reported_time
):

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


# -----------------------------
# Get All Incidents
# -----------------------------
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
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


# -----------------------------
# Update Status
# -----------------------------
def update_incident_status(
    incident_id,
    status,
    remarks
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE incidents
    SET
        status=?,
        remarks=?
    WHERE id=?
    """, (
        status,
        remarks,
        incident_id
    ))

    conn.commit()
    conn.close()


# -----------------------------
# Dashboard Statistics
# -----------------------------
def get_statistics():

    reports = get_incidents()

    total = len(reports)

    resolved = sum(
        1 for report in reports
        if report[7] == "Resolved"
    )

    pending = total - resolved

    return {
        "total": total,
        "resolved": resolved,
        "pending": pending
    }