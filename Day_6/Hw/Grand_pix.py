drivers=["Ram","Sachin","Virat","Dhoni"]
scores=[
    [10,9,8],
    [7,5,9],
    [9,9,9],
    [7,8,9]
]

totals=[]
for i in range(len(drivers)):
    name=drivers[i]
    race=scores[i]
    total=sum(race)
    totals.append(total)
    print(name,"-",total,"pts")

best_total=-1
best_name=""
for i in range(len(totals)):
    if totals[i]>best_total:
        best_total=totals[i]
        best_name=drivers[i]

print("Winner:", best_name, "with", best_total, "pts")

all_points=sum(totals)
race_count=len(drivers)*3
avg=round(all_points/race_count,1)
print("Average per race: ",avg)

