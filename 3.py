def find_prime_factor_of(number):
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
        i = i + 1
    print (number)



find_prime_factor_of(600851475143)