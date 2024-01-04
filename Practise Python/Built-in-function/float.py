from decimal import Decimal, getcontext

# getcontext -> viewing the list of context.

getcontext().prec = 4

# rounded to 4 decimal places
Decimal_comb = Decimal(3.5) + Decimal(2.2)
print(Decimal_comb, type(Decimal_comb))


c = float("1e-003")
print(c, type(c))
d = float("+1E6")
print(d, type(d))

# 5.700 <class 'decimal.Decimal'>
# 0.001 <class 'float'>
# 1000000.0 <class 'float'>
