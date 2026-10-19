#SET.ADD
#https://www.hackerrank.com/challenges/py-set-add/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=[]
for i in range(n):
  a.append(input())
res=set(a)
print(len(res))

    
