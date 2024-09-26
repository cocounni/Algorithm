n = int(input())

people = []

for _ in range(n):
    name, day, month, year = input().split()
    people.append((name, int(day), int(month), int(year)))
    
people.sort(key=lambda x: (x[3], x[2], x[1]))

print(people[-1][0])
print(people[0][0])