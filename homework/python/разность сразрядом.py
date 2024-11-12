N=int(input())
raz=1
list_num=list(str(N))
list_num.reverse()
print(list_num)
list_ost=[]
for i in range(len(list_num)):
    list_ost.append(int(list_num[i])-raz)
    raz+=1
print(max(list_ost))