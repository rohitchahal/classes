from car import Car


def main():
    limo = Car(100,  "abc")
    limo.add_fuel(20)
    print("fuel = ", limo.fuel)
    limo.drive(115)
    print("odometer = ", limo.odometer)
    print(limo)


main()
