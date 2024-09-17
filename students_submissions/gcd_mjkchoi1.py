def gcd(a: int, b: int) -> int:
 
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

print(gcd(54, 24))  # Output: 6
print(gcd(48, 18))  # Output: 6
print(gcd(101, 10))  # Output: 1