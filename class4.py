# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("\n")
# Using Get Function
g = dictionary.get("model")
print("Get Function: ", g)

# Using Keys Function
k = dictionary.keys()
print("Keys Function: ", k)

# Using Values Function
v = dictionary.values()
print("Values Function: ", v)

# Using Items Function
i = dictionary.items()
print("Items Function: ", i)

# Adding Items To The Dictionary
dictionary['price'] = "50 Lac"
print("After Adding New Items: ", dictionary)

# Adding Items Using Updates Method
dictionary.update({"color": "red"})
print("After Adding New Item Using Update Func: ", dictionary)

# Updating the Existing Items
dictionary.update({"color": "green"})
print("After Updating Existing Item Using Update Func: ", dictionary)

# Remove items Using POP 
dictionary.pop("color")
print("Items After Poping Color: ", dictionary)

# Remove items Using Popitem
dictionary.popitem()
print("After Poping Item: ", dictionary)

# Conditional Statements
new_dict = {
    "category" : "Student Information"
}
print("\nNew Dictionary:",new_dict,"\nUpdate Student Information")

name = input("Enter Full Name: ")
if isinstance(name, str) == False: 
    print("Invalid Input")

print("\n")
