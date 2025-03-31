# Шакула Дмитрий Андреевич 090301-ПОВа-о24

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def solve_diophantine(a, b, c):
    g, x0, y0 = extended_gcd(a, b)

    if c % g != 0:
        return None

    factor = c // g
    x_base = x0 * factor
    y_base = y0 * factor

    b_g = b // g
    a_g = a // g

    if b_g == 0:
        if x_base >= 0:
            return x_base, y_base
        else:
            return None

    if b_g > 0:
        k = -x_base // b_g
        if -x_base % b_g != 0:
            k += 1
    else:
        k = -x_base // b_g

    x = x_base + k * b_g
    y = y_base - k * a_g

    return x, y


# Ввод данных от пользователя
a, b, c = map(int, input().split())

# Решаем уравнение
result = solve_diophantine(a, b, c)

# Вывод результата
if result is None:
    print("No solution")
else:
    x, y = result
    print(x, y)
    
print("Выполнил Шакула Дмитрий Андреевич 090301-ПОВа-о24")
