from random import choice,randint
from time import time,sleep

ccc = 0

def good(x):
    global ccc
    print("----------\n")
    print(x)
    wi = input()
    if wi == x:
        return True
    else:
        ccc += 1
        good(x)

atoz = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])
a = int(input("How many words?:"))
for i in range(1, 4):
    print(i)
    sleep(1)
print("begin!")
il = []
for i in range(1,a+1):
    wl = randint(3,10)
    nl = []
    for j in range(wl):
        nl.append(choice(atoz))
    il.append(''.join(nl))
st = time()
for k in il:
    rt = good(k)
    if rt == True:
        continue
ft = time()
print(f"You have got {str(ccc)} wrong.But you have used {str((ft-st)/60)} min to finish {str(a)} words! GREAT JOB!!!!!!!!!!")