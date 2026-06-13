"""
Nested Loops-> a loop inside a loop
"""
#Mental model Rows x columns
for row in range(3):
    for col in range(4):
        print(f"({row}{col})",end=" ")
    print()



colors=["Red","Yellow"]
sizes=["S","M","L"]
print("Generating Variants")
for color in colors:
    for size in sizes:
        sku=f"Tshirt-{color[:3].upper()}-{sizes}"
        print(f"    {color}/{sizes}")
print()

#upper wale line-> rows
#niche wali line-> coloumns
