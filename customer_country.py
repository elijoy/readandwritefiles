import csv

customers = open('customers.csv', 'r')

customer_file = csv.reader(customers, delimiter = ',')


#how to make a new file
outfile = open('customer_country.csv', 'w')

counter = 0
outfile.write("FirstName,LastName,Country" + '\n')

next(customer_file)
for record in customer_file:
    outfile.write(record[1] + ',' + record[2] + ',' + record[4] + '\n')
    counter += 1
    
print(counter)

