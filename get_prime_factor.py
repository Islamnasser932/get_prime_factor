def get_prime_factor(N):
    factor = []
    divisor = 2

    while (divisor <= N):
        if (N % divisor == 0):
            factor.append(divisor)
            N = N//divisor
        else:
            divisor += 1

    return factor


print(get_prime_factor(13))
print(get_prime_factor(800))
