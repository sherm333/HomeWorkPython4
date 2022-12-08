'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

*Пример*

- при N=236     ->        [2, 2, 59]
'''

def prime_factors():
    number = int(input("Введите число N: "))
    factors = []
    a = 2

    while number > 1:
        if number % a == 0:
            factors.append(a)
            number /= a
        else:
            a += 1

    print(f"Простые множители числа N:", *factors)

prime_factors()