#Program to determine whether a number is prime or not

#Adding some exceptions for the first prime numbers
first_prime = [2, 3, 5, 7]

#Take input
number = int(input("Enter your number:"))

#Determining if the input is prime or not
if number in first_prime: #Making sure the first 4 prime numbers aren't counted as non prime
    print("This number is prime")
elif (number / 2).is_integer() or (number / 3).is_integer() or (number / 5).is_integer() or (number / 7).is_integer():
    print("This number is not prime")
else:
    print("This number is prime")