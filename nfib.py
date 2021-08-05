'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#Generate nth Fibonacci number

memo={}
def fib(n):
    if n in memo:
        return memo[n]
    elif n<=2:
        return 1
    else:
        memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
n=int(input())
result=fib(n)
print("The {}th fibonacci number is : ".format(n),result)


