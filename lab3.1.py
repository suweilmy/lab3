employees = {}

while True:
    name = input("Enter employee name: ")
    if name.lower() == 'no':
        break
    salary = float(input("Enter employee salary: "))
    employees[name] = salary

print(employees)