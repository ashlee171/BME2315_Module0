# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

#Ashlee Hyun (uay5yv)

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

# you can use three double-quotes to write multi-line comments

def sum_first_n_fibonacci(N): 
    if N<=0: #if N is 0 or negative, the sum is 0
        return 0
    if N == 1: #if N is 1, the sum is 0
        return 0 
    first = 0 #set first two numbers of the Fibonacci
    second = 1

    total_sum = first + second #start the total with the sum of the first two numbers

    for i in range(3, N+1): #loop from 3rd position up to N (including N)
        next_num = first + second #calculate the next Fibonacci number by adding the previous two
        total_sum += next_num #add the new Fibonacci mumber to running total

        first = second #update first to the value of second
        second = next_num

    return total_sum #return the final sum

N = 5 #define number of elements we want to sum
print (f"The sum of the first {N} Fibonacci numbers is: {sum_first_n_fibonacci(N)}") #call the function and print the result



# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # initialize count
total = 0

while count < N: #sets loop 
    total = total + b #<--ERROR: This line is incorrect. It should be total + a

    next_value = a + b #calculates the next number in the sequence by adding the current two
    a = b #move 'a' to take the value of 'b'
    b = next_value #move 'b' to take the value of the next number

    count = count + 1 #increment count

print(total) #print the total

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy as np

fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

std_deviation = np.std(fib_sequence)

print(f"The first 10 Fibonacci numbers are: {fib_sequence}")
print(f"The standard deviation is: {std_deviation}")
# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def get_fibonacci_sum(N):
    if N <= 0:
        return 0
    if N == 1:
        return 0

    a = 0 
    b = 1
    count = 0
    total = 0

    while count < N:
        total = total + a
        next_value = a + b
        a = b
        b = next_value
        count = count + 1

    return total
N_values = [5, 10, 15, 20, 25, 30]
calculated_sums = []

for N in N_values:
    result = get_fibonacci_sum(N)
    calculated_sums.append(result)
print("Calculated sums:", calculated_sums)

#instead of running six separate loops by hand, the code uses a single function wrapped inside a short for loop.
#it uses .append() to bundle all my answers into a single array container.

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """
    # The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    #Fix 1: Changed strings to integers
    a = 0
    b = 1

    #Fix 2: Initialized index before loop starts
    index = 0

    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index

#Running the function
result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit):
    #Initialize the first two Fibonacci numbers
    a, b = 0, 1
    total = 0

    #Loop through the sequence as long as the current number is within the limit

    while b <= limit:
        #BUG FIX 1: Changed check to != 0 to catch ODD number instead of evens
        if b % 2 != 0:  # This line checks if the Fibonacci number is odd
            #BUG FIX 2: Initialize total to 0 before the loop
            total += b
        #Move forward to the next Fibonacci numbers
        a, b = b, a + b
    return total


# Add your test cases here
#Test Case 1: Limit = 5
#Fibonacci numbers <= 5 are: 0, 1, 1, 2, 3, 5
#Odd ones are: 1, 1, 3, 5 --> Sum = 10
print("Test 1 (Limit 5): Expected 10, Got:", sum_odd_fib(5))

#Test Case 2: Limit = 10
#Fibonacci numbers <= 10 are: 0, 1, 1, 2, 3, 5, 8
#Odd ones are: 1, 1, 3, 5 --> Sum = 10
print("Test 2 (Limit 10): Expected 10, Got:", sum_odd_fib(10))

#Test Case 3: Limit = 15
#Fibonacci numbers <= 15 are: 0, 1, 1, 2, 3, 5, 8, 13
#Odd ones are: 1, 1, 3, 5, 13 --> Sum = 23
print("Test 3 (Limit 15): Expected 23, Got:", sum_odd_fib(15))

# %%