#exercise1.1
frequency_MHz= 2400
wavelength_m=0.125
name="Oscilloscope"
is_powered_on=True
print(frequency_MHz)
print(wavelength_m)
print(name)
print(is_powered_on)

#exercise1.2
x=100
y=100.0
z="100"
w=True
print(type(x))
print(type(y))
print(type(z))
print(type(w))


#exercise1.3
num1=10
num2=20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)


#exercise1.4
first_name="menna"
last_name="esmat"
concatenated=first_name+" "+last_name
print(concatenated)
print(first_name*3)
print(len(concatenated))


#exercise1.5
txt="42"
number=int(txt)
result=number+8
print(result)

#exercise1.6
fir=True
sec=True
third=False
print(fir and third)
print(fir or third)
print( not third)



#exercise1.7
frequency_GHz=2.4
speed_of_light_m_per_s=3e8
frequency=frequency_GHz*1e9
wavelength_m=speed_of_light_m_per_s/frequency
print(wavelength_m)

#exercise1.8
z1=50
z2=75

gamma=(z2-z1)/(z2+z1)
print(gamma)



#exercise1.9

import math
freq=100
period_s=1/freq
omega=2*math.pi/period_s
print(omega)
print(period_s)


#exercise1.10
v_in=5.0
r1=1000
r2=2000
v_out=v_in*(r2/(r1+r2))
v_out_rounded=round(v_out,2)
print(v_out_rounded)





