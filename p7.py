def gen(n):
    list1=[]
    n1=1
    list1.append(n1)
    list1.append(2*n1+1)
    list1.append(3*n1+1)
    print(list1)
    n1=3
    n2=4
    i=3
    while i<n:
        list1.append(2*n1+1)
        i+=1
        if i==n:
            break
        list1.append(2*n2+1)
        i+=1
        if i==n:
            break
        list1.append(3*n1+1)
        i+=1
        if i==n:
            break
        list1.append(3*n2+1)
        i+=1
        if i==n:
            break
        n1=2*n1+1
        n2=2*n2+1
    return list1
            
def main():
    n=int(input("Give me the number n: "))
    print(gen(n))
main()
