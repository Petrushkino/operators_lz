def get_min_operations(n):
    return (n + 2) // 3
    
number = 0
while not (1 <= number <= 100_000):
    number = int(input("Введите число (от 1 до 100 000): "))
print(get_min_operations(number))