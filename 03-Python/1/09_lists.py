# Create a variable and set it as an List
myList = ["Jacob", 25, "Ahmed", 80, 25]
print("Original List:",myList)
print()

# Copy a list
newList = myList.copy()

#Reverse a list 
newList.reverse()
print("reverse:",newList )
print()

# Adds an element onto the end of a List
myList.append("Matt")
print("Added Matt:",myList)
print()

# Returns the index of the first object with a matching value
print(myList.index("Matt"))


# Changes a specified element within an List at the given index
myList[3] = 85
print("List After Change:",myList)
print()

# Returns the length of the List
print("Len:",len(myList))
print()

# Removes a specified object from an List
myList.remove("Matt")
print("List after removing Matt:",myList)
print()
print()

# Removes the object at the index specified
myList.pop(0)
myList.pop(1)
print("After removing 2 elements from the beginning:", myList)
print()

# Insert to an existing list
myList.insert(1,["this","is","inside","list"]) 
print(f"myList after insert to 2nd location: {myList}")
print()
print("Inside List",myList[1])
print()
print("Element of Sub List:",myList[1][1])
print()

print()
print()
# Count an element's occurance
print("Count:", myList.count(25))

list1=["jack","amy","kate"]
list2 = ["max","rami","fred"]
list3 = list1 + list2

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")

print()
print()
list3.sort(reverse=True)
print(f"list3 Sorted:, {list3}")
print()
# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ('Python', 100, 'VBA', False)
print("Tuple:",myTuple)

import random
print("Random:",random.choice(list3))