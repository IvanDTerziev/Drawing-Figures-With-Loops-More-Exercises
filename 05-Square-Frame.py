n = int(input())

result = []

top_and_bottom_row = "+ " + "- " * (n - 2) + "+"
result.append(top_and_bottom_row)

for i in range(n - 2):
    middle_row = "| " + "- " * (n - 2) + "|"
    result.append(middle_row)

result.append(top_and_bottom_row)

print(*result, sep='\n')
