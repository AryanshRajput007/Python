# a = int(input("Enter the range to find factorial :"))
# fact = 1
# for i in range(1, a+1):
#   fact *= i
# print(fact)


def fact(a):
  fact = 1
  for i in range(1, a + 1):
    fact *= i
  print(fact)


x = int(input("Enter the number whose factorial you want : "))
fact(x)
