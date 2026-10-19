#Collections.Counter
#https://www.hackerrank.com/challenges/collections-counter/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
lstOfSizes=list(map(int,input().split()))
numOfCustomers=int(input())
total=0
for i in range(numOfCustomers):
    size,cost=map(int,input().split())
    if size in lstOfSizes:
        total+=cost
        lstOfSizes.remove(size)
print(total)
        
        