# Данные пользователя в милях.
# User data in miles.

ErrorInput = 'Keep digital data.\n\n'  # Ведите цыфровые данные.

try:
    miles = float(input('Enter the distance in miles.\n'))  # Введите растояние в милях.
except:
    print(ErrorInput)
