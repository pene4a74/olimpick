N=int(input())
nums=[]
N_easy=True
if N!=1:
    for i in range(2,N-1):
        if (N/i).is_integer():
            N_easy=False
            
    print(N_easy)
else:
    print(True)

for i in range(2,N-1):
    if (N/i).is_integer():
        nums.append()



if nums.index(N)-nums.index(N-1)>nums.index(N+1)-nums.index(N):
    print(nums.index(N-1))
else:
    print(nums.index(N+1))
    