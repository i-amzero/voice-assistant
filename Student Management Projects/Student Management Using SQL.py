import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        username="root",
        password="Rawat12345",
        database="student_db"
    )
    cursor = connection.cursor()
    print("*" * 10, "WELCOME TO STUDENT MANAGEMENT SYSTEM", "*" * 10)

    while True:
        print("\n1. VIEW TABLE\n2. ENTER RECORD\n3. DELETE RECORD ")
        cmd = int(input("\nChoose any option: "))

        if cmd == 1:
            cursor.execute("SELECT * FROM student_detail")
            res = cursor.fetchall()
            for value in res:
                print(value)

            more_entries = input("\nMore Queries:\n'y' for Yes or 'n' for No: ")
            if more_entries.lower() in ['y', 'yes']:
                continue
            else:
                break

        elif cmd == 2:
            name = input("Enter name: ")
            roll_no = input("Enter roll id: ")
            contact = input("Enter Phone number: ")
            addr = input("Enter city and state: ")

            sql_que = "INSERT INTO student_detail(name,id,contact,address) VALUES (%s,%s,%s,%s)"
            val = (name, roll_no, contact, addr)
            cursor.execute(sql_que, val)
            connection.commit()
            print(cursor.rowcount, "record(s) inserted")
            more_entries = input("\nMore Queries:\n'y' for Yes or 'n' for No: ")
            if more_entries.lower() in ['y', 'yes']:
                continue
            else:
                break

        elif cmd == 3:
            sql_que = "DELETE FROM student_detail WHERE name = %s"
            name = input("Enter name you want to delete:")
            cursor.execute(sql_que, (name,))
            connection.commit()
            print(cursor.rowcount, "record(s) deleted")
            more_entries = input("\nMore Queries:\n'y' for Yes or 'n' for No: ")
            if more_entries.lower() in ['y', 'yes']:
                continue
            else:
                break

except mysql.connector.Error as e:
    print("Something went wrong:", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
 