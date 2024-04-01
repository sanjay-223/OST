import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="31415",database="students")
cursor = db.cursor()

def selectall():
    cursor.execute("Select * from details")
    entries = cursor.fetchall()
    print('Roll, Name, Gender, CGPA, Mail, Phone')
    for e in entries:
        print(*e)
def insert(data):
    cmd = "INSERT INTO details (roll, name, gender, cgpa, mail, phone) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(cmd,data)
    db.commit()
    print("inserted Successfully")

selectall()
data = input('''Enter data to be inserted in the following order 
             (roll, name, gender, cgpa, mail, phone)
 > ''').split(',')
insert(data)
selectall()