import sqlite3

def create_db():
    conn = sqlite3.connect("esc2.db")
    cur = conn.cursor()
    
    # Create register table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS register (
            FNAME TEXT,
            LNAME TEXT,
            CONTACT TEXT,
            USERNAME TEXT PRIMARY KEY,
            SECURITY_Q TEXT,
            SECURITY_A TEXT,
            PASSWORD TEXT
        )
    """)
    
    # Create emp_salary2 table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS emp_salary2 (
            e_code TEXT PRIMARY KEY,
            e_name TEXT,
            e_gender TEXT,
            Designation TEXT,
            Contact TEXT,
            Email TEXT,
            "D.O.B" TEXT,
            "D.O.J" TEXT,
            Month TEXT,
            Year TEXT,
            Salary TEXT,
            "Working days" TEXT,
            Absent TEXT,
            Medical TEXT,
            Incentive TEXT,
            "net salary" TEXT,
            salary_receipt TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_db()
