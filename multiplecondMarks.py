#WAP to input marks of a student and print their grade according to the following

Marks              Grade
90 to 100            A+
80 to 90             A
70 to 80             B+
60 to 70             B
50 to 60             C
40 to 50             D
30 to 40             E
less than 30         F'''

'''marks=int(input("Enter the marks"))
if(marks>=90 and marks<=100):
    print("A+")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<80):
    print("B+")
elif(marks>=60 and marks<70):
    print("B")
elif(marks>=50 and marks<60):
    print("C")
elif(marks>=40 and marks<50):
    print("D")
elif(marks>=30 and marks<40):
    print("E")
elif(marks<30):
    print("F")
