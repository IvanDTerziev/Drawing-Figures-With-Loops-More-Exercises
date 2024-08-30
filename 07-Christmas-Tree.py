result = []
n = int(input())

result.append(f"{' ' * n} |")

for i in range(1, n + 1):
    left_side = " " * (n - i) + "*" * i
    middle = " | "
    right_side = "*" * i + " " * (n - i)
    row = left_side + middle + right_side
    result.append(row)

print('\n'.join(result))
