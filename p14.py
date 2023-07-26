def binaryOnes(x):
    ones=0
    while x != 0:
        if x % 2 == 1:
            ones+=1
        x//=2
    return ones
def main():
    numberBaseTen=int(input("Give the number in base ten: "))
    print("The number of ones in the binary representation of",numberBaseTen,"is",binaryOnes(numberBaseTen))
main()
    
