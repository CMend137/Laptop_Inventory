import sqlite3 

conn = sqlite3.connect("database.db")
cursor =  conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS rooms (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               room_number TEXT UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS laptops (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               model TEXT NOT NULL,
               serial_number TEXT UNIQUE NOT NULL,
               status TEXT CHECK(status IN ('Available', 'Assigned', 'Needs Repair')) DEFAULT 'Available'
               
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_id INTEGER,
               laptop_id INTEGER, 
               assigned_date TEXT,
               FOREIGN KEY(room_id) REFERENCES rooms(id),
               FOREIGN KEY(laptop_id) REFERENCES laptops(id)           
               
               )               
               """)
conn.commit()
conn.close()

print("Database and tables have been created successfully.")

#Functions 
def add_room(room_number):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO rooms (room_number) VALUES (?)", (room_number,))
        conn.commit()
        print(f"Room {room_number} added successfully!")
    except sqlite3.IntegrityError:
        print(f"Room {room_number} already exists!")
    
    conn.close()

def add_laptop(model, serial_number, status="Available"):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO laptops (model, serial_number, status) VALUES (?, ?, ?)", 
                       (model, serial_number, status))
        conn.commit()
        print(f"Laptop {serial_number} ({model}) added successfully!")
    except sqlite3.IntegrityError:
        print(f"Laptop with Serial Number {serial_number} already exists!")
    
    conn.close()

# 🔥 Add room1 without department names
add_room("MM100")
add_room("MM102")
add_room("MM103")

# 🔥 Add some laptops
add_laptop("Dell Loaner 1", "SN9TLR")
add_laptop("Dell Loaner 2", "SN8YLQ")
add_laptop("Dell Loaner 3", "SNGWLQ")
