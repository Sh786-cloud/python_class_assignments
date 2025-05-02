print(" The Set ") # A mutable, un-ordered, un-indexed collection of unique and immutable (un-exchangeable) elements.
# You can't modify the elements however you can add or remove the elements.
# The curly braces or set () function can be used to create a set.
#   Used to eliminate the duplicate enteries.
my_set : set = {12, 3, 27, 35, "d"} # elements are un-ordered - elements are stored based on their hash values.
my_set1 : set = set([12, 3, 27, 35, "d"])
my_set2 : set = set((12, 3, 27, 35, "d"))
my_set3 : set = {} # this will create an empty dictionary - use set() function for empty set.

print("my_set : ",my_set,type(my_set))
print("my_set1 : ",my_set1,type(my_set1))
print("my_set2 : ",my_set2,type(my_set2))
print("my_set3 : ",my_set3,type(my_set3))

my_set.add("e") # adds one new element
print(my_set)
my_set.update({"f","g","h"}) # add multiple new elements
print(my_set)
#pop_my_set = my_set.pop() # removes and returns the arbitrary element
#print(pop_my_set)
my_set.remove("h") # removes one given element - raises key-error if not found, use when you want to handle error.
print(my_set)
my_set.discard("g") # removes one element-doesn't raise error if not found, use when you don't want to handle error.
print(my_set)
my_set.difference_update({"h","g"}) # removes multiple elements - doesn't raise error if not found
print(my_set)

my_set4 : set = my_set.union({"l","m","n"}) # it combines two sets into single set, union() takes an iterable.
print(my_set4)
my_set : set = {122, 3, 27, 335, "d"}
my_set5 : set = my_set.union(my_set4)
print(my_set5)
my_new_set : set = {203, 405, 128}
my_set6 : set = my_set | my_new_set # it also combines two sets into single set.
print(my_set6)

print("\n Set Methods")
my_set : set = {10, 15, "n", 20, 25, "d"}
my_set1 : set = {30, 25, "d", 20, 35, "s"}

print("1) set difference :", my_set.difference(my_set1))
print(my_set)
print("2) difference_update :", my_set.difference_update(my_set1))
print(my_set)
my_set : set = {10, 15, "n", 20, 25, "d"} # reset set
print("3) symmetric_difference :", my_set.symmetric_difference(my_set1))
print(my_set)
print("4) symmetric_difference_update :", my_set.symmetric_difference_update(my_set1))
print(my_set)
my_set : set = {10, 15, "n", 20, 25, "d"} # reset set
print("5) union :", my_set.union(my_set1))
print(my_set)
print("6) intersection :", my_set.intersection(my_set1))
print(my_set)
print("7) intersection_update :", my_set.intersection_update(my_set1))
print(my_set)
my_set : set = {10, 15, "n", 20, 25, "d"} # reset set
print("8) set disjoint :", my_set.isdisjoint(my_set1))
print(my_set)
print("9) subset :", my_set.issubset(my_set1))
print(my_set)
print("10) superset :", my_set.issuperset(my_set1))
print(my_set)

print("\n The Frozenset")# An immutable, hashable, un-ordered, un-indexed collection of unique and immutable (un-exchangeable) elements.
# "Hashable" means frozensets can be used as a key in dictionaries.
# "Thread-safe" means frozensets can be safely accessed from multiple threads.
# frozenset() constructor is used to create a frozenset - it takes an iterable
my_frozen : frozenset = frozenset([1,2,3,4,5,6])
my_frozen1 : frozenset = frozenset((1,2,3,4,5,6,7))
my_frozen2 : frozenset = frozenset({1,2,3,4,5,6,7,8})
my_frozen3 : frozenset = frozenset(my_frozen)

print("my_frozen :", my_frozen)
print("my_frozen1 :", my_frozen1)
print("my_frozen2 :", my_frozen2)
print("my_frozen3 :", my_frozen3)

print("\n Frozenset Methods")
my_set : frozenset = frozenset({1,2,3,4,5})
my_set1 : frozenset = frozenset({3,5,6,7,8})

print("1) frozenset difference :", my_set.difference(my_set1))
print(my_set)
print("2) symmetric_difference :", my_set.symmetric_difference(my_set1))
print(my_set)
print("3) union :", my_set.union(my_set1))
print(my_set)
print("4) intersection :", my_set.intersection(my_set1))
print(my_set)
print("5) frozenset disjoint :", my_set.isdisjoint(my_set1))
print(my_set)
print("6) subset :", my_set.issubset(my_set1))
print(my_set)
print("7) superset :", my_set.issuperset(my_set1))
print(my_set)