def sum_of_all_even_numbers(n):
    s=0
    for i in range(0,n+1,2):
        s=s+i
    print ("The sum of even numbers up to ",n," is ",s)

sum_of_all_even_numbers(7)

