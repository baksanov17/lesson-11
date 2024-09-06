numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    simple = True
    for g in numbers[1:]:
        if i > 1 and i % g == 0 and i > g:
            simple = False
            break
    if simple == True and i > 1:
        primes += [i]
    elif simple == False:
        not_primes += [i]
print(primes)
print(not_primes)
