#The Minion Game
#https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0
    for i in range(len(string)):
        c=string[i].lower()
        if c in "aeiou":
           kevin+=len(string)-i
        elif c not in "aeiou":
            stuart+=len(string)-i
    if stuart>kevin:
        print("Stuart",stuart)
    elif kevin>stuart:
        print("Kevin",kevin)
    else:
        print("Draw")
           

if __name__ == '__main__':
    s = input()
    minion_game(s)