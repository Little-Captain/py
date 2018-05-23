import sqlite3
import sys

db_filename = 'mydatabase.db'
inid = sys.argv[1]
innat = sys.argv[2]

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

query = "update person set nationality = :nat where id = :id"
cursor.execute(query, {'id':inid, 'nat':innat})

cursor.execute("select id, name, dob,nationality,gender from person")
for row in cursor.fetchall():
    id, name, dob, nationality, gender = row
    print("%3d %15s %12s %10s %6s" % (id, name, dob, nationality, gender))