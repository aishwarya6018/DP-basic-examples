#Generate nth Fibonacci number

memo={} #Create a dictionary to store the values generated.
def fib(n):
    if n in memo: #Check if n is in the dictionary.
        return memo[n]
    elif n<=2:
        return 1
    else:
        memo[n]=fib(n-1)+fib(n-2) #Store the newly generated value in the dictionary, so that it will be useful in later computations.
    return memo[n] #Return the value of the nth fibonacci number.
  
n=int(input()) #Take input from the user.
result=fib(n) #Pass the input to the function and store the return value (Which is the answer) in a variable.
print("The {}th fibonacci number is : ".format(n),result) #Print the result i.e., the nth fibonacci number.


