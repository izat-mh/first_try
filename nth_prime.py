num = int(input())
primes=[]
candidate = 2
while len(primes) != num:
    is_prime= True
    for divisor in range(2,candidate):
        if candidate%divisor==0:
            is_prime= False
            break
    if is_prime:
        primes.append(candidate)
    candidate+=1
print(primes[-1])