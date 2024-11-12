num=int(input())
list_place=[]
list_place_al=["W","M","A","A","M","W","W","M","A","A","M","W",]
list_in=0
for i in range(9):
    list_place.append([])
for z in range(9):
    for i in range(2):
        list_place[z].append(7-1*i+12*z)
        list_place[z].append(5+3*i+12*z)
        list_place[z].append(9-5*i+12*z)
        list_place[z].append(3+7*i+12*z)
        list_place[z].append(11-9*i+12*z)
        list_place[z].append(1+11*i+12*z)
for i in range(9):
    if num in list_place[i]:
        list_in=i
        break
if list_place[i].index(num)<6:
    print(list_place[i][list_place[i].index(num)+6])
else:
    print(list_place[i][list_place[i].index(num)-6])

print(list_place_al[list_place[i].index(num)])

"""
-1
+3
-5
+7
-9
+11

различие между столбцами 
+12 везде вообще

"""