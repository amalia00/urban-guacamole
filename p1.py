def controldigit(x):
    while x>=10:
        s=0 #variabila in care se calculeaza "cifra"
        while x!=0:
            s+=x%10 #adaugam ultima cifra a lui x la suma
            x//=10 #taiem ultima cifra (impartirea intreaga in python se face cu "//"
        x=s
    return x
def main():
    x=int(input("Give me the number x: "))
    y=x #folosit doar pentrut afisare
    while x>=10:
        x=controldigit(x) #facem operatia din functia controldigit pana cand x<10
    print("The control digit of ",y," is",x)
main() #apelul functiei main
      
    
