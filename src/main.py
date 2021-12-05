class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            raise ValueError("Num is not in range from 0 to prime number")
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        if other is None:
            return True
        return not (self.num == other.num) and not (self.prime == other.prime)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two Finite Fields of a different prime numbers')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two Finite Fields of a different prime numbers')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two Finite Fields of a different prime numbers')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two Finite Fields of a different prime numbers')
        num = pow(self.num, other.num - 2, self.prime)
        return self.__class__(num, self.prime)
