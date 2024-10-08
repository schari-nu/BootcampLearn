import csv
import os

# Three Lists
indexes = ["1", "2", "3", "4"]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

print(f"Index: {indexes}")
print(f"Employees: {employees}")
print(f"Department: {department}")
print()
print("-" * 50)
# Zip all three lists together into tuples
roster = zip(indexes, employees, department)

# Print the contents of each row
for employee in roster:
    print(employee)
print()
print("-" * 50)
# save the output file path
print("Saving the data in output.csv file")

output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Index", "Employee", "Department"])
    #writer.writerows(zip(indexes, employees, department))
    writer.writerows(roster)

