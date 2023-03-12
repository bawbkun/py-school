#Import math module
import math

#formula that runs from line 28 w/ values
def quadratic_formula(a, b, c):
    #Compute the quadratic formula results in variables x1 and x2
    d = (math.pow(b, 2)) - 4*a*c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return (x1, x2)

#print x1 + x2 at end with only .0 to .2 decimal places  
def print_number(number, prefix_str):
    if float(int(number)) == number:
        print(f'{prefix_str}{number:.0f}')
    else:
        print(f'{prefix_str}{number:.2f}')
    
#main program
if __name__ == "__main__":
    print('Enter values for a, b, c in single line.')
    print('Example: 1 2 3')
    input_line = input('Values: ')
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])
    solution = quadratic_formula(a, b, c)
    print(f'Solutions to {a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0')
    print_number(solution[0], 'x1 = ')
    print_number(solution[1], 'x2 = ')
