import math

frequency_GHz=float(input("enter the frequency in GHz: "))
impedance=float(input("enter the impedance in ohms: "))
power_dbm=float(input("enter the power in dBm: "))

frequency_Hz=frequency_GHz*1e9
c=3e8
wavelength_m=c/frequency_Hz
period_s=1/frequency_Hz
omega=2*math.pi *frequency_Hz
power_mW=10**((power_dbm)/10)
power_watts=power_mW/1000
print(f"The frequency is: {frequency_Hz} Hz")
print(f"The impedance is: {impedance} ohms")
print(f"The power is: {power_watts} watts") 
print(f"The wavelength is: {wavelength_m} m")
print(f"The period is: {period_s} s")
