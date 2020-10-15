"""taxi simulator"""

from prac_8.taxi import Taxi
from prac_8.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    bill = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("taxis available")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            taxi = taxis[taxi_choice]
        elif choice == "d":
            taxi.start_fare()
            distance = float(input("Drive how far?: "))
            taxi.drive(distance)
            cost = taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(taxi.name, cost))
            bill += cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill))
        print(MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()