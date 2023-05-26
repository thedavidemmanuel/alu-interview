#!/usr/bin/python3
def minOperations(n):
  """
  Calculates the fewest number of operations needed to result in exactly n H characters in a text file.

  Args:
    n: The number of H characters to reach.

  Returns:
    The fewest number of operations needed.
  """

  if n <= 0:
    return 0

  operations = 0
  while n > 1:
    if n % 2 == 1:
      operations += 1
    n //= 2
    operations += 1

  return operations

