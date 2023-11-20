attendance=int(input("Enter your attendance: "))

if (attendance>70):
    print("Enter 3 grades and the program will compute the average:")
    grade1=int(input("enter 1st grade"))
    grade2=int(input("enter 2nd grade"))
    grade3=int(input("enter 3rd grade"))
    av=(grade1 + grade2 + grade3)/3

    letterGrade=""
    if (av>=90):
        letterGrade="A"
    elif (av>=80):
        letterGrade="B"
    elif (av>=70):
        letterGrade="C"
    elif (av>=60):
        letterGrade="D"
    else:
        letterGrade="F"
    print("The equivalent letter grade is:", letterGrade)

else:
    print("Your attendace did not meet the requirement")