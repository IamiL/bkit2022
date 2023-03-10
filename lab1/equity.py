import sys
import math


def get_coef(index, prompt):
    
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    coef = 'coefficient'

    while not isinstance(coef, float):
        try:
            coef = float(coef_str)
        except:
            print('Проверьте корректность вводимых данных')
            print(prompt)
            coef_str = input()
    return coef


def get_roots(a, b, c):
    
    answer = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            t1 = math.sqrt(root)
            t2 = -math.sqrt(root)
            answer.append(t1)
            answer.append(t2)
        if root == 0:
            t = 0
            answer.append(t)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        if root1 > 0:
            t1 = math.sqrt(root1)
            t2 = -math.sqrt(root1)
            answer.append(t1)
            answer.append(t2)
        if root1 == 0:
            t = 0
            answer.append(t)
        root2 = (-b - sqD) / (2.0 * a)
        if root2 > 0:
            t3 = math.sqrt(root2)
            t4 = -math.sqrt(root2)
            answer.append(t3)
            answer.append(t4)
        if root2 == 0:
            t = 0
            answer.append(t)
    return answer


def main():
    a = 0
    while a == 0:
        print('Значение коэффициента А не может равняться 0')
        a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()