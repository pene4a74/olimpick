import random
list_n=[]
counter=0
a=int(input())
for i in range(a):
    list_n.append(random.randint(0,100))
list_n.sort()
print(list_n)
if sum(list_n)%5==0:
    print(sum(list_n))
else:
    list_num=list_n.copy()
    while (sum(list_num))%5!=0:
        list_num.pop(0)
        print(list_num)
    print(sum(list_num))