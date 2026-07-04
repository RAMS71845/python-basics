def initials(full_name):
    split_name = full_name.split()
    return "".join(name[0].upper() for name in split_name)

full_name = input("Enter your Full name")
result = initials(full_name)
print(f"Expected: {result}")