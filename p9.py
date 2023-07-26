def property():
    i=1
    while i < 100:
        if (i*i)%10==i%10:
            print(i,end = " ")
        i+=1
def main():
    property()
main()
