def gcd(a, b):
    r = -1
    temp_a = max(a, b)
    temp_b = min(a, b)

    while r != 0:
        r = temp_a % temp_b
        temp_a = temp_b
        temp_b = r
    return temp_a

class Fraction:
    def __init__(self, a, b):
        assert isinstance(a, int), "Argument Error : numerator is not an integer."
        assert isinstance(b, int), "Argument Error : denominator is not an integer."
        assert b != 0, "Argument Error : denominator is equal to zero!"

        if a < 0 and b < 0:
            self.__numerator =  int(-a / gcd(abs(a), abs(b)))
            self.__denominator = int(-b / gcd(abs(a), abs(b)))
        elif a < 0 or b < 0:
            self.__numerator =  int(-abs(a) / gcd(abs(a), abs(b)))
            self.__denominator = int(abs(b) / gcd(abs(a), abs(b)))
        else:
            self.__numerator =  int(a / gcd(abs(a), abs(b)))
            self.__denominator = int(b / gcd(abs(a), abs(b)))

    def __repr__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)
    
    def getNumerator(self):
        return self.__numerator
    def getDenominator(self):
        return self.__denominator
    def setNumerator(self, new_numerator):
        assert isinstance(new_numerator, int), "Argument Error : new numerator is not an integer."
        self.__numerator = new_numerator
    def setDenominator(self, new_denominator):
        assert isinstance(new_denominator, int), "Argument Error : new denominator is not an integer."
        assert new_denominator != 0, "Argument Error : new denominator is equal to zero!"
        self.__denominator = new_denominator

    def __add__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return Fraction(self.getNumerator() * other.getDenominator() + other.getNumerator() * self.getDenominator(), self.getDenominator() * other.getDenominator())
    def __sub__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return Fraction(self.getNumerator() * other.getDenominator() - other.getNumerator() * self.getDenominator(), self.getDenominator() * other.getDenominator())
    def __mul__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return Fraction(self.getNumerator() * other.getNumerator(), self.getDenominator() * other.getDenominator())
    def __truediv__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return Fraction(self.getNumerator() * other.getDenominator(), self.getDenominator() * other.getNumerator())
    def __pow__(self, n):
        assert isinstance(n, int), "Argument Error : second member is not an integer."
        return Fraction(pow(self.getNumerator(), 2), pow(self.getDenominator(), 2))

    def __iadd__(self, other):
        return self.__add__(other)
    def __isub__(self, other):
        return self.__sub__(other)
    def __imul__(self, other):
        return self.__mul__(other)
    def __itruediv__(self, other):
        return self.__truediv__(other)
    def __ipow__(self, n):
        return self.__pow__(n)

    def __eq__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return self.getDenominator() == other.getDenominator() and self.getNumerator() == other.getNumerator()
    def __ne__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return self.getDenominator() != other.getDenominator() or self.getNumerator() != other.getNumerator()
    def __gt__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return self.getNumerator() * other.getDenominator() > other.getNumerator() * self.getDenominator()
    def __ge__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return self.__eq__(other) or (self.getNumerator() * other.getDenominator() > other.getNumerator() * self.getDenominator())
    def __lt__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return self.getNumerator() * other.getDenominator() > other.getNumerator() * self.getDenominator()
    def __le__(self, other):
        assert isinstance(other, Fraction), "Argument Error : second member is not a Fraction."
        return self.__eq__(other) or (self.getNumerator() * other.getDenominator() < other.getNumerator() * self.getDenominator())

    def __neg__(self):
        return Fraction(-self.getNumerator(), self.getDenominator())
    def __inv__(self):
        return Fraction(self.getDenominator(), self.getNumerator())

    # Misc functions
    def approximation(self):
        return self.getNumerator() / self.getDenominator()
