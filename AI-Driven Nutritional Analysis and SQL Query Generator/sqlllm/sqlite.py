import sqlite3

def create_student_table():
    """Create STUDENT table and insert initial records."""
    with sqlite3.connect('test.db') as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS STUDENT (
                NAME VARCHAR(255),
                CLASS VARCHAR(255),
                SECTION VARCHAR(255)
            );
        """)
        cur.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION) VALUES ('Raju', '7th', 'A')")
        cur.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION) VALUES ('Shyam', '8th', 'B')")
        cur.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION) VALUES ('Baburao', '9th', 'C')")
        conn.commit()
        
        print("Data Inserted in the table:")
        for row in cur.execute("SELECT * FROM STUDENT"):
            print(row)

if __name__ == "__main__":
    create_student_table()
