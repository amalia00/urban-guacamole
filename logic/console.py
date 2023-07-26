import main
main.show_menu()
def interface():
    op=input("Option= ")
    if op=='1':
        a=main.read_list()
        c=[]
    elif op=='17':
        a=main.readfromfile()
        c=[]
    c=main.copie(a,c)
    while op!='0':
        main.show_menu()
        if op=='2':
            c=main.copie(a,c)
            x=int(input("The score you want to add is = "))
            a=main.add_elem(x,a,c)
        elif op=='3':
            c=main.copie(a,c)
            y=int(input("The score you want to insert is = "))
            i=int(input("The number of the participant will be = "))
            a=main.insert_elem(i,y,a)
        elif op=='4':
            c=main.copie(a,c)
            k=int(input("The first index is = "))
            z=int(input("The last index is = "))
            a=main.delete_scores(k,z,a)
        elif op=='5':
            c=main.copie(a,c)
            i=int(input("The number of the participant you want to delete is= "))
            a=main.del_elem(i,a)
        elif op=='6':
            c=main.copie(a,c)
            x=int(input("The score you want to replace is = "))
            m=int(input("The new score will be = "))
            a=main.replace_elem(m,x,a)
        elif op=='7':
            c=main.copie(a,c)
            x=int(input("The value is = "))
            main.print_less(x,a)
        elif op=='8':
            c=main.copie(a,c)
            main.print_increasing(a)
        elif op=='9':
            c=main.copie(a,c)
            main.print_decreasing(a)
        elif op=='10':
            c=main.copie(a,c)
            x=int(input("The value is = "))
            main.print_sorted(x,a)
        elif op=='11':
            c=main.copie(a,c)
            i=int(input("The number of the first participant = "))
            j=int(input("The number of the last participant = "))
            print("The average is ")
            main.average(i,j,a)
        elif op=='12':
            c=main.copie(a,c)
            i=int(input("The number of the first participant = "))
            j=int(input("The number of the last participant = "))
            print("the smallest score is ")
            main.smallest(i,j,a)
        elif op=='13':
            c=main.copie(a,c)
            i=int(input("The number of the first participant = "))
            j=int(input("The number of the last participant = "))
            print("the smallest score is ")
            main.multiple(i,j,a)
        elif op=='14':
            c=main.copie(a,c)
            main.keep10(a)
        elif op=='15':
            c=main.copie(a,c)
            main.high70(a)
        elif op=='16':
            print(a)
            print(c)
        elif op=='18':
            main.writeinfile(a)
        elif op=='0':
            print("good bye")
        else:
             print("invalid option")
        op=input("Option= ")
interface()