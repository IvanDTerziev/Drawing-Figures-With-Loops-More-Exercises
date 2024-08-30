result = []
house_width = int(input())

roof_height = (house_width + 1) // 2
initial_stars = 2 if house_width % 2 == 0 else 1

for i in range(roof_height):
    if i == 0 and house_width % 2 == 0:
        dashes = (house_width - 2) // 2
        row = "-" * dashes + "**" + "-" * dashes
    else:
        dashes = (house_width - initial_stars) // 2
        row = f"{'-' * dashes}{'*' * initial_stars}{'-' * dashes}"
    result.append(row)
    initial_stars += 2

base_height = house_width - roof_height
for i in range(base_height):
    row = f"|{'*' * (house_width - 2)}|"
    result.append(row)

print('\n'.join(result))
