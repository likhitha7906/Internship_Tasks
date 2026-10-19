#Merge the tools
#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    # your code goes here
    res=[]
    for i in range(0,len(string),k):
        res.append(string[i:i+k])
    
    for i in res:
        unique=""
        for j in i:
            if j not in unique:
                unique=unique+j
        print(unique)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)