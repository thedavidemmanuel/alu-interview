#!/usr/bin/python3
'''minimum operations'''

import math

def minOperations(n):
  """
  Calculates the fewest number of operations needed to result in exactly n H characters in a text file.

  Args:
    n: The number of H characters to reach.

  Returns:
    The fewest number of operations needed.
  """

   if n <= 1:
        return 0

    operations = 0
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations
