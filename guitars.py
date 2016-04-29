from guitar import Guitar


def main():
    guitar1 = Guitar("Fender Stratocaster", 2014, 765.40)
    guitar2 = Guitar("Gibson", 1922, 16000)
    guitar3 = Guitar("line", 2010, 1965)
    guitars = [guitar1,guitar2,guitar3]
    for i,guitar in enumerate(guitars):
        print("Guitar {}: {}".format(i,guitar))



main()
