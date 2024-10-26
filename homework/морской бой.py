import random
N=9
pos_al=["A","B","C","D","I","F","G","H"]
mas_our = [["*","A","B","C","D","I","F","G","H",],
       [1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8]
       ]
mas_enemy = [["*","A","B","C","D","I","F","G","H",],
       [1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8]
       ]

mas_enemy_hiden = [["*","A","B","C","D","I","F","G","H",],
       [1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8]
       ]


number_enemy_unit=0
number_our_unit=0


game=True
#наполнение нулями
for i in range(1,N):
    emt_list=[]
    for z in range(1,N):
        emt_list.append("⛆")
    mas_enemy[i].append(emt_list)

for u in range(1,N):
    emt_list=[]
    for z in range(1,N):
        emt_list.append("※")
    mas_enemy_hiden[u].append(emt_list)
#заполнение 16 кораблями

while number_enemy_unit<16: 
    pos_str=random.randint(1,8)
    pos_stl=random.randint(0,7)
    if mas_enemy[pos_str][1][pos_stl]=="⛆":
        mas_enemy[pos_str][1][pos_stl]="⛴︎"
        number_enemy_unit+=1

#наполнение водой нашего поля
for i in range(1,N):
    our_units=[]
    for z in range(1,N):
        our_units.append("⛆")
    mas_our[i].append(our_units)



"""for y in range(N):
    print(mas_our[y])
print("\n")
for y in range(N):
    print(mas_enemy[y])"""



while game:
    while number_our_unit<1:
        for y in range(N):
            print(mas_our[y])
        our_units_pos=input("введите координаты коробля (ex:5А)")
        if mas_our[int(our_units_pos[:1])][1][pos_al.index(our_units_pos[-1:])]=="⛆":
            mas_our[int(our_units_pos[:1])][1][pos_al.index(our_units_pos[-1:])]="⛴︎"
            number_our_unit+=1
    for t in range(N):
        print(mas_enemy_hiden[t])
    attack_pos=input("введите координаты для атаки")

    