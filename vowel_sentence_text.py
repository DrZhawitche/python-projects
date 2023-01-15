#Determining the number of vowels/consonants in a file/sentence

#Defining vowels
vowel = ["a", "e", "i", "o", "u"]

#Defining some variables
vowels = 0
consonants = 0

#Is vowel function
def is_vowel(x):
    if x in vowel:
        return True
    return False

#Determining input method 
method = str(input("Take input from user [I]nput or text [F]ile?: "))

if method.lower() == "f":
    file_input = str(input("Enter full file name: ")) #File location
    file = open(file_input)                          #Defining file
    contents = file.read()                           #Defining contents
    for letter in contents.lower().replace(" ", ""): #Removing spaces from file and making everything lowercase
        if is_vowel(letter) == True:
            vowels += 1
        else:
            consonants += 1
#If method of input is user input
elif method.lower() == "i":
    sentence = str(input("Enter a sentence: ").replace(" ", "").lower()) #Removing spaces and making everything lowercase
    for letter in sentence: 
        if is_vowel(letter) == True:
            vowels += 1
        else:
            consonants += 1

#Printing the final results (vowels/consonants)
print(str(vowels) + " vowels")
print(str(consonants) + " consonants")