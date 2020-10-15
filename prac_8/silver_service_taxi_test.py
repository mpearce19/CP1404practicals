"""silver service taxi tests"""

from prac_8.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()