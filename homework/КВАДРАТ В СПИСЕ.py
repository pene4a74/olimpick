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
for i in range(N):
    print(mas[i])

if mas[0][0]==1 and mas[0][len_cube]==1 and mas[len_cube][0]==1 and mas[len_cube][len_cube]==1 :
    print(True)
else:
    len_cube-=1
    for z in range(2,N):
        print("test")
        for i in range(z):
            print("eshkere")
            for j in range(z):
                print("test1",i,j,len_cube,mas[i][j])
                print("test2",i,j,len_cube,mas[i][j+len_cube])
                print("test3",i,j,len_cube,mas[i+len_cube][j])
                print("test4",i,j,len_cube,mas[i+len_cube][j+len_cube],"\n")
                if mas[i][j]==1 and mas[i][j+len_cube]==1 and mas[i+len_cube][j]==1 and mas[i+len_cube][j+len_cube]==1 :
                    print(True,len_cube)
                    num_len.append(len_cube+1)
        len_cube-=1
print("максимальная сторона квадрата:",max(num_len))
    

