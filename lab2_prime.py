def prime_number(n):
    ok=True
    if(n<2):
        ok = False
    else:
        d=2
        while d <= int(n/2) and ok == True:
            if n%d == 0:
                ok = False
            d+=1
    return ok
n = int(input("give me a value "))
if( prime_number(n) == True):
    print(n," is prime")
else:
    print(n," in not prime")
prime_number(n)
prime_number(n)

