#functions

def fun():
    print('hi')
fun() #calling

#function arguments
def evenOdd(x):
    if (x%2==0):
        return 'even'
    else:
        return 'odd'
print(evenOdd(4))
print(evenOdd(5))     


#*args  **kwargs
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for k, v in kwargs.items():
        print(f"{k} == {v}")

myFun('Hey', 'Welcome', first='I am', mid='Menna', last='Esmat')

#calculate speed
def speed(dist,time):
    print('distance(km):',dist)
    print('Time(hr):',time)
    return dist/time
print('speed is :',speed(abs(45.9),abs(-2)))
print('')


def greet(x):
    print("Hello",x)
greet('Menna')

#power
def power(a,exp=2):
    return a ** exp
print(power(4))

#all function
def sucsess(*args):
    return all(x > 50 for x in args)

print(sucsess(60))
#Return Multiple Values from a Function
def multiply(*args):
    result=1
    for n in args:
        result*=n
    return result
print(multiply(3,4))

def student(**data):
    for k,v in data.items():
        print(f'{k}:{v}')        
    
def order(name,*items,info):
    print(f"Customer: {name}")
    print(f"Orders: {items}")
    print(f"Info: {info}")


#Variable Length of Arguments (*args)
def func1(*num):
    for i in num:
        print(i)    
        
func1(20,30,40) 



def   show_employee(name,salary= 9000):
    print('name:',name ,'salary:',salary)
        
print(show_employee('manne',12000))  

def f1(a,b):
    def f2(a,b):
        return a+b
    add=f2(a,b)
    return add +5
print(f1(5,10))


#recursive
def addition(n):
    if n== 0:
        return 0
    return n+ addition(n-1)
print(addition(4))    
        
        
#Generate a List of Even Number   
def even_numbers():
    even=[]
    for i in range(0,11):
        if i%2==0:
            even.append(i)
    return even
print(even_numbers()) 

# max()
def largest(list_input):
    largest_item= list_input[0]
    for i in list_input:
        if i >largest_item:
            largest_item= i
    return largest_item        
        
numbers=list(map(int,input('enter number').split()))
print(largest(numbers))

#Recursive Factorial (Non-Negative Integers)#
def addition(n):
    if n<0:
        return 'please enter positive number'
    if n== 0:
        return 1
    return n* addition(n-1)
num=int(input('enter number'))
print(addition(num))    
                       