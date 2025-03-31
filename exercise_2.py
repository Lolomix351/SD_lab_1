# Шакула Дмитрий Андреевич 090301-ПОВа-о24

def solve(a, b, c):
    # Сначала ищем положительные x и y, перебирая y от 1
    for y in range(1, 1001):
        numerator = c - b * y
        if a != 0 and numerator % a == 0:  
            x = numerator // a
            if x > 0:  
                return f"{x} {y}"

    # Если не нашли положительные x и y, ищем с отрицательными y
    for y in range(-1, -1001, -1):
        numerator = c - b * y
        if a != 0 and numerator % a == 0: 
            x = numerator // a
            if x > 0: 
                return f"{x} {y}"

    return "Impossible"


def main():
    # Читаем входные данные
    a, b, c = map(int, input().split())
    print(">>> solve({}, {}, {})".format(a, b, c))
    print(solve(a, b, c))


if __name__ == "__main__":
    main()
    
print("Выполнил Шакула Дмитрий Андреевич 090301-ПОВа-о24")
