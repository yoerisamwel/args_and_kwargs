def create_employee(**kwargs):
    employee = {
        "name": kwargs.get('name', 'John Joe'),
        'age': kwargs.get('age',30),
        'position': kwargs.get('position','Employee'),
        'salary': kwargs.get('salary',50000.0),
        'department': kwargs.get('department', 'General'),
    }
    return employee

def display_employee_info(employee):
    print(f"Name: {employee['name']}")
    print(f"Age: {employee['age']}")
    print(f"Position: {employee['position']}")
    print(f"Salary: {employee['salary']}")
    print(f"Department: {employee['department']}")

if __name__=='__main__':
    # create employee using **kwargs
    employee1 = create_employee(name="Alice", position="Manager", salary=75000.0)
    # Display employee information
    display_employee_info(employee1)

    employee2 = create_employee(name="Bob", position="Manager", salary=75000.0)
