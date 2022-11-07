from math import gcd

class Rational:

  def __init__(self, numer, denom):
    self.n = numer
    self.d = denom
    if self.d == 0:
      raise ValueError('divided by 0')

  def __add__(self, other):
    if type(other) is int:
        other = Rational(other, 1)
    sum = Rational((self.n*other.d) + (other.n*self.d),self.d * other.d)
    return sum.simp()

  def __radd__(self, other):
    return self + other

  def __sub__(self, other):
    if type(other) is int:
        other = Rational(other, 1)
    dif = Rational((self.n*other.d) - (other.n*self.d),self.d * other.d)
    return dif.simp()

  def __rsub__(self, other):
    return self - other

  def __mul__(self, other):
    if type(other) is int:
        other = Rational(other, 1)
    prod = Rational((self.n * other.n), (self.d * other.d))
    return prod.simp()

  def __rmul__(self, other):
    return self * other

  def __truediv__(self, other):
    if type(other) is int:
        other = Rational(other, 1)
    temp = other.n
    other.n = other.d
    other.d = temp
    quo = Rational(self.n * other.n, self.d * other.d)
    return quo.simp()

  def __rtruediv__(self, other):
    return self / other

  def simp(self):
    if self.n == 0:
      return 0
    else:
      x = gcd(self.n, self.d)
      self.n //= x
      self.d //= x
      if self.d == 1:
        return self.n
      return self

  def __repr__(self):
      return f"{self.n}/{self.d}"


def main():
  rat = Rational(2,5)
  rat2 = Rational(1,4)
  print(f"the sum is {rat + rat2}, the difference is {rat - rat2}, the product is {rat * rat2}, and the quotient is {rat / rat2}")


if __name__ == '__main__':
    main()
