import decimal as dc
import math as mt

# takes a binary string, a desired number of decimal digits to use during
# calculations (input of 0 here means no additional limit on digits), and last
# input is 0 for chopping and 1 for rounding  
def machine_to_decimal_digits(binStr, digits, rounding):

  # s is sign, uses first bit
  s = (-1)**int(binStr[0])

  # c is exponent, uses second through twelfth bits
  # It is a binary integer, so I look from left to right doubling the running
  # sum before I add each new bit. I apply this exponent to 2, according to the
  # definition of floats
  c = int(binStr[1])
  for i in range(2, 12):
    c = c*2 + int(binStr[i]) - 1
    # anywhere with this digits conditional is an instance of chopping or
    # rounding being applied. I do it after every calculation
    if(digits > 0):
      c = number_digits(c, digits, rounding)
  c = 2**c
  if(digits > 0):
    c = number_digits(c, digits, rounding)
  
  # f is the mantissa, uses all remaining bits
  # I don't append 0s, but because of the definition of the mantissa, the first
  # bit is always 1/2 i.e. it encodes the fraction of a binary number. I iterate
  # from right to left, adding each new bit to the total, and then halving the
  # running sum. I make sure to add 1 because of how floats are calculated
  f = 0
  for i in range( len(binStr) - 1, 11, -1):
    f = .5 * (f + int(binStr[i]) )
    if(digits > 0):
      f = number_digits(f, digits, rounding)
  f += 1
  if(digits > 0):
    f = number_digits(f, digits, rounding)

  # multiplying all the parts of the float together
  n = s * c * f
  if(digits > 0):
    n = float(number_digits(n, digits, rounding))
  return n

# this applies chopping or rounding to a positive float by multiplying it, then
# casting to int. Takes the number, a desired number of decimal digits to use
# during calculations (input of 0 here means no additional limit on digits), and
# last input is 0 for chopping and 1 for rounding
def number_digits(number, digits, rounding):
  exp = 0
  while number < 10**(digits-1):
    number *= 10
    exp -= 1
  while number > 10**digits:
    number *= .1
    exp += 1
  return int(number + rounding * .5) * 10**exp

# algorithm for calculating maximum minimum terms for bisectional root-finding
# matched with expected output. No need in this case to use actual algorithm
# though there would be other cases where bisection might produce the exact zero
# before reaching this number
def min_terms_bisection(iniMin, iniMax, maxErr):
  return int( mt.log( (iniMax - iniMin) / maxErr, 2) ) + 1

# an implementation of newton's algorithm that returns the iteration count
# instead of the approximated root. FuncStr is a string representing the function.
# derivStr is the derivative of this function. x is the initial approximation.
# maxErr is the maximum error allowed, and maxIter is the number of iterations
# before the function will return a failure.
def newtons_method_calc_iterations(funcStr, derivStr, x, maxErr, maxIter):
  i = 0
  while i < maxIter:
    if(eval(derivStr) == 0):
      print("derivative 0, couldn't find solution")
      return 0
    if(eval(funcStr) == 0):
      return i
    newX = x - eval(funcStr) / eval(derivStr)
    i += 1
    if(abs(x - newX) < maxErr):
      return i
    x = newX
  print("max iterations reached, couldn't find solution")
  return 0

# problem 1, check function for explanation
exact = machine_to_decimal_digits('010000000111111010111001', 0, 0)
print(exact, end='\n\n')

# problem 2, check function for explanation
print(machine_to_decimal_digits('010000000111111010111001', 3, 0), end='\n\n')

# problem 3, check function for explanation
approx = machine_to_decimal_digits('010000000111111010111001', 3, 1)
print(approx, end='\n\n')

# problem 4.1, per definition of absolute error
absError = approx - exact
print(absError)

# problem 4.2, per definition of relative error
print(dc.Decimal(absError) / dc.Decimal(exact), end='\n\n')

# problem 5
# by inspection, problem given is an infinite summation with alternating terms
# of decreasing absolute value. Number of terms to reach desired accuracy can be
# found by setting the absolute value of the interior of the summation to be
# less than the accuracy desired. Since problem is for f(1), the x**k term
# is equivalent to 1 and the calculation is simplified greatly.
x = 1
maxErr = 10**-4
print(int( (x / (maxErr))**(1/3) - 1 ) + 1, end='\n\n')

# problem 6.1, check function for explanation
print(min_terms_bisection (-4, 7, 10**-4), end='\n\n')

# problem 6.2, check function for explanation
print(newtons_method_calc_iterations("x**3 + 4*x**2 - 10", "3*x**2 + 8*x", -4, 10**-4, 100), end ='\n\n')
