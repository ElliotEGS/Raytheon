#Created by Elliot Smith
import numpy as np
num_to_100A = np.array([1,2])
#Used numpy to create my array as I personally prefer it to the basic python arrays for adding numbers to a list-
# and doing calculations
value = []
#This is used as my true or false value later in the code
primes = np.array([2,3,5,7])
#Started the prime number list manually with values already known for ease in later code
starting_number = 7
#This is used so it checks the list of numbers 1 - x after the number 7 which is the highest prime number-
# that I already have in my list
q1 = ()
q1 = input('How big do you want your list of numbers to be? Type a number that is positive and above 1:')
#Pretty simple user input to check how many primes numbers there are in a certain list so code is more universale 
#*note only works up until about 9000 and code will break if integer is not put in manually, in future would-
# add an accept value error and ask them to imput it again
list_length = int(q1)
#The code struggled to make the user input into a list even with the int() feature so I created a new variable
while (num_to_100A.size + 1) <= list_length:
    list_size = [num_to_100A.size + 1]
    num_to_100B = np.append(num_to_100A , list_size)
    num_to_100A = num_to_100B
    #Had to create 2 variables to add new numbers onto the list and numpy doesnt like using a list inside a list
    
#generates list with a while loop, there may be a python feature to do this but this is the first thing that popped into my head
print ('Here is your list :\n ',num_to_100A)
def check_primes():
    global value
    global primes
    global starting_number
    global list_size
    pot_prime = num_to_100A[starting_number]
    while value != [1]:
    #This while loop checks if there are any common factors in the potential prime number and if one is found it stops the- 
    # loop and continues for the next number,If one isnt found it adds it onto the list of prime numbers and breaks the loop.
    # Debated using the break command but decided not to as not too familiar with it.
        if list_size < primes.size:
            if (pot_prime % primes[list_size]) ==0:
                value = [1]      
        if list_size < primes.size:
            list_size = list_size + 1
            check_primes()
        elif list_size == primes.size and value == [0]:
            primes_temp = np.append(primes , pot_prime)
            primes = primes_temp
            #Again create a temporary variable to add to already existing loop
            value = [1]
while starting_number < list_length:
    list_size = 0
    value  = [0]
    check_primes()
    starting_number = starting_number + 1
    #This loop resets value for my function I created and also checks if the list of prime numbers is completed
    
print ('Here are the prime numbers in the list:\n',primes)




