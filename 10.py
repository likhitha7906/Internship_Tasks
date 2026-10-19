#Find a string
#https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    i=0
    j=len(sub_string)
    count=0
    while j<=len(string):
        if string[i:j]==sub_string:
            count+=1
        i+=1
        j+=1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)