'''
Вычислить число π c заданной точностью d

*Пример:* 

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

def num_PI():
    d = int(input("Введите количество цифр после запятой: "))

    PI = 0
    for i in range(1, d * 2 ** 22):
        PI = PI + 4 * ((-1) ** (i + 1)) / (2 * i - 1)
    print(f"π: {round(PI, d)}")

num_PI()