"""
conditionls-if/elif/else
"""
#1
temp=38
if temp>35:
    print("Its Hot")
else:
    print("cool")
print("This will always be printed")
#2
age=17
if age>=18:
    print("you can vote")
else:
    print("Too young to vote")


marks=77
if marks>90:
    grade="A"
elif marks>=75:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>=40:
    grade="D"
else:
    grade="E"
print(f"your marks {marks} : Your Grade {grade}")