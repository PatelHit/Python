# ::tuples::

# ---------------------->que-1: Write a Python program to create a tuple with different data types.<--------------------------
mytuple = ("name", 30, True, "city")
print(mytuple, type(mytuple))

# ---------------------->que-2: Write a Python program to create a tuple with numbers and print one item.<--------------------------

tuple = (12, 4.5, 25)
print(tuple[1])

# ---------------------->que-3: Write a Python program to add an item in a tuple.<--------------------------

thistuple = ("kiwi", "apple", "orange")
print(thistuple)
x = list(thistuple)
x.append("banana")
thistuple = tuple(x)
print(thistuple)

# ---------------------->que-4: Write a Python program to convert a tuple to a string.<--------------------------

def coverttostring(tup):
    str = ' '
    for item in tup:
        str = str+item
    return str


thistuple = ("a", "p", "p", "l", "e")
str = coverttostring(thistuple)
print(str)

# ---------------------->que-5: Write a Python program to find the length of a tuple.<--------------------------

thistuple = ("apple", "name", 12, 5.6)
print(len(thistuple))
