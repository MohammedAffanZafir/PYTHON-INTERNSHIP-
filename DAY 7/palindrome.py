def palindrome(n, rev=0, temp=None):
    if temp is None:
        temp = n
    if n == 0:
        return temp == rev
    rev = rev * 10 + n % 10
    return palindrome(n // 10, rev, temp)
num = 12321
print("Palindrome:", palindrome(num))