import random as r
# print(chr(103))
# print(chr(65))
# print(ord("a"))
# print(chr(ord("a")))
# print(int("A5",base=16))
# print(round(32.31752365435, 0))
life = True
def rulett():
    print("Válassz csövet")
    int(input())


    shot = r.randint(1,5)
    if guess == shot:
        print("kaptad a golyót öcsi")
        life = False
    else:
        print("nem haltál meg")
    print("te választásod:",guess)
    print("ebben a csőben volt golyó:",shot)
    print("\n Kövi játékos jön")
while life == True:
    rulett()