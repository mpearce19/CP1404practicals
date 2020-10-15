"""Taxi Test"""

from prac_8.taxi import Taxi


def main():
    """Test Taxi class"""
    taxi = Taxi("Prius ", 100, 1.23)
    taxi.drive(40)
    print(taxi)
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)


main()
