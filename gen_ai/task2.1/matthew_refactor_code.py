# base 10 to base 7

def b10tob7(n):
    if n == 0:
        return '0'
    a = []
    while n != 0:
        r = n - (n // 7) * 7
        a.insert(0, str(r))
        n = (n - r) // 7
    b = ""
    for i in range(len(a)):
        b += a[i]
    return b

print(b10tob7(24))

def base10_to_base7(n):
    if n == 0:
        return '0'
    
    base7_digits = []
    while n:
        base7_digits.append(str(n % 7))
        n //= 7
    
    return ''.join(reversed(base7_digits))

print(base10_to_base7(24))