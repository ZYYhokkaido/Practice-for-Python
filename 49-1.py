def is_prime(num):
    for a in range(2,num):
        if num%a==0:
            return False
        
    return True

def sum_primes(x):
    count=0
    for a in range(2,x):
        if is_prime(a)==True:
            count+=a
                
    return count

print(sum_primes(2000))

