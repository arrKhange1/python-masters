import math

def get_divisors(n):
    divisors = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: # второй множитель e.g. 100: 2 и 100 // 2 = 50
                divisors.append(n // i)
    return divisors

def is_prime(divisors_of_n):
    return len(divisors_of_n) == 0

number = int(input('Number: '))
divisors_of_number = get_divisors(number)
print(f'Is prime: {is_prime(divisors_of_number)} \nDivisors: {divisors_of_number}')