import time 
seconds = int(input('enter count down time in seconds: '))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
print('time up!')  
