print("Python Sequence Types")
print("1) Lists") # ordered, indexed, mutable collection of items.
numbers : list = [3,6,9,12,15,18]
# access elements using index starting from 0, negative indexing starts from -1
print(numbers[2])
print(numbers[-2])
# modifying lists using index
numbers[3] = 14
print(numbers)
# list slicing
new_numbers : list = numbers[2:4]
new_numbers1 : list = numbers[2:]
print(new_numbers)
print(new_numbers1)
# adding elements
numbers : list = [3,6,9,12,15,18,12]
numbers.append("twenty-one") # adds one element
numbers.extend(["twenty-four","twenty-seven","thirty"]) # adds multiple elements
print(numbers)
# removing elements
numbers.remove(12) # value based - deletes the first occurence of a given value
print(numbers)
deleted = numbers.pop(5) # index based - deletes the element at given index and returns the deleted element
print(numbers)
print(deleted)
# sorting of a list
numbers : list = [6,3,27,12,21,18]
numbers.sort() # sorting in ascending order
print(numbers)
numbers.sort(reverse=True) # sorting in descending order
print(numbers)
numbers.reverse() # sorting in reverse order
print(numbers)
names : list = ["Ahmed","Ghazanfar","Gul","Shazy"]
names.sort(key=len) # sorting by length
print(names)

print("\n List Comprehension") # for creating new lists, useful for filtering unwanted data
names : list = ["Ahmed","Ghazanfar","Gul","Shazy"]
new_names : list = ["Mr " + name for name in names if len(name) == 5] 
print(new_names)

print("\n 2) Tuples") # ordered, indexed, immutable collection of items, items can't be deleted, added or modified.
# tuples are faster than lists due to memory efficiency
names : tuple = ("Ahmed","Ghazanfar","Gul","Shazy")
print(names[2]) # accessing element using index
print(names[0:2]) # tuple slicing using index
print(len(names)) # tuple length
for name in names : # iterating through a tuple
    print("Mr", name)
new_names : tuple = ("Ismail","Junaid","Hadi Bux","Azhar")
total_names : tuple = names + new_names # concatenating tuples
print(total_names)
nested_names : tuple = (names , new_names) # nested tuples
print(nested_names)
a,b,c,d = new_names # unpacking tuple
print(a,b,c,d)
print(new_names.count("Junaid")) # finding counts of an element
print(new_names.index("Hadi Bux")) # finding index of an element

print("\n 3) Dictionary") # ordered, mutable, un-indexed collection of key-value pairs
bioData : dict = dict(name = "Shahab", age = 29, city = "Jamshoro")
print(bioData)
print(bioData["age"]) # accessing value associated with the key using square bracket, key-error if not found
print(bioData.get("age", 30)) # accessing value associated with the key using get() method with default value - does'nt raise error
bioData["e-mail"]= "shahab@example.com" # adding  new key value pair - mutable
bioData["city"]= "Hyderabad" # modifying key value pair - mutable
print(bioData)
del bioData["e-mail"] # deleting a key value pair using "del" keyword - does'nt return the deleted value
age : int = bioData.pop("age", 30) # deleting a key value pair using pop() method with default value - returns the deleted value
print("deleted value age:", age)
print(bioData)
print(len(bioData)) # returns the length of dictionary
# Dictionary methods
# keys()	Returns a list of all keys in the dictionary.	
# values()	Returns a list of all values in the dictionary.	
# items()	Returns a list of key-value pairs as tuples.	
# clear()	Removes all items from the dictionary.	
# update()	Adds or updates multiple key-value pairs from another dictionary.
print("All keys:",bioData.keys())
print("All value:",bioData.values())
print("All key-value pairs:",bioData.items())
print("Updating & adding a new key-value pair:",bioData.update({"city":"Jamshoro", "e-mail":"shahab@example.com"}))
print(bioData)
# print("Clearing all key-value pairs:",bioData.clear())
# print(bioData)
bioData = {'name': 'Shahab', 'city': 'Jamshoro', 'e-mail': 'shahab@example.com', 'city': 'Hyderabad'}
# Duplicate keys not allowed - it will overwrite the previous one
print(bioData)

print("Iterating over a dictionary")
for key in bioData :
    print(key)
for key, value in bioData.items() :
    print(key, ":", value)
# searching in dictionary
contacts : dict = {"Shahab": 12345, "Ismail":1234567, "Junaid":9090909}
name : str = str(input("Enter your name : "))
if name in contacts :
    print("Name included in dictionary !", name)
else :
    print("Sorry, name is'nt in dictionary !")

print("Dictionary Comprehension")
marks : dict = {"Shahab": 70, "Ismail":76, "Junaid":82}
print(marks)
new_marks : dict = {k : v - 7 for k,v in marks.items()}
print(new_marks)