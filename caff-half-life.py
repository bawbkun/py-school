caffeine_mg = float(100)

# Output needed
# After 6 hours: 50.00 mg
# After 12 hours: 25.00 mg
# After 24 hours: 6.25 mg

hour_6 = caffeine_mg / 2
print(f'After 6 hours: {hour_6:.2f} mg')

hour_12 = hour_6 / 2
print(f'After 12 hours: {hour_12:.2f} mg')

hour_24 = hour_12 / 4
print(f'After 24 hours: {hour_24:.2f} mg')