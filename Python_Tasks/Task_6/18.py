#Set Mutations
#https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
A=set(map(int,input().split()))
t=int(input())
for i in range(t):
    operation=input().split()
    B=set(map(int,input().split()))
    if operation[0]=="intersection_update":
        A.intersection_update(B)
    elif operation[0]=="update":
        A.update(B)
    elif operation[0]=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif operation[0]=="difference_update":
        A.difference_update(B)
print(sum(A))
