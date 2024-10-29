import random
a=[]
N=int(input())
counter=0
first_el=0
end_el=0
for i in range(N):
    a.append(random.randint(0,1))
print(a)
for i in range(len(a)):
    if a[i]==1:
        first_el=i
        break

for i in range(len(a)):
    if a[i]==1:
        first_el=i
        break
for i in range(first_el,end_el+1):
    counter+=1
print(counter)