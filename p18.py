def commonDigits(a,b):
    digitsA=[0]*10
    digitsB=[0]*10
    while a != 0:
        digitsA[a%10]=1
        a//=10
    while b != 0:
        digitsB[b%10]=1
        b//=10
    digits=0
    for i in range(1,10):
        if digitsA[i]!=0 and digitsB[i]!=0:
            print(i,end=" ")
            digits+=1
    print("\nThe number of common digits is: ",digits)
def main():
    a=int(input("Give me the number a: "))
    b=int(input("Give me the number b: "))
    commonDigits(a,b)
main()
          
