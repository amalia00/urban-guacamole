def sumOfDigits(x):
    s=0
    while x!=0:
        s+=x%10
        x//=10
    return s
def isSpecial(x):
    for i in range(0,x):
        if i+sumOfDigits(i)==x:
            return True
    return False
def main():
    x=int(input("Gime me the number: "))
    if isSpecial(x)==True:
        print(x,"is special.")
    else:
        print(x,"is not special.")
main()
