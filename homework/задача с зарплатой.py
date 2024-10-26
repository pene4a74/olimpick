import datetime
from datetime import date
day=int(input())
month=int(input())
year=int(input())
list_of_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
list_of_week=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]

if (year%4)==0 and (year%100!=0 or year%400==0):
    list_of_month[2]=29
delta_month=month
delta_day=day
delta_year=year
counter=1


while delta_day!=15:
    counter+=1
    if delta_day+1<list_of_month[delta_month]:
        delta_day+=1
    else:
        delta_month+=1  
        delta_day=1
    if delta_month>len(list_of_month)-1:
       delta_year+=1
       delta_month=1

day=date(delta_year,delta_month,delta_day).weekday()
if day>4:
    while day>4:
        counter-=1
        day-=1
    day+=1
print(counter,list_of_week[day])
