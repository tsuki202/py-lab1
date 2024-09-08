#Завдання 1
alphabet = "Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz"

#а)
sorted_alphabet = sorted(alphabet)
print("Літери в алфавітному порядку:")
print(" ".join(sorted_alphabet))

#б)
reversed_alphabet = sorted(alphabet)[::-1]
print("\nАлфавіт в зворотньому порядку:")
print(" ".join(reversed_alphabet))

#с)
uppercase = sorted([char for char in alphabet if char.isupper()])
lowercase = sorted([char for char in alphabet if char.islower()],[:-1])
print("\nВеликі літери в алфавітному порядку, а малі в зворотньому:")
print(" ".join(uppercase + lowercase))


#Завдання 2
# Створюємо множини A та B відповідно до умов задачі
A = set(range(10, 51))  # Множина цілих чисел від 10 до 50
B = set(i**2 for i in range(1, 11))  # Множина квадратів цілих чисел від 1 до 10

#a) Перетин множин A та B
intersection_AB = A & B
print("Перетин множин A та B:", intersection_AB)

#b) Об'єднання множин A та B
union_AB = A | B
print("Об'єднання множин A та B:", union_AB)

#c) Різниця множин B та A
difference_BA = B - A
print("Різниця множин B та A:", difference_BA)

#d) Чи належить число 8 множині B
is_8_in_B = 8 in B
print("Чи належить число 8 множині B?", is_8_in_B)


#Завдання3
# Введення множини символів A і символу x
A = set(input("Введіть символи для множини A (без пробілів): "))
x = input("Введіть символ х: ")

# Перевірка і зміна множини A за правилами
if x in A:
    A.remove(x)  # Видалення елементу x, якщо він присутній у множині A
else:
    A.add(x)  # Додавання елемента x, якщо він відсутній у множині A

# Виведення результату
print("Оновлена множина B:", A)