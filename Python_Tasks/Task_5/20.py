#Piling UP
#https://www.hackerrank.com/challenges/piling-up/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(all_blocls):   
    for b in all_blocks:
        res=float('inf')
        i=0
        j=len(b)-1
        while(i<=j):
            if b[i]>=b[j] and b[i]<=res:
                  res=b[i]
                  i+=1
            elif b[j]>=b[i] and b[j]<=res:
                  res=b[j]
                  j-=1
            else:
                 print("No")
                 break
                 
        else:
            print("Yes")
            
n=int(input())
all_blocks=[]
for testcase in range(n):
    t1=int(input())
    block=list(map(int,input().split()))
    all_blocks.append(block)
solve(all_blocks)
    
            
          
