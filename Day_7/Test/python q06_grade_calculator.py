def grade(marks):
    
    if marks>100 and marks<0:
        print("INVALID")
    elif marks>=90:
        grade='A'
    elif marks>=75 and marks<90:
        grade='B'
    elif marks>=60 and marks<75:
        grade='C'
    elif marks>=40 and marks<70:
        grade='D'
    else:
        grade='E'
    return grade
    
marks=int(input("ENTER YOUR MARKS: "))
print(f"# {grade(marks)}")


