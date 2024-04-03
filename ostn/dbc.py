import mysql.connector

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS last (
                        reg_number INT PRIMARY KEY,
                        gender VARCHAR(10),
                        age INT,
                        email VARCHAR(255),
                        phone_number VARCHAR(20),
                        cgpa FLOAT
                    )''')
    print("Table 'last' created successfully.")

def insert_student(cursor, reg_number, gender, age, email, phone_number, cgpa):
    cursor.execute('''INSERT INTO last (reg_number, gender, age, email, phone_number, cgpa)
                      VALUES (%s, %s, %s, %s, %s, %s)''', (reg_number, gender, age, email, phone_number, cgpa))

def fetch_all_students(cursor):
    cursor.execute("SELECT * FROM last")
    rows = cursor.fetchall()
    return rows

def main():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="787898",
        database="last"
    )

    cursor = conn.cursor()
    
    # Create the table if it does not exist
    create_table(cursor)

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            reg_number = int(input("Enter registration number: "))
            gender = input("Enter gender: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            cgpa = float(input("Enter CGPA: "))
            insert_student(cursor, reg_number, gender, age, email, phone_number, cgpa)
            conn.commit()
            print("Student added successfully!")
        elif choice == '2':
            students = fetch_all_students(cursor)
            print("\nStudents in the database:")
            for student in students:
                print(student)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
