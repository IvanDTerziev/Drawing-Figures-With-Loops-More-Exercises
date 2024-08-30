import math

n = int(input())
result = []

starting_stars = 2 if n % 2 == 0 else 1
first_row = f"{'-' * ((n - starting_stars + 1) // 2)}" \
            f"{'*' * starting_stars}" \
            f"{'-' * ((n - starting_stars + 1) // 2)}"
result.append(first_row)

left_idx = math.ceil(n / 2) - 2
right_idx = left_idx + 3 if n % 2 == 0 else left_idx + 2
upper_half = (n - 2) // 2
if not n % 2 == 0:
    upper_half += 1
for r in range(upper_half):
    row = ['-'] * n
    row[left_idx] = '*'
    row[right_idx] = '*'
    left_idx -= 1
    right_idx += 1
    row_str = ''.join(row)
    result.append(row_str)

left_idx += 1
right_idx -= 1
lower_half = upper_half - 1
for r in range(lower_half):
    row = ['-'] * n
    left_idx += 1
    right_idx -= 1
    row[left_idx] = '*'
    row[right_idx] = '*'
    row_str = ''.join(row)
    result.append(row_str)

result.append(first_row)

if n == 1:
    print('*')
elif n == 2:
    print('**')
else:
    print('\n'.join(result))
