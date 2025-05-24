import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondb"
)
mycursor = db.cursor()

def register():
    username = input("Choose username: ")
    password = input("Choose password: ")
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    try:
        mycursor.execute(query, (username, password))
        db.commit()
        print(" Registered successfully.")
    except:
        print("Username already exists.")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    mycursor.execute(query, (username, password))
    result = mycursor.fetchone()
    return result is not None

def create_employee():
    name = input("Enter name: ")
    age = int(input("Enter Age: "))
    role = input("Enter new role (LIKE : HR , Finance , Backand , frontend  , Sales ...etc )  :   ")
    salary = float(input("Enter salary: "))
    query = "INSERT INTO ems(name, age, role, salary) VALUES (%s, %s, %s, %s)"
    mycursor.execute(query, (name, age, role, salary))
    db.commit()
    print(f"Thank you, {name}! Your entry has been recorded.")

def view_employees():
    query = "SELECT * FROM ems"
    mycursor.execute(query)
    result = mycursor.fetchall()

    if not result:
        print("No employees found.")
        return

    print("\n Employee List:")
    print("{:<10} {:<20} {:<10} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Role", "Salary"))
    print("-" * 70)

    for row in result:
        emp_id, name, age, role, salary = row
        print("{:<10} {:<20} {:<10} {:<15} {:<10}".format(emp_id, name, age, role, salary))


def update_employee():
    query = "SELECT * FROM ems"
    mycursor.execute(query)
    result = mycursor.fetchall()

    if not result:
        print("No employees found.")
        return

    print("\n Employee List:")
    print("{:<10} {:<20} {:<10} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Role", "Salary"))
    print("-" * 70)

    for row in result:
        emp_id, name, age, role, salary = row
        print("{:<10} {:<20} {:<10} {:<15} {:<10}".format(emp_id, name, age, role, salary))
    emp_id = int(input("Enter employee ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    role = input("Enter new role (LIKE : HR , Finance , Backand , frontend  , Sales ...etc )  : ")
    salary = float(input("Enter new salary: "))
    query = "UPDATE ems SET name=%s, age=%s, role=%s, salary=%s WHERE empid=%s"
    mycursor.execute(query, (name, age, role, salary, emp_id))
    db.commit()
    print(" Employee updated successfully.")

def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    query = "DELETE FROM ems WHERE empid=%s"
    mycursor.execute(query, (emp_id,))
    db.commit()
    print(" Employee deleted.")

def main_menu():
    while True:
        print("\n--- Employee Management ---")
        print("1. Create Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            update_employee()
        elif choice == 4:
            delete_employee()
        elif choice == 5:
            print("Thank you  for using this System ")
            break
        else:
            print(" Invalid choice. Try again.")

def start():
    print("=== Welcome to EMS System ===")
    print("1. Register")
    print("2. Login")
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        register()
        start()
    elif choice == 2  :
        if login():
            print(" Login successful.")
            main_menu()
        else:
            print(" Login failed. Try again.")
            start()
    else:
        print(" Invalid input.")

start()
