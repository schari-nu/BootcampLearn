x = 1
y = 11

# Checks if one value is equal to another
if x == 1:
    print("x is equal to 1")
    print("===============")
print("It is not equal to 10")
if y != 1:
    print("y is not equal to 1")
if x < y:
    print("x is less than y")

# Checks if one value is greater than another
if y > x:
    print("y is greater than x")
if x >= 1:
    print("x is greater than or equal to 1")
# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")

if x == 1 or y == 10:
    print("One of the  values returned true")

# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")

