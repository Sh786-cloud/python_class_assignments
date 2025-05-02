# CONTROL FLOW - Order in which the program is executed, achieved by "if, elif and else statements".
print("1) The if statement") # used to execute a block of code if the condition is true.
a : str = "artificial"
if a == "artificial":
    print("If statement executed!")

print("\n 2) The else statement") # used to execute a block of code if the if condition is false.
a : str = "artificial"
if a == "natural":
    print("If statement executed!")
else :
    print("Else statement executed!")

print("\n 3) The elif statement") # used to execute a block of code if the if condition is false.
# Used to check multiple conditions, stands for else-if.
x : int = 16
if x > 20 :
    print("x is greater than 20 !")
elif x % 4 == 0 :
    print("x is divisible by 4 !")
else :
    print("x is not divisible by 4 !")

print("\n Nested If statements") #if statements can be nested inside other if statements to check multiple conditions.
y : int = 60
if y % 2 == 0 :
    if y % 3 == 0 :
        print("y is an even number and divisible by both 2 and 3.")
    else :
        print("y is an even number.")
else :
    print("y is an odd number.")

print("\n Python match-case statement") # alternative to if-elif-else chain, introduced in python 3.10
y : int = 60
match y :
    case 50 :
        print("y is equal to 10 * 5.")
    case 60 :
        print("y is equal to 10 * 6.")
    case _ :
        print("y is unknown.")

print("\n Python loops and iteration") # used to execute a block of code multiple times.
print("for loop") # it executes a block of code for each item, used to iterate over a  sequence like lists, tuple, string and range.
# iterates over a list
vegetables : list = ["cabbage", "lady-finger", "carrot"]
for vegetable in vegetables :
    print(vegetable)
# iterates over a string
fruit : str = "Watermelon"
for fruit in fruit :
    print(fruit)

# For loop with else - else statement executes only if the loop is completed without break statement.
operators : list = ["Babar", "Shahab", "Junaid"]
for operator in operators :
    print(operator)
else :
    print("Loop completed successfully !")

# Print odd numbers from 3 to 11
for numb in range(3,12,2) :
    print(numb)

print("\n while loop") # it executes a block of code as long as the condition is true
count : int = 6
while count > 0 :
    print(f"The number is {count}.")
    count -= 1

print("\n Controlling Loops")
# 1) break - it breaks/exits the loop immediately
avg_score_list : list = [45, 69, 75, 87, 101, 124]
for score in avg_score_list :
    if score > 100 :
        break
    else :
        print(f"The score was {score}.")
else :
    print("Loop completed!")
# 2) continue - skips the rest of the code in current iteration and jumps to the next iteration
for score in avg_score_list :
    if score == 87 :
        continue
    print(f"The score was {score}.")
        
else :
    print("Loop completed!")

print("\n Nested Loops")
for i in range(2,5) :
    print(f"Multiplication table for {i}")
    for numb in range(1,11) :
        print(f"{i}*{numb}= ", i*numb)
