import math

class Complex:
    #
    #   A Complex number is written in the following form:
    #
    #       z = a + bi
    #
    #   The Complex class gives the user the necessary tools to tackle complex number problems.
    #

    def __init__(self, a,  b):
        assert isinstance(a, int), "Argument Error : a is not an integer."
        assert isinstance(b, int), "Argument Error : b is not an integer."
        self.__a = a
        self.__b = b

    def __repr__(self):
    # Displays the Complex number nicely :-)
        if self.__a == 0:
            if self.__b == 0:
                return "0"
            else:
                return str(self.__b) + "i"
        else:
            if self.__b == 0:
                return str(self.__a)
            else:
                if self.__b < 0:
                    return str(self.__a) + str(self.__b) + "i"
                else:
                    return str(self.__a) + "+" + str(self.__b) + "i"
    
    # Getters&Setters
    def getRealPart(self):
        return self.__a
    def getImagPart(self):
        return self.__b
    def setRealPart(self, new_a):
        assert isinstance(new_a, int), "Argument Error : new real part is not a Number."
        self.__a = new_a
    def setImagPart(self, new_b):
        assert isinstance(new_b, int), "Argument Error : new imaginary part is not a Number."

    # Operation operators
    def __add__(self, other):
        assert isinstance(other, Complex), "Argument Error : second member of addition is not a Complex number."
        return Complex(self.getRealPart() + other.getRealPart(), self.getImagPart() + other.getImagPart())
    def __sub__(self, other):
        assert isinstance(other, Complex), "Argument Error : second member of substraciton is not a Complex number."
        return Complex(self.getRealPart() - other.getRealPart(), self.getImagPart() - other.getImagPart())
    def __mul__(self, other):
        assert isinstance(other, Complex), "Argument Error : second member of multiplication is not a Complex number."
        return Complex(self.getRealPart() * other.getRealPart() - self.getImagPart() * other.getImagPart(), other.getRealPart() * self.getImagPart() + self.getRealPart() * other.getImagPart())
    def __truediv__(self, other):
        pass
    def __pow__(self, n):
        # Only integer powers are supported atm.
        assert isinstance(n, int), "Argument Error : second member of power is not an integer."
        assert n >= 0, "Argument Error : n is not equal or greater than 0."

        if n == 0:
            return Complex(1, 0)
        elif n == 1:
            return self
        else:
            temp_result = Complex(1, 0)
            for i in range(0, n):
                temp_result *= self
            result = temp_result
            return result
            
    # Assignment operators
    def __iadd__(self, other):
        assert isinstance(other, Complex), "Argument Error : second member is not a Complex number."
        self = self + other
        return self
    def __isub__(self, other):
        assert isinstance(other, Complex), "Argument Error : second member is not a Complex number."
        self = self - other
        return self
    def __imul__(self, other):
        assert isinstance(other, Complex), "Argument Error : second member is not a Complex number."
        self = self * other
        return self
    def __itruediv__(self, other):
        assert isinstance(other, Complex), "Argument Error : second member is not a Complex number."
        self = self / other
        return self
    def __ipow__(self, n):
        assert isinstance(n, int), "Argument Error : second member is not an integer."
        self = self ^ n
        return self

    # Unary operators
    def __neg__(self):
        return Complex(- self.getRealPart(), - self.getImagPart())
    def __invert__(self):
        return Complex(Complex(1, 0) / self)

    # Comparaison operators
    def __eq__(self, other):
        assert isinstance(other, Complex), "Argument Error : second member is not a Complex number."
        return self.getRealPart() == other.getRealPart() and self.getImagPart() == other.getImagPart()
    def __ne__(self, other):
        return not(self.__eq__(other))
    
    def module(self):
        return math.sqrt((pow(self.__a), 2) + pow(self.__b, 2))

    def argument(self):
        pass