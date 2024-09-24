#
#
# def CreatePlant(name,dmg,hp):
#     namePlant = name
#     dmgPlant = dmg
#     hpPlant = hp
#     return {
#         "name":namePlant,
#         "dmg":dmgPlant,
#         "hp": hpPlant
#     }
#     # return (namePlant, dmgPlant, hpPlant)
#
# a = CreatePlant("Подсолнух", 0, 6)
# b = CreatePlant("Стено-орех", 0, 50)
# print(a, b)
#
# print(f"Название: {a['name']}, Урон: {a['dmg']}, Здоровье: {a['hp']} Укусов")
# # print(f"Название: {b[0]}, Урон: {b[1]}, Здоровье: {b[2]} Укусов")


def checkTriangl():
    a = input("1-ая сторона: ")
    b = input("2-ая сторона: ")
    c = input("3-ая сторона: ")

    if not(a.isnumeric()) or not(b.isnumeric()) or not(c.isnumeric()):
        print("Одна из сторон указана не верно")
        return
    a = int(a)
    b = int(b)
    c = int(c)

    if a + b > c and a + c > b and b + c > a:
        print("Треугольник со сторонами ", a, b, c, "существует")
        if a == b and b == c:
            print("Треугольник равносторонний")
        elif a == b or b == c or a == c:
            print("Треугольник равнобедренный")
        elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            print("Треугольный прямоугольный")
        else:
            print("Треугольник обычный")
    else:
        print("Треугольник со сторонами ", a, b, c, " не существует")

while True:
    check = input("\nВведите 0 для завершения программы, 'Enter' для продолжюения:\n")
    if check == "0":
        break
    checkTriangl()