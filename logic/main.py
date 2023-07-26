def copie(a,c):
    c=a[:]
    return(c)
def read_list():
    """ functia citeste numarul participantiilor si scorurile acestora """
    a=[]
    c=[]
    length=int(input("the number of participants is: "))
    for i in range(0,length):
        print("the score for the ",i+1)
        a.append(int(input("participant is = ")))
    c=a
    return a

def add_elem(x,a,c):
    """ functia adauga scorul unui nou participant la sfarsitul listei """
    c=a
    a.append(x)
    print(a)
    return a

def test_add_elem():
    assert add_elem(23,[3,6,7])==[3,6,7,23]
    assert add_elem(2,[5])==[2,5]
def insert_elem(i,y,a):
    """ functia adauga un nou concurent la un indice precizat"""
    a.insert(i-1,y)
    print(a)
    return a

def test_insert_elem():
    assert insert_elem(2,10,[30,40,50])==[30,10,40,50]
    assert insert_elem(1,10,[])==[10]
    assert insert_elem(4,100,[1,2,3,5])==[1,2,3,4,5]

def delete_scores(k,z,a):
    """functia sterge scorurile dintre doi indici dati"""
    if k<z:
        del(a[k:z+1])
    else:
        print("impossible")
    print(a)
    return a
  
def del_elem(i,a):
    """functia sterge scorul unui concurent dat de indice"""
    del a[i-1]
    print(a)
    return a
    
def replace_elem(m,x,a):
    """functia schimba scorul unui participant de la un anumit index"""
    for n,i in enumerate(a):
        if i==x:
            a[n]=m
    print(a)
    return a
def print_less(x,a):
    """functia afiseaza scorurile mai mici decat o valoare data"""
    for elem in a:
        if elem<x:
            print (elem)
def print_increasing(a):
    """functia afiseaza scorurile crescator"""
    b=a
    for i in range (len(b)):
        for j in range (i,len(b)):
            if(b[i]>b[j]):
                aux=b[i]
                b[i]=b[j]
                b[j]=aux
    print(b)
def print_decreasing(a):
    """functia afiseaza scorurile descrescator"""
    b=a
    for i in range (len(b)):
        for j in range (i,len(b)):
            if(b[i]<b[j]):
                aux=b[i]
                b[i]=b[j]
                b[j]=aux
    print(b)
def print_sorted(x,a):
    """functia afiseaza scorurile mai mari decat o valoare si sortate crescator"""
    b=a
    for i in range (len(b)):
        for j in range (i,len(b)):
            if(b[i]>b[j]):
                aux=b[i]
                b[i]=b[j]
                b[j]=aux
    for elem in b:
        if elem>x:
            print (elem)
def average(i,j,a):
    """functia calculeaza media aritmetica a particip. dintre doi indici"""
    s=0
    nr=j-i+1
    for k in range(i-1,j):
        s=s+a[k]
    av=s/nr
    print(av)
def smallest(i,j,a):
    """afiseaza cel mai mic scor dintre doi indici"""
    min=9999
    for k in range(i-1,j):
        if a[k]<min:
            min=a[k]
    print(min)
def multiple(i,j,a):
    """functia afiseaza scorurile multiple de 10 intre doi indici"""
    for k in range(i-1,j):
        if a[k]%10==0:
            print(a[k])
def keep10(a):
    """functia sterge toate scoruruile care nu sunt multiple de 10"""
    for i in range (len(a)-1,-1,-1):
        if a[i]%10!=0:
            del a[i]
    print(a)
    return(a)
def high70(a):
    """functia sterge toate scoruruile care nu sunt mai mari decat 70"""
    for i in range (len(a)-1,-1,-1):
        if (a[i]<=70):
            del a[i]
    print(a)
    return(a)
def undo(a,copie):
    a=copie
    print(a)
    return(a)

def readfromfile():
    f= open("input.txt","r")
    a=[]
    for x in f:
        val=int(x)
        a.append(val)
    f.close()
    return a
def writeinfile(a):
    g= open("output.txt","w")
    g.write("[")
    for i in range (len(a)):
        g.write(" "+str(a[i])+" ")
    g.write("]")
    g.close()

def show_menu():
    print("1.Read the list")
    print("2.Add a scores to the list")
    print("3.Insert a score into the list at a certain index")
    print("4.Delete scores between two indices")
    print("5.Delete a score at given index")
    print("6.Replace a score from the list")
    print("7.Print the scores less than a value")
    print("8.Print the scores sorted in increasing order")
    print("9.Print the scores sorted in decreasing order")
    print("10.Print the scores sorted and greater than a value")
    print("11.The average score for specific participants")
    print("12.The smallest score for specific participants")
    print("13.The scores for specific participants which are multiples of 10")
    print("14.Keep only participants with scores multiple of 10 ")
    print("15.Keep only participants with scores higher than 70")
    print("16.Undo the last operation that modified the array")
    print("17.Read current scores from file")
    print("18.Write the current scores to file")
    print("0.Exist")
