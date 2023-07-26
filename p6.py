def ageInYears(currentDay,currentMonth,currentYear,birthDay,birthMonth,birthYear):
    age=0
    for i in range(birthYear+1,currentYear):
        age+=1
    if currentMonth > birthMonth:
        age+=1
    else:
        if currentMonth == birthMonth:
            if currentDay>=birthDay:
                age+=1
    return age
def main():
    currentDay=int(input("The current day: "))
    currentMonth=int(input("The current month: "))
    currentYear=int(input("The current year: "))
    birthDay=int(input("The birth day: "))
    birthMonth=int(input("The birth month: "))
    birthYear=int(input("The birth year: "))
    print("The age of the person in years is",ageInYears(currentDay,currentMonth,currentYear,birthDay,birthMonth,birthYear),"years old.")
main()
            
