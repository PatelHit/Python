#20CE083-Hit Patel
#https://github.com/PatelHit/Python/blob/main/practical2_tuple.py

# ::tuples::

# ---------------------->que-1: Write a Python program to create a tuple with different data types.<--------------------------
mytuple = ("name", 30, True, "city")
print(mytuple, type(mytuple)) #type() 

# ---------------------->que-2: Write a Python program to create a tuple with numbers and print one item.<--------------------------

tuple = (12, 4.5, 25)
print(tuple[1]) #print an item at index 1

# ---------------------->que-3: Write a Python program to add an item in a tuple.<--------------------------

thistuple = ("kiwi", "apple", "orange")
print(thistuple)
x = list(thistuple) #convert tuple into list to add an element
x.append("banana") #append() to add item 
thistuple = tuple(x) #convert list into tuple
print(thistuple)

# ---------------------->que-4: Write a Python program to convert a tuple to a string.<--------------------------

def coverttostring(tup):  #fun to convert tuple to string and it will return string
    str = ' '
    for item in tup:
        str = str+item #add all items to str var
    return str 


thistuple = ("a", "p", "p", "l", "e")
str = coverttostring(thistuple)
print(str)

# ---------------------->que-5: Write a Python program to find the length of a tuple.<--------------------------

thistuple = ("apple", "name", 12, 5.6)
print(len(thistuple)) #len() to find length of a tuple
