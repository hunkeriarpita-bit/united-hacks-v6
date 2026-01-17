import sqlite3

def create_db():
    # Database se judna (Ye resources.db file apne aap bana dega)
    conn = sqlite3.connect('databasek/resources.db')
    cursor = conn.cursor()

    # Pehle purani table hatao taaki naya data dhal sake
    cursor.execute('DROP TABLE IF EXISTS resources')
    
    # Nayi Table banana
    cursor.execute('''CREATE TABLE resources 
                     (city TEXT, type TEXT, name TEXT, contact TEXT)''')

    # Hackathon ke liye "Real" sample data
    # Format: ('City Name', 'Emergency Type', 'Place Name', 'Phone Number')
    data = [
        # MUMBAI DATA
        ('Mumbai', 'Medical', 'Nanavati Max Hospital', '022-26267500'),
        ('Mumbai', 'Medical', 'SevenHills Hospital', '022-67676767'),
        ('Mumbai', 'Fire', 'Andheri Fire Station', '101'),
        ('Mumbai', 'Fire', 'Borivali Fire Station', '022-28051646'),
        
        # DELHI DATA
        ('Delhi', 'Medical', 'AIIMS Delhi', '011-26588500'),
        ('Delhi', 'Medical', 'Max Super Speciality', '011-26515050'),
        ('Delhi', 'Fire', 'Delhi Fire Service HQ', '101'),
        
        # PUNE DATA
        ('Pune', 'Medical', 'Ruby Hall Clinic', '020-66455100'),
        ('Pune', 'Fire', 'Pune Central Fire Dept', '020-26451707')
    ]
    
    # Saara data ek saath database mein dalna
    cursor.executemany('INSERT INTO resources VALUES (?,?,?,?)', data)
    
    conn.commit() # Data save karna
    conn.close()  # Connection band karna
    print("✅ Database successfully updated with real contacts!")

if __name__ == '__main__':
    create_db()