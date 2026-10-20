#17Check Strict Superset
#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
print(all(A>set(map(int,input().split())) for i in range(n)))
