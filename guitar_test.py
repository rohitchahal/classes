from guitar import Guitar


def main():
    g1 = Guitar("abc", 1910, 65)
    g1.get_age()
    if g1.is_vintage():
        print("vintage")
    print(g1)


main()
