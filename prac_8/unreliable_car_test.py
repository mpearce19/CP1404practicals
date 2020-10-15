"""Unreliable car test"""

from prac_8.unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Reliable", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 10)

    for i in range(1,15):
        print("Attempting to drive {}km:".format(i))
        print("{:10} drove {:2}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{:10} drove {:2}km".format(unreliable_car.name, unreliable_car.drive(i)))

    print(reliable_car)
    print(unreliable_car)


main()
