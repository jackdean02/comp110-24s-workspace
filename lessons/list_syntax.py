"""Demonstrate Basic List Syntax"""

# Initialize an empty list
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] #<- literal

print(grocery_list)

# Add itme to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# Create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list: ")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

# Indexing
print("Print first element of string")
print(grocery_list[0])

# Modifying by Index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change: ")
print(grocery_list)

# Measuring length
print("Length of list: ")
print(len(grocery_list))

# Removing an item
grocery_list.pop(1)
print("After removing almond milk:")
print(grocery_list)

# Function name: Display
# Parameter: list[str]
# Return Nothing!
# Print out the list!

def display(word: list[str]) -> None:
    print(word)

display(grocery_list)
x = display(["Alyssa", "Erin", "Will"])
print(x)

# Create a list!
# Name: create
# Parameters: str and str
# RV: list[str]
# Put both parameters into list and return that list

def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

print(create("Hello", "World"))