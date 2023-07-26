def isLeap(year): #verificam daca anul e bisect
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False
def dayToDate(year,day):
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    #lista cu nr de zile din fiecare luna, pt fiecare pozitie i din lista, avem luna i+1
    if isLeap(year)==True:
        months[1]=29 #daca anul e bisect, luna februarie are 29 de zile
    i=0 #index pentru parcurgerea listei, incepand cu ianuarie
    while months[i] < day: #cat timp ziua depaseste nr de zile dintr-o luna inseamna ca putem avansa
        day-=months[i] #scadem numarul de zile din luna
        i+=1
    #cand while-ul se termina inseamna ca i-ul este luna cautata, iar valoarea ramasa in day este ziua cautata
    print("the date is: ",day,".",i+1,".",year)
def main():
    year=int(input("Give me the year: "))
    day=int(input("Give me the day: "))
    dayToDate(year,day)
main()
