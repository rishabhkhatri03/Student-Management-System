import psycopg2

def create_table():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Rishabh21",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key,name text,address text,age int,number text);")
    print("Student table created")
    conn.commit()
    conn.close()
    
def insert_data():
    # code to accept data from user
    name = input("Enter name:")
    address = input("Enter Address:")
    age = input("Enter age:")
    number = input("Enter number:")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Rishabh21",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("insert into students(name,address,age,number) values(%s,%s,%s,%s)",(name,address,age,number))
    print("Data inserted")
    conn.commit()
    conn.close()
    
def delete_data():
    student_id = input("Enter id of the student to be updated")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Rishabh21",host="localhost",port="5432")
    cur = conn.cursor()
    
    
    cur.execute("select * from students where student_id= %s",(student_id,))
    student = cur.fetchone()
    
    if student:
        print(f"Student to be deleted: ID {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Number: {student[4]}")
        choice = input("Are you sure you want to delete the student? (yes/no)")
        if choice.lower() == "yes":
            cur.execute("delete from students where student_id=%s", (student_id,))
            print("student record deleted")
        else:
            print("Deletion cancelled")
    else:
        print("student not found")
    conn.commit()
    conn.close()
def update_data():
    student_id = input("Enter id of the student to be updated")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Rishabh21",host="localhost",port="5432")
    cur = conn.cursor()
    fields = {
        "1":("name","Enter name"),
        "2":("address","Enter address"),
        "3":("age","Enter age"),
        "4":("number","Enter number"),
    }
    # name = input("Enter name:")
    # address = input("Enter Address:")
    # age = input("Enter age:")
    # number = input("Enter number:")
    print("Which field you would like to update")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice = input("Enter the number of the field ypu want to update: ")
    if field_choice in fields:
        field_name, promt = fields[field_choice]
        new_value = input(promt)
        sql = f"update students set {field_name}=%s where student_id=%s"
        cur.execute(sql,(new_value,student_id))
        print(f"{field_name} updated successfully")
    else:
        print("Invalid choice")
        
    conn.commit()
    conn.close()

def read_data():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Rishabh21",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("select * from students;")
    students = cur.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Number: {student[4]}")
    conn.close()

while True:
    print("\n Welcome to the student database management system")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice=="1":
        create_table()
    elif choice=="2":
        insert_data()
    elif choice=="3":
        read_data()
    elif choice=="4":
        update_data()
    elif choice=="5":
        delete_data()
    elif choice=="6":
        break
    else:
        print("Invalid choice")