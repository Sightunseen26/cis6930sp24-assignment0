import sqlite3
import os

def createdb():
    # Ensure the resources directory exists
    if not os.path.exists('resources'):
        os.makedirs('resources')

    db_path = 'resources/normanpd.db'
    
    # Connect to the database file or create it if it doesn't exist
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            incident_time TEXT,
            incident_number TEXT,
            incident_location TEXT,z
            nature TEXT,
            incident_ori TEXT
        )
    ''')
    db.commit()
    return db

def populatedb(db, incidents):
    cursor = db.cursor()
    for incident in incidents:
        cursor.execute('''
            INSERT INTO incidents VALUES (?, ?, ?, ?, ?)
        ''', incident)
    db.commit()

def status(db):
    cursor = db.cursor()
    cursor.execute('''
        SELECT COALESCE(nature, ''), COUNT(*) as count
        FROM incidents
        GROUP BY COALESCE(nature, '')
        ORDER BY count DESC, COALESCE(nature, '')
    ''')
    for row in cursor.fetchall():
        print(f'{row[0]}|{row[1]}')
