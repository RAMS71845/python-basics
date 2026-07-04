def stats(*numbers):
    if not numbers:
        return None
    total=0
    largest=0
    smallest=0
    for number in numbers:
        avg=total/len(numbers)
    
    return {"min": smallest, "max": largest, "avg": avg}
print(f"expected: {stats(4,8,2,6)}")






