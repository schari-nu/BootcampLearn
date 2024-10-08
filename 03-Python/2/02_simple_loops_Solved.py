# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
print("Number Range 0-10 [not including]")
for x in range(10):
    print(x)
print("=" * 50)
print()

# If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
print("Number range 20 - 50 [not including] Step 10")
for x in range(20, 50, 10):
    print(x)
print("=" * 50)
print()

# If a list is provided, then the For loop will loop through each element within the list
words = ["Peanut", "Butter", "Jelly", "Time", "Is", "Now"]
for word in words:
    print(word)
print("=" * 50)
print()

# Break  a sentence into a list using split()
myString = "Oh happy days!"
print(f"Original String : {myString}")

#Split the tring and make a list
mywords = myString.split(" ")

print(f"MyString to List: {mywords}")
for myword in mywords:
    print(myword)
print("=" * 50)
print()
# A While Loop will continue to loop through the code contained within it until some condition is met
x = "Yes"
while x == "Yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again [Yes/No? ")
