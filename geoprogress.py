def progression_sum(b, q, n):   
    if q == 1:
        return b * n
    else:
        return b * (q**n - 1) // (q - 1)
    
    
input_str = input("Введите 3 числа через пробел (первое — начальный член b, второе — множитель q, третье — количество элементов n): ").split()

a = int(input_str[0])
b = int(input_str[1])
c = int(input_str[2])

result_sum = progression_sum(a, b, c)
print("Результат вычисления суммы:", result_sum)