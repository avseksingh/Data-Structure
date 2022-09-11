class Currency:
    def __init__(self, rupees, paise):
        self.total = 100 * rupees + paise

    def __add__(self, other):
        return Currency(0, self.total + other.total)

    def __sub__(self, other):
        return Currency(0, self.total - other.total)

    # def __divmod__(self, other):
    #     return Currency(0,self.total % other.total)

    def __mul__(self, other):
        return Currency(0, self.total * other.total)

    def __eq__(self, other):
        if self.total == other.total:
            return True
        else:
            return False
        # return Currency(0, self.total == other.total)

    def __gt__(self, other):
        if self.total > other.total:
            return True
        else:
            return False

    def __str__(self):
        # print("Str Called")
        total = self.total
        sign = ""
        if self.total < 0:
            sign = "-"
            total = -self.total
        r = total // 100
        p = total % 100
        if r < 10:
            r = "0" + str(r)
        if p < 10:
            p = "0" + str(p)
        return "₹ {2} {0}.{1}".format(r, p, sign)


c1 = Currency(3, 60)
c2 = Currency(3, 60)
print(c1 == c2)  # c1.add(c2)
