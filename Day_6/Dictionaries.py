# """
# Dict- holds n key,value pairs
# """
# student={
#     "name":"Rohan",
#     "age":21,
#     "marks":[80,86,99]
# }
# print("Name:   ",student["name"])
# print("How many items in dictionary: ",len(student))
# print("'age' in students","age" in student )
# print("Missing values",student.get("college"))  
# # print("Missing values",student("college"))#will show RUN TIMEerror


# student["email"]="abc@gmail.com"
# student["age"]=35
# print("Student after Update",student)

# remove_item=student.pop("marks")
# print (remove_item)

# # del student["email"]
# # print(remove_item)
# # print(student)
# #task-create the total bill
# price={
#     "coffee":120,
#     "juice":100,
#     "sandwich":150
# }
# order=["coffee","juice"]
# total=0
# for item in order:
#         total+=price.get(item)

# print(total)
# # 4

# bills = {
#     "Aarav": [60, 75, 60],
#     "Priya": [80, 80],
#     "Rohan": [50, 90, 70, 40],
# }
# students=["Aarav","Priya","Rohan"]
# total=0
# for student in students:
#     total+=sum(bills.get(student))
#     print(f"{student} Rs {total}")
