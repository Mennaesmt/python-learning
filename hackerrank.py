#1
n=int(input())
s=set(map(int,input().split()))

for _ in range(n):
    command = input().split()

    if command[0] == "pop":
        s.pop()

    elif command[0] == "remove":
        s.remove(int(command[1]))

    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))




"""menna is a shoe shop owner. His shop has X number of shoes. 
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute how much money menna earned."""

from collections import Counter
X=int(input()) #number of shoes
sizes=list(map(int ,input().split()))
s=Counter(sizes)
N=int(input()) #number of customers
e=0  #earned
for _ in range(N):
    size,price=map(int,input().split())
    if s[size]:
        e += price
        s[size] -= 1

print(e)



#polar 
import cmath
z=complex(input())
r=abs(z)
theta=cmath.phase(z)
print(r)
print(theta)


#simple array sum
a=int(input())
arr=list(map(int,input().split()))
print(sum(arr))


#compare the triplets
a=list(map(int,input().split()))
b=list(map(int,input().split()))
alice=0
bob=0
for i in range(3):
    if a[i]>b[i]:
        alice=alice+1
    elif b[i]>a[i]:
        bob=bob+1
print(alice,bob)  



#plusMinus

def plusMinus(arr):
    n=len(arr)
    p=0
    ni=0
    z=0
    for i in arr:
        if i>0:
            p+=1
        elif i<0: 
            ni+=1
        else:
            z+=1
    print(f'{p/n:.6f}')
    print(f'{ni/n:.6f}')
    print(f'{z/n:.6f}')
                
    
if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    plusMinus(arr)
    


# staircase
def staircase(n):
    for i in range(1,n+1):
        s=' '*(n-i)
        h='#'*i
        print(s+h)
if __name__ == '__main__':
    n=int(input())
    staircase(n)

    
