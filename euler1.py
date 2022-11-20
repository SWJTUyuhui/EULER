import time
#1
s=0
start=time.time()
for i in range(1,1000):
    if (i%3==0)|(i%5==0):
        s=s+i
print(s)
end=time.time()
print(end-start)
#2
s=0
start=time.time()
for i in range(1,1000):
    if i%3==0:
        s=s+i
    if i%5==0:
        s=s+i
    if i%15==0:
        s=s-i
print(s)
end=time.time()
print(end-start)

