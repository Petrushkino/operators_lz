def is_prime(n):
    if n <= 1:
        return "Y"
    for i in range(2, n):
        if n % i == 0:
            return "N"
    return "Y"    
            
num = int(input("Введите число в диапозоне от 1 до 25: "))

result = is_prime(num)
print(result)