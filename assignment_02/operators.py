# ARITHMATIC OPERATORS - These operators perform basic mathematical operations.
print("i) ARITHMATIC OPERATORS")
# i) Addition " + " : 
a : int = 7
b : int = 23
c = a + b
print("Addition result  c = ", c, type(c))
# ii)   Subtraction " - " :
d : int = 7
e : int = 23
f = e - d
print("Subtraction result  f = ", f, type(f))
# iii)   Multiplication " * " :
g : int = 5
h : int = 4
i = g * h
print("Multiplication result  i = ", i, type(i))
# iv)   Division (Float) " / " :
j : int = 7
k : int = 23
l = k / j
print("Float Division result  l = ", l, type(l))
# v)   Floor Division " // " :
m : int = 7
n : int = 23
o = n // m
print("Floor Division result  o = ", o, type(o))
# vi)   Modulus " % " :
p : int = 7
q : int = 23
r = q % p
print("Modulus result  r = ", r, type(r))
# vii)   Exponentiation " ** " :
s : int = 6
t : int = 3
u = s ** t
print("Exponentiation result  u = ", u, type(u))

# ASSIGNMENT OPERATORS - They assign values to variables.
print("\n ii) ASSIGNMENT OPERATORS")
# i) " = "
x = 15
print("Value of x = ", x, type(x))
# ii) " += "
x += 3
print("Value of x after \"+=\" = ", x, type(x))
# iii) " -= "
x -= 3
print("Value of x after \"-=\" = ", x, type(x))
# iv) " *= "
x *= 3
print("Value of x after \"*=\" = ", x, type(x))
# v) " /= "
x /= 3
print("Value of x after \"/=\" = ", x, type(x))
# vi) " //= "
x //= 6
print("Value of x after \"//=\" = ", x, type(x))

# COMPARISION OPERATORS - They are used to compare two values, return true or false.
print("\n iii) COMPARISION OPERATORS")
# i) Equal to " == "
x = 32
y = 27
print(x == y)
# ii) Not equal to " != "
print(x != y)
# iii) Greater than " > "
print(x > y)
# iv) Less than " < "
print(x < y)
# v) Greater than or equal to " >= "
print(x >= y)
# vi) Less than or equal to " <= "
print(x <= y)

# LOGICAL OPERATORS - They are used to combine conditional statements.
print("\n iv) LOGICAL OPERATORS")
# i) Logical AND "and"
a = 10
b = 7
c = 13
print(a > b and c > a)
# i) Logical OR "or"
print(a > b or c < a)
# i) Logical NOT "not"
print(not c > a)

# IDENTITY OPERATORS - They are used to compare memory locations, return true or false.
print("\n v) IDENTITY OPERATORS")
a = [1, 2, 3, 5]
b = [1, 2, 3, 5]
c = a
# i) " is "
print("c is a: ", c is a)
print("a is c: ", a is c)
print("a is b: ", a is b)
print("a == b: ", a == b)
print("c is b: ", c is b)
print("c == b: ", c == b)
print("id of a : ", id(a))
print("id of b : ", id(b))
print("id of c : ", id(c))
# ii) " is not "
print("c is not a: ", c is not a)
print("a is not c: ", a is not c)
print("a is not b: ", a is not b)

# MEMBERSHIP OPERATORS - They are used to check if a value is in a sequence (list, tuple. dictionary, set etc)
print("\n vi) MEMBERSHIP OPERATORS")
# i) " in "
a : tuple = ("Gul", "Ahmed", "Osama")
b : str = "Palestine"
print("Ahmed" in a)
print("AHMED" in a)
print("t" in b)
# ii) " not in "
a : list = [3, 6, 9, 12, 15]
print(7 not in a)
print(12 not in a)

# BITWISE OPERATORS
print("\n vii) BITWISE OPERATORS")
# i) AND " & "
print(6 & 3)
print(bin(6))
print(bin(3))
# ii) OR " | "
print(6 | 3)
# iii) XOR " ^ "
print(6 ^ 3)
# iv) NOT " ~ "
print( ~3 )
# v) Zero fill left shift " << "
print( 3 << 2 )
# vi) Signed right shift " >> "
print( 8 >> 2 )