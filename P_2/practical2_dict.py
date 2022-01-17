# 20CE083-Hit Patel
#https://github.com/PatelHit/Python/blob/main/practical2_dict.py

# ::dictionary::
d1 = {
    "a": "apple",
    "b": "banana",
    "g": "grapes",
    "s": "strawberry"
}
d2 = {
    "c": "cat",
    "d": "dog",
    "e": "elephant",
    "f": "fish"
}

# ---------------------->que-1: Write a Python script to check whether a given key already exists in a dictionary.<--------------------------

print("the given dictionary is: ", d1)
val = input("enter the key: ") #take input from user

if val in d1:    #if the value is present in given dictionary d1 then print else not
    print(val, "is present in dictionary.")
else:
    print(val, "is not present in dictionary.")

# ---------------------->que-2: Write a Python script to merge two Python dictionaries.<--------------------------
# --------->method-1<-------------

print({**d1, **d2})

# --------->method-2<-------------

d3 = d2.copy()  #copy items from d2 to d3
d3.update(d1) #update all items of d1 in d3
print(d3)

# ---------------------->que-3: Write a Python program to sum all the items in a dictionary.<--------------------------

def returnsum(x):  #function to sum aal items in dictionary
    sum = 0
    for i in x:  #for loop to sum all items one by one
        sum = sum+x[i]

    return sum


x = {
    "a1": 100,
    "a2": 12,
    "a3": 50,
}
print("given dictionary is:\n", x)
print("sum:", returnsum(x))

# ---------------------->que-4: Write a Python script to add a key to a dictionary.<--------------------------

A1 = {
    "v1": "red",
    "v2": "black",
    "v3": "white"
}

print("given dictionary is:\n", A1)
A1.update({"v4": "pink"})  #update items in A1
print("updated dictionary is:\n", A1)

# ---------------------->que-5: Write a Python script to concatenate the following dictionaries to create a new one.<--------------------------

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic2.update(dic3)  #update all items from dic3 to dic2
dic1.update(dic2)  ##update all items from dic1 to dic2
print(dic1)
