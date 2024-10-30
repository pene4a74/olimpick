import random
N=int(input())
num_len=[0]
mas = [] 
len_cube=N-1
for i in range(N):
    emp_mas=[]
    for j in range(N):
        emp_mas.append(random.randint(0,1))
    mas.append(emp_mas)
if random.randint(0,10)<=8:
    mas[0][0]=1
else:
    mas[0][0]=0
for i in range(N):
    print(mas[i])


for z in range(1,N):
    for i in range(z):
        for j in range(z):
            if mas[i][j]==1 and mas[i][j+len_cube]==1 and mas[i+len_cube][j]==1 and mas[i+len_cube][j+len_cube]==1 :
                print(True,len_cube)
                num_len.append(len_cube+1)
    len_cube-=1
    if int(len(num_len))>1:
        break
print("максимальная плаощадь квадрата:",max(num_len)*max(num_len))
    



"""print("test1",i,j,len_cube,mas[i][j])
    print("test2",i,j,len_cube,mas[i][j+len_cube])
    print("test3",i,j,len_cube,mas[i+len_cube][j])
    print("test4",i,j,len_cube,mas[i+len_cube][j+len_cube],"\n")"""