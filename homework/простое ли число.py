N=int(input())
N_easy=True
if N!=1:
    for i in range(2,N-1):
        if (N/i).is_integer():
            N_easy=False
    print(N_easy)
else:
    print(True)
