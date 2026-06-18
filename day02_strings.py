#string are arrays of characters
for x in "banana":
    print(x)
#string length
a = "Hello, World!"
print(len(a))
#check if a word is in a string
txt = "The best things in life are free!"
print("free" in txt)
#check if not in a string
a= "hello my name is menna"
print("menna"  in a)
#use if statement to check if a word is in a string
if "menna" in a:
    print("yes") 
#slicing strings
b = "Hello, World!"
print(b[2:5])
#negative indexing
print(b[-5:-2]) 
print(b[:5])
print(b[2:])


#modify strings
a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip()) #removes whitespace from the beginning and end of a string
print(a.replace("H", "J"))
print(a.split(",")) #returns a list where the string has been split at each comma



#concatination
a = "Hello"
b = "World"
c = a + b
print(c)
print(a + " " + b)
print(a + " " + b + " " + "I am learning Python")

#formatting strings
age = 36
txt = "I am {:.2f} years old."
print(txt.format(age))
txt=f"my name is menna and I am {age} years old"
print(txt)


#escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#methods
a = "Hello, World!"
print(a.capitalize())
print(a.casefold())
print("".join(a))
print(a.count("l"))
print(a.endswith("!"))
print(a.startswith("H"))
print(a.find("o"))
print(a.index("o"))


#booleans
print(bool("Hello"))
print(bool(15))
print(bool(""))
print(bool(0))
print(bool(None))
print(bool([]))
print(bool({}))
print(bool(()))


#assignment operators
x = 5
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
x=int(x)
x &= 3
print(x)
x |= 3
print(x)
x ^= 5
print(x)
x >>= 3 #right shift
print(x)
x <<= 3 #left shift
print(x)
print(x:= 5) #walrus operator


#ternary operator
a = 5
b = 10
print("a is greater than b") if a > b else print("b is greater than a")

#comparison operators
a = 5
b = 10
print(a == b)
print(a != b)
print(a > b)
print(a < b) 
print(a >= b)
print(a <= b)
#identity operators
a = "Hello"
b = "Hello"
print(a is b)
print(a is not b)

#membership operators
a = "Hello, World!"
print("Hello" in a)
print("hello" not in a)

#logical operators
a = 5
b = 10
print(a > 3 and b > 5)
print(a > 3 or b > 5)
print(not(a > 3 and b > 5))

#bitwise operators
a = 5
b = 10
print(a & b) #bitwise AND
print(a | b) #bitwise OR
print(a ^ b) #bitwise XOR
print(~a) #bitwise NOT
print(a << 1) #left shift
print(a >> 1) #right shift

#operator precedence
a = 5 + 3 * 2
print(a)



