def print_shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        n = 0
        while n != num_cycles:   
            n = n + 1
            print(n, ': Lather and rinse')
        print('Done.')

user_cycles = int(input('enter cycles: '))
print_shampoo_instructions(user_cycles)
