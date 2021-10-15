import random as r

# 1. /////////////////////////////////////////////////
#
# print("Írjon be számot (km/h)")
# kmperora = int(input())
# mpers = kmperora/3.6
# print(mpers,"m/s")
# # 2. /////////////////////////////////////////////////
# n = []
# paros = []
# paratlan = []
# j = 0
# while j != 10:
#     n.append(r.randint(0,10000))
#     j+=1
# print("Lista:",n)
#
# for i in n:
#     if i%2==0:
#         paros.append(i)
#     else:
#         paratlan.append(i)
# print("Páros:",paros)
# print("Páratlan:",paratlan)
# 3. /////////////////////////////////////////////////
# a = int(input("kérek egy oldalt "))
# b = int(input("na mégegyet "))
# c = int(input("utsó "))
# d = (a+b+c)/2
# print(d)
# print( d * (d - a) * (d - b) * (d - c) **0.5)
# 4. /////////////////////////////////////////////////
# lista = []
# while True:
#     be = input()
#     if be == "":
#         break
#     lista.append(be)
#     print(lista)
# 5. /////////////////////////////////////////////////
listb = []
for i in range(20):
    listb.append(r.randint(1,100))
print(listb)
print(min(listb))