strings=[]
count_numbers=int(input())
for i in range(count_numbers):
    a=input()
    if a in strings:
        if "." in a:
            b=1
            while a[:a.find(".")]+"("+str(b)+")"+a[a.find("."):]  in strings:
                b=b+1
            a=a[:a.find(".")]+"("+str(b)+")"+a[a.find("."):]
        else:
            b=1
            while a+"("+str(b)+")"  in strings:
                b=b+1
            a=a+"("+str(b)+")"
    strings.append(a)
strings.sort()

print(*strings,sep="\n")