import numbers
from typing import Union

class ComplexFraction:

    def __init__(self, num: numbers.Number, denomin: numbers.Number) -> None:
        """
        Initiates a new instance of ComplexFraction object, numerator and denominators may both be ints or complex
        with integer parts - unfortunately, complex numbers are stored as floats (forced to have integer values) and
        it needs to be implemented in other way. Floats are accepted only when int(val) == val
        """

        # Private attributes
        self._num = 0
        self._denomin = 1
        # Setters initiate the private attributes
        self.num = num
        self.denomin = denomin

    @property
    def num(self) -> complex:
        return self._num

    @num.setter
    def num(self, val: numbers.Number) -> None:
        """
        Needs to be called before the denominator setter, as the latter one changes numerator by multiplying with
        denominator's conjugate. Also, it is the latter one that divides both num and denomin by their GCD
        """
        if isinstance(val, int) or (isinstance(val, float) and int(val) == val):
            self._num = val
        elif isinstance(val, complex):
            if not val.real == int(val.real) or not val.imag == int(val.imag):
                raise Exception("Real and imaginary parts of numerator must both be integers!")
            else:
                self._num = val
        else:
            raise Exception("Numerator must be integer or complex with integer parts!")

    @property
    def denomin(self) -> int:
        return int(self._denomin)

    @denomin.setter
    def denomin(self, val: numbers.Number) -> None:
        """
        Denominator setter - assures correct type and then converts denomin to be real by multiplying with
        conjugate. Before returning, divides both numerator and denominator by their Greatest Common Divisor
        """

        if val == 0:
            raise Exception("Denominator must not be equal to zero!")
        elif isinstance(val, int) or (isinstance(val, float) and int(val) == val) or (isinstance(val, complex) and
                                                                                      val.imag == 0):
            self._denomin = val
            divisor = ComplexFraction.complex_GCD(self.num, self.denomin)
            self.num = (self.num.real // divisor) + (self.num.imag // divisor)*1j
            self._denomin = self.denomin // divisor
        elif isinstance(val, complex):
            if not val.real == int(val.real) or not val.imag == int(val.imag):
                raise Exception("Real and imaginary parts of denominator must both be integers!")
            else:
                temp = self.num
                self.num = self.num*val.conjugate()
                self._denomin = int((val*val.conjugate()).real)
                divisor = ComplexFraction.complex_GCD(self.num, self.denomin)
                self.num = (self.num.real // divisor) + (self.num.imag // divisor)*1j
                self._denomin = self.denomin // divisor
                print(f"Multiplying {temp} / {val} with {val.conjugate()} / {val.conjugate()}. Got {self.num} / "
                      f"{self.denomin}")
        else:
            raise Exception("Denominator must be integer or complex with integer parts!")

    def __repr__(self) -> str:
        # Using getters
        return f"{self.num} / {self.denomin}"

    def __neg__(self) -> "ComplexFraction":
        return ComplexFraction(-self.num, self.denomin)

    def __abs__(self) -> numbers.Number:
        return abs(self.num) / abs(self.denomin)

    def __add__(self, other: Union["ComplexFraction", numbers.Number]) -> "ComplexFraction":
        if type(other) != ComplexFraction:
            if isinstance(other, numbers.Number):
                # noinspection PyTypeChecker
                temp = other * self.denomin
                print(f"Adding {self} to {temp} / {self.denomin}")
                return ComplexFraction(self.num + temp, self.denomin)
            else:
                raise Exception("Wrong adding operand!")
        old_denomin1 = self.denomin
        old_denomin2 = other.denomin
        new_denomin = ComplexFraction.least_common_denomin(self, other)

        new_numerator1 = self.num * new_denomin
        new_numerator2 = other.num * new_denomin

        new_numerator1 = int(new_numerator1.real / old_denomin1) + int(new_numerator1.imag / old_denomin1)*1j
        new_numerator2 = int(new_numerator2.real / old_denomin2) + int(new_numerator2.imag / old_denomin2)*1j

        print(f"Adding {self} == {new_numerator1} / {new_denomin} to {new_numerator2} / {new_denomin} == {other}")

        new_numerator1 += new_numerator2
        return ComplexFraction(new_numerator1, new_denomin)

    def __mul__(self, other: Union["ComplexFraction", numbers.Number]) -> "ComplexFraction":
        if type(other) != ComplexFraction:
            if isinstance(other, numbers.Number):
                # noinspection PyTypeChecker
                return ComplexFraction(self.num * other, self.denomin)
            else:
                raise Exception("Wrong adding operand!")
        return ComplexFraction(self.num * other.num, self.denomin * other.denomin)

    def __truediv__(self, other: Union["ComplexFraction", numbers.Number]) -> "ComplexFraction":
        if type(other) != ComplexFraction:
            if isinstance(other, numbers.Number):
                # noinspection PyTypeChecker
                return ComplexFraction(self.num, self.denomin * other)
            else:
                raise Exception("Wrong adding operand!")
        return ComplexFraction(self.num * other.denomin, self.denomin * other.num)

    def __pow__(self, power: int, modulo=None) -> "ComplexFraction":
        if type(power) != int:
            raise Exception("You may raise ComplexFraction instance only to an integer power!")
        return ComplexFraction(self.num ** power, self.denomin ** power)

    @staticmethod
    def least_common_denomin(frac1: "ComplexFraction", frac2: "ComplexFraction") -> int:
        """
        Returns the least common denominator of two complex fractions - @denomin.setter assures denominator to be
        real integer so it is possible
        """

        x1 = frac1.denomin
        x2 = frac2.denomin

        while x1 != x2:
            if x1 < x2:
                x1 += frac1.denomin
            elif x2 < x1:
                x2 += frac2.denomin

        print(f"The least common denominator of {frac1} and {frac2} is {x1}")
        return int(x1)

    @staticmethod
    def complex_GCD(z1: complex, z2: complex):
        temp = ComplexFraction.greatest_common_divisor(int(z1.real), int(z1.imag))
        temp = ComplexFraction.greatest_common_divisor(int(temp), int(z2.real))
        temp = ComplexFraction.greatest_common_divisor(int(temp), int(z2.imag))
        return temp

    @staticmethod
    def greatest_common_divisor(num1: int, num2: int) -> int:
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        return num1


if __name__ == "__main__":
    print(ComplexFraction(2+1j, 3-1j) + ComplexFraction(7-10j, 30j))
