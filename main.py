import json

## Task 1
# Вывести все товары в наличии
# Найти самый дорогой товар
# Посчитать общую стоимость всех товаров

# load first.json
with open("first.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

# total stock
stock = [p["name"] for p in products if p["in_stock"]]
print(f"Products in stock: {stock}")

# the most expensive product
product = max(products, key=lambda x: x["price"])["name"]
print(f"The most expensive product: {product}")

# total price of all products
total = sum(product["price"] for product in products)
print(f"Total: {total}")

## Task 2
# Найти средний балл каждого студента
# Вывести студента с самым высоким средним баллом
# Вывести студентов, у которых средний балл ≥ 4

# load second.json
with open("second.json", "r", encoding="utf-8") as f:
    students_task2 = json.load(f)["students"]

# Average function
def student_average(students):
    averages = list()
    for student in students:
        average = sum(student["grades"]) / len(student["grades"])
        name = student["name"]
        averages.append([name, round(average, 2)])
    return averages
st_avgs = student_average(students_task2)

# average of every student
print(f"Average of every student: {st_avgs}")

# a student with the highest average
highest_avg = max(st_avgs, key=lambda x: x[1])
print(f"Highest average: {highest_avg}")

# students with average >= 4
high_avg_list = [st[0] for st in st_avgs if st[1] >= 4]
print(f"Average >= 4: {high_avg_list}")

## Task 3
# Вывести всех студентов
# Найти факультет с наибольшим количеством студентов
# Посчитать общее количество студентов

# load third.json
with open("third.json", "r", encoding="utf-8") as f:
    faculties = json.load(f)["university"]["faculties"]

# all students
students_task3 = [st["name"] for fac in faculties for st in fac["students"]]
print(f"All students: {students_task3}")

# faculty with more students
largest_faculty = max(faculties, key=lambda x: len(x["students"]))["name"]
print(f"Largest faculty: {largest_faculty}")

# total students amount
print("Total students amount:", sum(len(f["students"]) for f in faculties))