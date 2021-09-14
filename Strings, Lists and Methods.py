# type doesnt actualy matter
var1 = 1  # integer
var2 = 1.1  # float
var3 = "Some text"  # String
var4 = True  # boolean

# if <condition> :
# elif <condition> :
# else:

# STRINGS
string = "a new random string with random values"

print(string[1:4])  # prints the values from the interval [1; 4[
print(string[2:])  # prints the values from 2 till the end

print(string.strip())  # removes the '\n' from the end of the list

print(string.find("new"))  # obtains and returns the fist appearence's index for the seached word or -1 if not found

print(string.replace("new",
                     "old"))  # replaces an old expression by the new one. Note that it does not change the original string

# LISTS
list1 = [1, 3, 57, 8, 8]
list2 = ["hello", "world", "!"]
list3 = ["word", 2.2, "hmm yes", 1, False]

# iterate though a List -> for each
for i in list1:
    print(i)

# manual loop into a list -> c style
for i in range(len(list1)):
    print(list1[i])

if "!" in list2:
    print("!")

list4 = sorted(list1)  # returns a sorted list
list1.sort()  # sorts the list itself
print(list1)
list.reverse()  # reverses the list itself

# HASH TABLES
hashTable = {"key": "object"}
hashTable["newKew"] = "new value added"


# THE METHODS MUST BE DEFINED BEFORE BEING CALLED
def newMethof(arg1, arg2):  # method that recieves two arguments and prints them
    print(arg1 + "\n" + arg2)
