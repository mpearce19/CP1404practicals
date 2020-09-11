# 6.
from prac_6.guitar import Guitar

CURRENT_YEAR = 2020

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
other = Guitar("Another Guitar", 2012, 1512.9)

print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98,
                                                  guitar.get_age()))
print("{} get_age() - Expected {}. Got {}".format(other.name, 8,
                                                  other.get_age()))
print()
print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                     True,
                                                     guitar.is_vintage()))
print("{} is_vintage() - Expected {}. Got {}".format(other.name,
                                                     False,
                                                     other.is_vintage()))
