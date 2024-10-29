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
##наполнение водой вражеского поля поля
for i in range(1,N):
    emt_list=[]
    for z in range(1,N):
        emt_list.append("⛆")
    mas_enemy[i].append(emt_list)
 #скраытое поле
for u in range(1,N):
    emt_list=[]
    for z in range(1,N):
        emt_list.append("※")
    mas_enemy_hiden[u].append(emt_list)
#заполнение 16 кораблями вражеского поля

while number_enemy_unit<3: 
    pos_str=random.randint(1,8)
    pos_stl=random.randint(0,7)
    if mas_enemy[pos_str][1][pos_stl]=="⛆":
        mas_enemy[pos_str][1][pos_stl]="⛴︎"
        number_enemy_unit+=1
#/
#наполнение водой нашего поля
for i in range(1,N):
    our_units=[]
    for z in range(1,N):
        our_units.append("⛆")
    mas_our[i].append(our_units)


"""
for y in range(N):
    print(mas_our[y])
print("\n")

for y in range(N):
    print(mas_enemy[y])
"""
while number_our_unit<3:
        for y in range(N):
            print(mas_our[y])
        our_units_pos=input("введите координаты коробля (например:5А)")
        if mas_our[int(our_units_pos[:1])][1][pos_al.index(our_units_pos[-1:])]=="⛆":
            mas_our[int(our_units_pos[:1])][1][pos_al.index(our_units_pos[-1:])]="⛴︎"
            number_our_unit+=1

while game:
    for g in range(N):
        print(mas_our[g])
    print('\n')
    for t in range(N):
        print(mas_enemy_hiden[t])
    print('\n')
    # наша атака
    attack_pos=input("введите координаты для атаки")
    if mas_enemy[int(attack_pos[:1])][1][pos_al.index(attack_pos[-1:])]=="⛴︎":
        mas_enemy_hiden[int(attack_pos[:1])][1][pos_al.index(attack_pos[-1:])]="☠︎"
        print("убил")
        number_enemy_unit-=1
    else:
        mas_enemy_hiden[int(attack_pos[:1])][1][pos_al.index(attack_pos[-1:])]="⛆"
        print("не попал")

    print("я тут не ломаюсь!")
    if number_our_unit<=0:
        print("вы проиграли")
        break
    elif number_enemy_unit<=0:
        print("вы выйграли")
        break
    # вражеская атака
    while True: 
        pos_atack_str=random.randint(1,8)
        pos_atack_stl=random.randint(0,7)
        if mas_our[pos_atack_str][1][pos_atack_stl]=="⛆":
            mas_our[pos_atack_str][1][pos_atack_stl]="⚙︎"
            print("враг промахнулся")
            break
        elif mas_our[pos_atack_str][1][pos_atack_stl]=="⚙︎":
            pass
        else:
            mas_our[pos_atack_str][1][pos_atack_stl]="☠︎"
            print("враг попал")
            number_our_unit-=1
            break
        