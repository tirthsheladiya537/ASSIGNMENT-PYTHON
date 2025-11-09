# Employee Management System (EMS)
# Step 1: Plan the Data Storage
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}
# Step 2: Define the Menu System
def main_menu():
    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                add_employee()
            elif choice == 2:
                view_employees()
            elif choice == 3:
                search_employee()
            elif choice == 4:
                print("Thank you for using the Employee Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
# Step 3: Add Employee Functionality
def add_employee():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Employee ID already exists. Please enter a unique ID.")
                continue
            break
        except ValueError:
            print("Invalid Employee ID. Please enter a valid integer.")
    
    name = input("Enter Employee Name: ").strip()
    while True:
        try:
            age = int(input("Enter Employee Age: "))
            break
        except ValueError:
            print("Invalid Age. Please enter a valid integer.")
    
    department = input("Enter Employee Department: ").strip()
    while True:
        try:
            salary = float(input("Enter Employee Salary: "))
            break
        except ValueError:
            print("Invalid Salary. Please enter a valid number.")
    
    # Store the employee data
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"Employee {name} (ID: {emp_id}) added successfully!")
# Step 4: View All Employees
def view_employees():
    if not employees:
        print("No employees available.")
        return
    
    # Print header
    print("\nEmployee Details:")
    print("-" * 70)
    print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Department':<15} {'Salary':<10}")
    print("-" * 70)
    
    # Print each employee
    for emp_id, details in employees.items():
        print(f"{emp_id:<5} {details['name']:<15} {details['age']:<5} {details['department']:<15} {details['salary']:<10}")
    print("-" * 70)
# Step 5: Search for an Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Invalid Employee ID. Please enter a valid integer.")
        return
    
    if emp_id in employees:
        details = employees[emp_id]
    print("\nEmployee Details:")
    print("-" * 70)
    print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Department':<15} {'Salary':<10}")
    print("-" * 70)
    
    # Print each employee
    for emp_id, details in employees.items():
        print(f"{emp_id:<5} {details['name']:<15} {details['age']:<5} {details['department']:<15} {details['salary']:<10}")
    print("-" * 70)
# Step 5: Search for an Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Invalid Employee ID. Please enter a valid integer.")
        return
    
    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nEmployee Found:")
        print(f"ID: {emp_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    else:
        print("Employee not found.")
# Step 6: Exit the Program (handled in main_menu)
# Run the program
if __name__ == "__main__":
    main_menu()
