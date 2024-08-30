output_list = []
glasses_width = int(input())

upper_frame = "*" * (2 * glasses_width) + " " * glasses_width + "*" * (2 * glasses_width)
output_list.append(upper_frame)

for i in range(1, glasses_width - 1):
    left_lens = "*" + "/" * (2 * glasses_width - 2) + "*"
    right_lens = "*" + "/" * (2 * glasses_width - 2) + "*"

    if i == (glasses_width - 1) // 2:
        middle = "|" * glasses_width
    else:
        middle = " " * glasses_width

    middle_row = left_lens + middle + right_lens
    output_list.append(middle_row)

bottom_row = upper_frame
output_list.append(bottom_row)

print('\n'.join(output_list))
