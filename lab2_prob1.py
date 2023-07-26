def control_digit(n):
    x = n
    while x > 10:
        s = 0
        while x > 0:
            s = s + x%10
            x = x/10
        x = s
    return int(x)
n = int(input("give me a value "))
print("the control digit of integer number ",n," is ",control_digit(n))

        
