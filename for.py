numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    simple = True
    for g in range(2,i):
        if i % g == 0 and i > g:
            simple = False
            break
    if simple == True:
        primes += [i]
    else:
        not_primes += [i]
print(primes)
print(not_primes)
