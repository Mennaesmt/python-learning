import math

signal_data=[35, 42,28,45,38,25,50,32,55,48,40,22,31,43,37,20,52,29,46,39]
strong_threshold=40
weak_threshold=25
lost_threshold=20


count_strong=0
count_weak=0
count_lost=0
sum_signal=0

for i, signal in enumerate (signal_data,1):
     sum_signal=sum_signal+signal
     if signal >=strong_threshold :
        status='strong'
        count_strong=count_strong+1
     elif signal <= weak_threshold :
        status='weak'
        count_weak=count_weak+1
     else :
        status='lost'
        count_lost=count_lost+1
        
     print(f'sample{i:2d}:{signal:3d} db {status}')

total_samples=len(signal_data)
average_signal=sum_signal/total_samples

print(f'average:{average_signal}')
print(f"strong:{count_strong}")
print(f"weak :{count_weak}")
print(f"lost:{count_lost}")


max_signal=max(signal_data)
min_signal=min(signal_data)

print(f"maximum:{max_signal}")
print(f"minimum:{min_signal}")



#enumerate function (the position , the value )

    
