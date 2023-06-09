
def isPalindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
        
    half = 0
    while x > half:
        half = (half * 10) + (x % 10)
        x = x // 10

    return x == half or x == half // 10
    
def isPalindrome_str(y):
    y = str(y)
    return y == y[::-1]
    

x = 1221
y = 123321
z = 1233321
jen = -121

print(isPalindrome(x))
print(isPalindrome(y))
print(isPalindrome(z))
print(isPalindrome(jen))

print(f"\n{isPalindrome_str(x)}")
print(isPalindrome_str(y))
print(isPalindrome_str(z))
print(isPalindrome_str(jen))