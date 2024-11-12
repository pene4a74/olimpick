import random
N=int(input())
list_n=[]
list_max=[]
for i in range(N):
    list_n.append(random.randint(0,100))
list_n.sort()
print(list_n)
for z in range(len(list_n)):
    if len(list_max)>2:
        break
    if max(list_n)%2==0 and max(list_n) not in list_max:
        list_max.append(max(list_n))
        list_n.pop(list_n.index(max(list_n)))
    else:
        list_n.pop(list_n.index(max(list_n)))
if len(list_max)<3:
    print("нет 3-х чисел")
else:
    print(list_max)
