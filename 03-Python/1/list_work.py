# All lines starting with # are comments
# The following exercise shows how to manipulate List in python
#
#
# Lists are used to store multiple items in a single variable.
# They use [] square bracket to store elements. Elements are seperated by a comma
# List items are ordered, changeable, and allow duplicate values.
# The index/subscript number is used to identify each element
# The index number starts at 0 denoting the element located in first position

myList = ["Jacob", 25, "Ahmed", 80, 25]
print() # Print Blank line 
print(f"The Original List is {myList}")
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
# myList[0]  -> Jacob  (First element in the list)
# myList[1]  -> 25     (Second element in the list)
# myList[-1] -> 25     (Last element in the list)
print()


# Copy a list
newList = myList.copy()
print("Make a copy of the myList to newList")
print(f"The new list is {newList}")
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
print()


#Reverse a list. Reversed list is a permanent change
newList.reverse()
print("reverse of newList:",newList )
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
print()


# Adds an element onto the end of a List
myList.append("Matt")
print("Append a new element Matt:",myList)
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
print()


# Returns the index of the first object with a matching value
print(f"The index position of element Matt is: {myList.index("Matt")}")
print("Remember, the index starts at zero")
print() # Print Blank line
print("-------------------------------------") # Print Line of ----
print()

# Get Elements 2,3,4 from the list
print(myList[2:5])
print("Get Elements located on index 2,3,4 from the list")
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
print()
# Get the last element from the list
print(myList[-1])
print("Get the last element from the list")
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
print()
# Get the 2nd last element from the list
print(myList[-2])
print("Get the 2nd last element from the list")
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
print()

# Changes a specified element within an List at the given index
myList[3] = 85
print("Change the value of index 3 to 85")
print("List After Change:",myList)
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
print()

# To determine how many items a list has, use the len() function
print(f"Number of Elements : {len(myList)}")
print("-------------------------------------") # Print Line of ----
print()


# Removes a specified object from an List by value
myList.remove("Matt")
print("List after removing Matt:",myList)
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
print()

# Removes the object at the index specified
myList.pop(0)
print("After removing 1 elements from the beginning:", myList)
print()
print("-------------------------------------") # Print Line of ----
print()

# Insert an element at 2nd location (remember, the index starts from 0)
myList.insert(1,"Sandra") 
print(f"After Inserting element 'Sandra' at location index #1: {myList}")
print("-------------------------------------") # Print Line of ----
print()

#Print element at a particular location
print(f"The element at index 1 :  {myList[1]}")
print()
print("-------------------------------------") # Print Line of ----
print()

# Count an element's occurance
print("Count the occurance of element 25 in the list:", myList.count(25))
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----


# Join 2 Lists and make one big list
print("Join 2 Lists and make one big list")
list1=["jack","amy","kate"]
list2 = ["max","rami","fred"]
list3 = list1 + list2
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"Join list1 and list2 to make list3: {list3}")
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----

# Sort List in reverse order
list3.sort(reverse=True)
print(f"list3 Sorted in reverse order:, {list3}")
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----


# Get a random element from the list
import random
print("Random element from list3:",random.choice(list3))
print()


# Tuples are used to store multiple items in a single variable.
# They use () round bracket to store elements. Elements are seperated by a comma
# A tuple is a collection which is ordered and unchangeable.
# Tuple has only 2 methods available to manipulate them count() and index()
myTuple = ('Python', 100, 'VBA', False)
print("Tuple:",myTuple)
print() # Print Blank line 
print("-------------------------------------") # Print Line of ----
