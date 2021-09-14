# OPEN FILE
f = open("file")  # used to open a file

line = f.readline()  # used to read a line
print(line)

remainingList = f.readlines()  # reads all the file and returns the lines in a list
for i in remainingList:
    print(i.strip())

print("")

# CREATE FILE
nf = open("newFile", "w")  # open/create a file to write. The contents the file had before are cleared
nf.write("This is a new File")

nf = open("newFile", "a")  # opens/ create a file to write. It does not delete the contents the file had before
nf.write("\nAnew line even tho it was reopened")


nf = open("newFile")
line = nf.readlines()
for s in line:
    print(s.strip())