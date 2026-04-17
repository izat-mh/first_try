def is_power(n, m):
    if n == 1:
        return True
    if n % m != 0:
        return False
    return is_power(n // m, m)

n = int(input())
m = int(input())
print(is_power(n, m))