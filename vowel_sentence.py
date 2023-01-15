#Program to count vowels and consonnants in a word or sentence

#Defining vowels
vowel = ["a", "e", "i", "o", "u"]

#Defining some variables
vowels = 0
consonants = 0

#Is vowel function
def is_vowel(x):
    if x in vowel:
        return True
    elif x not in vowel:
        return False

#Determing if reading from user input or text file
inp_text = str(input("Read from [I]nput or text [F]ile?: "))

#Taking input
sentence = str(input("Enter a sentence: ").replace(" ", "").lower())

#Determining whether it is a vowel or not
for letter in sentence: #Removing spaces
    if is_vowel(letter) == True:
        vowels += 1
    else:
        consonants += 1

#Printing the final results
print(str(vowels) + " vowels")
print(str(consonants) + " consonants")