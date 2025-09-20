def nums(n):
    if n == 0:
        return
    nums(n - 1)
    print(n, end=" ")
n = int(input())
nums(n)