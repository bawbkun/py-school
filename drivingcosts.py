cars_gas_mileage = float(input('Gas mileage:'))
cost_of_gas = float(input('Cost of gas:'))

# 20mi traveled / 20 mpg = 1 gallon = 3.1599 (baseline for formula)

value1 = (20 / cars_gas_mileage) * cost_of_gas
value2 = (75 / cars_gas_mileage) * cost_of_gas
value3 = (500 / cars_gas_mileage) * cost_of_gas

print(f'{value1:.2f} {value2:.2f} {value3:.2f}')
