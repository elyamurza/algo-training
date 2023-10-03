"""
Finds the greatest common denominator (GCD) of two integers.

Example: GCD of 20 and 8 is 4 (because 8/4 is 2; and 20/4 is 5)

How it works: 

For two integers a and b, where a > b, divide a by b.
If the remainder, r, is 0, then stop: GCD is b.
Otherwise, set a to b, b to r, repeat at step 1 until r is 0
"""

def gcd(a, b):
  while (b != 0):
    t = a
    a = b
    b = t % b

  return a


print(gcd(60, 96))
print(gcd(20, 8))