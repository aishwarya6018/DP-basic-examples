#Number of ways to travel to the last cell of a grid/maze from the first cell of a grid
#We can only move down or right or diagonal.
#Dynamic Programming (Memoization)


memo={}
def gridSol(m,n):
    l=(m,n)
    if(l in memo.keys()):
        return memo[l]
    if(m==1 and n==1):
        return 1 #1x1 grid
    if(m==0 or n==0):
        return 0
    memo[l]=gridSol(m-1,n)+gridSol(m,n-1)
    return memo[l]

m=int(input())
n=int(input())
result=gridSol(m,n)
print("Number of ways are: ",result)