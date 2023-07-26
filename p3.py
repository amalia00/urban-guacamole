def printPower(n,k):
    print(1) #afisam 1 pentru fiecare k
    p=n #copiem n-ul pentru ca va suferi modificari
    while(p<k):
        print(p)
        p*=n #ridicam p la puterea n
def main():
    n=int(input("Give me the number n: "))
    k=int(input("Give me the number k: "))
    printPower(n,k)
main()
