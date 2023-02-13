'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

infile = open('employee_data.csv', 'r', newline = '')
reader = csv.reader(infile)
fields = next(reader)

#create an empty dictionary
emp_list = []
emp_dict = {}

#use a loop to iterate through the csv file

for row in reader:
     if row[3] == 'Marketing':
        emp_list.append(row[1])
        emp_list.append(row[2])
        emp_list.append(row[5])
        for emp in emp_list: 
            full_name = row[1] + row[2]
            emp_dict[full_name] = row[5]



    #check if the employee fits the search criteria

for row in reader:
    if row[3] == 'Marketing':
        print('Manager name: ', row[1], row[2], 'Salary: ', row[5])

    

print()
print('=========================================')
print()

for emp in emp_dict:
    emp_dict[emp] = float(emp_dict[emp]) * 1.10
    for k,j in emp_dict.items():
        print('Manager Name: ', k, 'Salary: ', j )

#iternate through the dictionary and print out the key and value as per printout



          
        

        
    
