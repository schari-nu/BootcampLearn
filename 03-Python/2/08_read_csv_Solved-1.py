# First we'll import the os module
# This will allow us to create file paths across operating systems
# https://www.w3schools.com/python/module_os.asp

import os

# Module for reading CSV files
import csv
print(f"Current dir: {os.getcwd()}")
print()

#csvpath = os.path.join('/Users/schari/Desktop/LearnPython/Assignment2/Resources/', 'contacts.csv')
csvpath = os.path.join('..', 'Resources', 'contacts.csv')


# # Method 1: Plain Reading of CSV files like a text file
with open(csvpath, 'r') as file_handler:
     lines = file_handler.read()
     print(lines)
     print(type(lines))


# Method 2: Improved Reading using CSV module with delimiter

with open(csvpath) as csvfile: 

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print the reference to a file stream
    print(f"Reference Address to the file stream: {csvreader}")   
    print("===================")
    print()
    # Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        print(row)
 
