#Statistics about a file

#Defining a list
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
space = [ " "]

#Defining some variables
file_to_write = str(input("To what file do you wish to write?: "))
file_name = input("Enter a file name to open: ")
file_open = open(file_name)
file_contents = file_open.read().lower()
file_write = open(file_to_write, "w+")

#Defining the count function
def count_function(x, y):
    count = 0
    for letter in x:
        if letter == y:
            count += 1
    file_write.write("\n" + str(count) + " " + y)

#Write the file name
file_write.write("Statistics about " + file_name.upper())

#Couting ALL letters
file_write.write("\n\n--ALL LETTERS--\n\n")
count = 0
for letter in file_contents.replace(" ", ""):
    if letter in alphabet:
        count += 1
file_write.write(str(count) + " letters in total")

#Couting individual letters
file_write.write("\n\n--LETTERS--\n")
for x in alphabet:
    count_function(file_contents, x)

#Counting ALL numbers
file_write.write("\n\n--ALL NUMBERS--\n\n")
count = 0
for number in file_contents:
    if number in numbers:
        count += 1
file_write.write(str(count) + " total numbers")

#Couting numbers
file_write.write("\n\n--NUMBERS--\n")
for x in numbers:
    count_function(file_contents, x)

#Counting special characters
file_write.write("\n\n--SPECIAL CHARACTERS--\n\n")
count = 0
for x in file_contents.replace(" ", ""):
    if x not in alphabet and x not in numbers and x not in space:
        count += 1
file_write.write(str(count) + " special characters")

#Counting spaces
file_write.write("\n--SPACES--\n")
count = 0
for letter in file_contents:
    if letter == " ":
        count += 1
file_write.write("\n" + str(count) + " spaces ")

print("\nPrinted statistics to" + file_to_write +"\n")