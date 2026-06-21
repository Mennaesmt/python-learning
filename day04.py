#if_statement ,loops

x=5
y=2
if x>y:
    print('x greater than y')


#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")  


#ex 1
signal_strength=45
if signal_strength>40:
   print("signal is strong")
else :
  print("signal is weak")
  
#ex 2 logic operators
frequency = 2400
impedance = 50
if frequency > 1000 and impedance ==50 :
  print("valid configuration") 


#while loop
battery=0
while battery<100:
  battery=battery+10
  print(f"charding...{battery}%")
print("battery full")



#break & continue

c=0
while True:
  c=c+1
  print(c)
  if c==5:
    break
print("loop ended")


s=0
count=1
while count<=10:
  s=s+count
  count=count+1
print(s)           

