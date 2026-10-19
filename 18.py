#List
#https://www.hackerrank.com/challenges/python-lists/problem


if __name__ == '__main__':
    N = int(input())
    res=[] 
    for operation in range(N):
        op,*nums=input().split()
        nums = list(map(int, nums))
       
        if op=="insert":
            res.insert(nums[0],nums[1])
        elif op=="print":
            print(res)
        elif op=="append":
            res.append(nums[0])
        elif op=="sort":
            res.sort()
        elif op=="pop":
            res.pop()
        elif op=="reverse":
            res.reverse()
        elif op=="remove":
            res.remove(nums[0])
            
            