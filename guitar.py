class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        vintage_string = ""
        if self.is_vintage():
            vintage_string = "(vintage)"
        return "{} ({}), worth ${:10,.2f} {}".format(self.name, self.year, self.cost, vintage_string)

    def get_age(self):
        age = 2016 - self.year
        return age

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False
