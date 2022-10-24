from math import gcd

class Rational:

  def __init__(self, numer, denom):
    self.n = numer
    self.d = denom

  def __add__(self, other):
    sum = Rational((self.n*other.d) + (other.n*self.d),self.d * other.d)
    return sum.simp()

  def __sub__(self, other):
    dif = Rational((self.n*other.d) - (other.n*self.d),self.d * other.d)
    return dif.simp()

  def __mul__(self, other):
    prod = Rational((self.n * other.n), (self.d * other.d))
    return prod.simp()

  def __truediv__(self, other):
    temp = other.n
    other.n = other.d
    other.d = temp
    quo = Rational(self.n * other.n, self.d * other.d)
    return quo.simp()

  def simp(self):
    x = gcd(self.n, self.d)
    self.n //= x
    self.d //= x
    return self

  def __repr__(self):
      return f"({self.n}/{self.d})"


def main():
  rat = Rational(3,4)
  rat2 = Rational(2,9)
  print(f"the sum is {rat + rat2}, the difference is {rat - rat2}, the product is {rat * rat2}, and the quotient is {rat / rat2}")


if __name__ == '__main__':
    main()
