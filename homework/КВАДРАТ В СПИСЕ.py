import random
N=int(input())
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
    len_cube_str=len_cube
    for i in range(N-1):
        len_cube_str=N-1
        print("eshkere")
        for j in range(len_cube_str):
            print("test1",i,j,len_cube,mas[i][j])
            print("test2",i,j,len_cube,mas[i][j+len_cube])
            print("test3",i,j,len_cube,mas[i+len_cube][j])
            print("test4",i,j,len_cube,mas[i+len_cube][j+len_cube],"\n")
            if mas[i][j]==1 and mas[i][j+len_cube]==1 and mas[i+len_cube][j]==1 and mas[i+len_cube][j+len_cube]==1 :
                print(True)
                break
    i=0
    j=0
    len_cube_str-=1

