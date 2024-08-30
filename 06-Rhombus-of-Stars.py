n = int(input())

for i in range(1, n):
    print(f"{' ' * (n - i)}*{' *' * (i - 1)}")

for i in range(1, n + 1):
    print(f"{' ' * (i - 1)}*{' *' * (n - i)}")
