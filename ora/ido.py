ido = input("Adjon meg egy számot,\n"
            "amit a gép másodpercekre"
            " lefordítva feloszt nagyobb egységekre\n")
ido = int(ido)

minutes = int(ido / 60)
seconds = ido % 60

hours = int(minutes / 60)
minutes = minutes - hours*60

days = int(hours / 24)
hours = hours - days*24

years = int(days / 365)
days = days - years*365

print(years,"years",days,"days",hours,"hours",minutes,"minutes",seconds,"seconds")
list = [years, days, hours, minutes, seconds]
empty = 0
for i in list:
    if i == 0:
        empty+=1
if empty == len(list):
    print("now")
else:
    list2 = ['years','days','hours','minutes','seconds']
    print("\n")
    list3 = list2
    print("- list2 -",list2)
    nemnulla = 0
    for i in list:
        if i != 0:
            nemnulla+=1
    # print(nemnulla)

    # print(list.index(0))
    # print(list2[list.index(0)])
    print("- list copy -",list)
    while len(list) != nemnulla:
        pop = list2[list.index(0)]
        print(pop)
        list3.remove(pop)
        list.remove(0)
    print("- list -",list)
    print(list3)
    k = 0
    while k !=len(list3):
        print(list[k],list3[k],end=" ")
        k+=1
