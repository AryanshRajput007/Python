class Solution(object):

  def divide(self, dividend, divisor):
    """
      :type dividend: int
      :type divisor: int
      :rtype: int
      """
    if dividend == 0:
      return 0
    negative = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    result = 0
    while dividend >= divisor:
      temp, multiple = divisor, 1
      while dividend >= (temp << 1):
        temp <<= 1
        multiple <<= 1
      dividend -= temp
      result += multiple
    if negative:
      result = -result
    return min(max(-2147483648, result), 2147483647)
