## Conditional Statements
# Grade students based on marks
# marks 90, grade = "A"
# 90 > marks 80, grade = "B"
# 80 > marks 70, grade = "C"
# 70 > marks, grade = "D"
marks = int(input("Enter Your Marks : "))
if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
elif marks >= 60:
    print("D Grade")
else:
    print("You Are Fail")
    
    
# 2nd way
score = int(input("Enter Student Marks : "))
if(score >= 90):
    grade ="A"
elif(score>=80 and marks<90):
    score = "B"
elif(score >= 70 and marks <80):
    score = "C"
else:
    grade = "D"
print("The Grade is =>> ", grade)
