def control_digit(n):
    if(n % 9 == 0):
        return 9
    else:
        return n % 9
n = int(input("give me a value "))
print("the control digit of integer number ",n," is ",control_digit(n))
