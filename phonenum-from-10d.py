phone_number = int(8005551212)

#first 3 digits of phone #
area_code = phone_number // 10000000

#last 4 digits of phone #
line = phone_number % 10000

# print(area_code)
# print(line)

#to get prefix in center of number we need a temp variable
prefix_tmp = phone_number // 10000
prefix = prefix_tmp % 1000

# print(prefix)

print(f'({area_code}) {prefix}-{line}')