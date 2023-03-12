print('Enter amount of currency in the following prompts.')
print('')

quarters = float(input('Enter quarters:')) * .25
dimes = float(input('Enter dimes:')) * .10
nickels = float(input('Enter nickels:')) * .05
pennies = float(input('Enter pennies:')) * .01

dollars = quarters + dimes + nickels + pennies

print('')
print(f'Amount: ${dollars:.2f}') # 2 digits after decimal