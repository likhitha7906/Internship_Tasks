#Word Order
#https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_diff_Words(ls):
    d={}
    for i in ls:
            d[i]=d.get(i,0)+1
    return d
    
    
    
n=int(input())
ls=[]
for i in range(0,n):
    ls.append(input())

res=count_diff_Words(ls)
print(len(res))
for key,value in res.items():
    print(value,end=" ")
    





