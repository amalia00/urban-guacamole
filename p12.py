def sameDigits(a,b):
    digitsA=[0]*10
    digitsB=[0]*10
    while a != 0:
        digitsA[a%10]=1
        a//=10
    while b != 0:
        digitsB[b%10]=1
        b//=10
    for i in range(0,10):
        if digitsA[i]!=digitsB[i]:
            return False
    return True
def main():
    a=int(input("Give the first number: "))
    b=int(input("Give the second number: "))
    if sameDigits(a,b)==True:
        print("The numbers have the same digits.")
    else:
        print("The numbers don't have the same digits.")
main()
            
