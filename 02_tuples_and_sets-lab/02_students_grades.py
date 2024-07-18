num = int(input())
students = {}

for _ in range(num):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    print(f"{name} -> {' '.join([f'{grade:.2f}' for grade in grades]) } (avg: {(sum(grades)/len(grades)):.2f})")