# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# def Factor(n):
#     Ans = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             Ans.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         Ans.append(n)
#     return Ans
# print(Factor(int(input())))

# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# numbers = [2, 20, 3, 3, 40, 5, 77, 12, 77]
# def get_unique_numbers(numbers):
#     unique = []
#     for number in numbers:
#         if number in unique:
#             continue
#         else:
#             unique.append(number)
#     return unique
# print(get_unique_numbers(numbers))


# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# from random import randint
# max_val=100
# k = int(input('Введите натуральную степень k:'))
# koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
# poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# poly=poly.replace('x^1+', 'x+')
# poly=poly.replace('x^0', '')
# poly+=('','1')[poly[-1]=='+']
# poly=(poly, poly[:-2])[poly[-2:]=='^1']
# print(poly)