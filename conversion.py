# Конвертация мили в километры.
# Convert miles to kilometers.

from data import *

# Кооефициент конверции
# conversion factor
conversion_factor = 0.621371


# Функция конверции мили в километры.
# The function of converting miles to kilometers.
def kilometers():
    k = miles / conversion_factor
    return k
