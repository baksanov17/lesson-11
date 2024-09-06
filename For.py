numbers = [9, 2, 3, 4, 11, 23, 1, 10, 15, 12, 99]
primes = []
not_primes = []
for i in numbers:
    simple = True
    for g in numbers:
        if i > 1 and g > 1 and i % g == 0 and i > g:
            simple = False
            break
    if i > 1 and g > 1 and simple == True:
        primes += [i]
    elif simple == False:
        not_primes += [i]
print(primes)
print(not_primes)
