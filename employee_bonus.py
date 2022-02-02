import csv

employee = open('EmployeePay.csv','r')

employee_file = csv.reader(employee, delimiter = ',' )

next(employee_file)


for record in employee_file:
    salary = int(record[3])
    bonus = float(record[4])
    
    print("First Name: ", record[1])
    print("Last Name: ", record[2])
    print("Salary: $", format(salary, ',.2f'), sep='')
    print('Bonus Amount: $', format(salary * bonus, ',.2f'),sep='')

    calc_total = salary + (salary * bonus)
    print('Total Pay: $', format(calc_total, ',.2f'),sep='')
    
    input()