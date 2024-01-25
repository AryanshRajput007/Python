# def converter(nums):
#   a = int(nums)
#   b = float(nums)
#   c = str(nums)
#   d = bool(nums)
#   e = complex(nums)
#   print(a)
#   print(type(a))
#   print(b)
#   print(type(b))
#   print(c)
#   print(type(c))
#   print(d)
#   print(type(d))
#   print(e)
#   print(type(e))

# converter(input("Enter a number: "))
# nums = complex(input("Enter a number: "))
# num = bool(input("Enter a number: "))
# print(num)

# a = 10
# print(id(a))
# a = a + 10
# print(a)
# print(id(a))
# b = 10
# c = 10
# print(a is b is c)
# print(id(a), id(b), id(c))

x = 'ab', 'cd', 'ef'
print(x)
print(type(x))

my_list = [int(x) for x in input("Enter the values separated by space: ").split(" ")]
print(my_list)

from array import array
# lst = [int(x) for x in input("Enter the value separated by space: ").split()]
my_list = [10, 20, 30, 40, 50]
my_list.insert(3, 70)
print(type(my_list))
print(my_list)
print(max(my_list))
print(my_list.count(50))
print(min(my_list))
print(my_list.index(30))
my_list.remove(70)
print(my_list)
print(my_list[::-1])
my_list.reverse()
print(my_list)
print(id(my_list))
sorted_list = sorted(my_list)
print(sorted_list)

# new_list = ure
# for i in range(len(new_list)):
#     if isinstance(new_list[i], list):
#         for j in range(len(new_list[i])):
#             print(new_list[i][j])
#     elif isinstance(new_list[i], set):
#         print(', '.join(new_list[i]))
#     else:
#         print(new_list[i])

arr = array('i', [1,2,3,4,5])
print(arr)

lst = [10, 20, 30, 40]
lst[1] = 70
print(lst)
lst2 = lst
lst2.extend(my_list)
print(id(lst))
print(id(lst2))
print(lst2)
print(lst)
print(lst[1:4])

for i in range(len(lst)):
  print(lst[i:])

for i in range(len(lst)):
  print(lst[:i])

# list = [1,2,3,1,1,1,7,8,1]
# list.remove(3)
# print(list)
# # for i in range(len(list)):
# #   if list[i] == 1:
# #     list[i] = 10
# # print(list)
# for i in range(len(list) // 2):
#   if list [i] == 1:
#     list[i] = 10
#   if list[len(list) - i - 1] == 1:
#     list[len(list) - i - 1] = 10
# print(list)

# n = "shark"
# x = [x for x in n]
# print(x)
# s = "abcabcbb"
# list = []
# for i in range(len(s)):
#   if s[i] not in list:
#     list.append(s[i])
# result = len(list)

# list = [int(x) for x in input().split()]
# list = [10 if x == 1 else(20 if x == 2 else x)  for x in list]
# print(list)

# for i in range(len(list) // 2):
#   if list [i] == 1:
#     list[i] = 10
#   if list[len(list) - i - 1] == 1:
#     list[len(list) - i - 1] = 10

# list = []
# n = int(input("Enter the number of elements: "))
# for i in range(n):
#   list.append(int(input("Enter the element: ")))
#   if list[i] == 1:
#     list[i] = 10
#   if list[i] == 2:
#     list[i] = 20
# print(list)

# def func():
#   list = []
#   n = int(input("Enter the number of elements: "))
#   for i in range(n):
#     list.append(int(input("Enter the element: ")))
#     list [i] = (list[i] % 10) * 10
#   return list

# print(func())

# n = 5
# list = [x for x in range(n)]
# print(list)

# list = [int(x) for x in input("Enter the values seperated by spaces: ").split()]
# list2 = [x for x in list if x % 2 == 0]
# print("The even list is: ",list2)
# list3 = [x for x in list if x % 2 != 0]
# print("The odd list is: ", list3)

# t = (10, 20, 30, 40)
# t = t + (300,)  
# t = t[:t.index(10)] + t[t.index(10)+1:]
# print(t)
# print(id(t))
# print(type(t))
# t2 = (10,)
# print(t2[0])

# words = ("apple", "banana", "cherry")
# for index, word in enumerate(words, start = 1):
#     print(f"Word {index}: {word}")

# my_set = [3, 1, 2, 3, 4, 5, 1, 2]
# print(set(my_set))
# list1 = [1, 2, 2, 3]
# list2 = ["abc", "xyz", "abc", "rzy"]
# map = {}

# for i in range(len(list1)):
#   if list1[i] not in map:
#     map[list1[i]] = []
#   map[list1[i]].append(list2[i])
# print(map)

# s = set({})
# print(type(s))

# set1 = {15,20,25}
# set2 = {30,40,50}
# set1.add(10)
# if 0 in set1:
#     set1.remove(0)
# print(set1.union(set2))
# print(set1)
# print(set1.intersection(set2))

# set3 = {"Nanimo", "Bankai", "Gotei", 13, ("Ichigo", "Ken", "Saitama")}
# print(set3)
# for i in enumerate(set3, start = 1):
#   print(f"{i}")

#Set Operations
# Union of three sets (combining all unique elements)
# set1 = {1, 2, 3, 4, 5}
# set2 = {10, 20, 30, 40, 50}
# set3 = {100, 200, 300, 400, 500}
# set4 = set1.union(set2, set3)  # set1 | set2 | set3
# print("Union:", set4)

# # Intersection of three sets (common elements)
# set5 = set1.intersection(set2, set3)
# print("Intersection:", set5)

# # Update set1 with the union of set2 and set3
# set1.update(set2, set3)
# print("Updated set1:", set1)

# # Add 60 to set2
# set2.add(60)
# print("Updated set2:", set2)

# # Update set3 with a new set {600, 700, 800}
# set3.update({600, 700, 800})
# print("Updated set3:", set3)

# # Remove 100 and 200 (if present) from set3
# set3.discard(100)
# set3.remove(200 if 200 in set3 else "Not Found")
# print("Updated set3 after removal:", set3)

# # Clear all elements from set3
# set3.clear()
# print("Cleared set3:", set3)

# # Copy set2 to set3
# set3 = set2.copy()
# print("Copied set3 from set2:", set3)

# # Print the ID of set3 and pop an arbitrary element
# print("ID of set3:", id(set3))
# print("Popped element from set3:", set3.pop())

# # Difference between two sets (elements in set1 but not in set2)
# my_set1 = {10, 20, 30, 40}
# my_set2 = {50, 60, 70, 80, 40}
# my_set3 = my_set1.difference(my_set2)
# print("Difference between set1 and set2:", my_set3)

# # Symmetric difference (elements not common to both sets)
# my_set6 = my_set2.difference(my_set1)
# print("Symmetric difference between set2 and set1:", my_set6)

# # Intersection of two sets (common elements)
# my_set4 = my_set1.intersection(my_set2)
# print("Intersection of set1 and set2:", my_set4)

# # Symmetric difference of two sets (elements not common to both sets)
# my_set5 = my_set1.symmetric_difference(my_set2)
# print("Symmetric difference between set1 and set2:", my_set5)

# # Intersection update of set1 with set2 (common elements)
# my_set1.intersection_update(my_set2)
# print("Intersection update of set1 with set2:", my_set1)

# my_set3.symmetric_difference_update(my_set4)
# print("Symmetric difference update of set3 and set4:", my_set3)

# # Unique name of the set
# my_set = {1, 2, 3, 4, 5}

# # Implementing subset, superset, min, max, len, list(enumerate()), sum and disjoint of sets
# subset_set = {1, 2, 3}
# superset_set = {1, 2, 3, 4, 5}
# min_value = min(my_set)
# max_value = max(my_set)
# length = len(my_set)
# enumerated_list = list(enumerate(my_set))
# sum_value = sum(my_set)
# disjoint_set = {6, 7, 8}

# print("Subset:", subset_set.issubset(my_set))
# print("Superset:", superset_set.issuperset(my_set))
# print("Minimum value:", min_value)
# print("Maximum value:", max_value)
# print("Length:", length)
# print("Enumerated list:", enumerated_list)
# print("Sum:", sum_value)
# print("Disjoint:", disjoint_set.isdisjoint(my_set))

# my_set7 = sorted(my_set, reverse=True)
# print("Sorted set: ", my_set7)

# list1 = [1, 2, 3, 4, 'ab', 6]
# list1 = list1[::-1]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six']
# list2 = list2[::-1]
# map = dict()

# while list1:
#     map[list1.pop()] = list2.pop()

# print("Map:", map)

# print("The keys are: ", map.keys())
# print("The values are: ", map.values())
# print("The items are: ", map.items())

# for key, value in map.items():
#     print(key, value)

# for key in map.keys():
#     print(key)

# for key, value in map.items():
#     print(value)

# list1 = ['one', 'two', ['Bankai', 'Senbunzakara', 'Kageyoshi'], ['Bankai', 'Tensa', 'Zangetsu']]
# list2 = [1, 2, 3, 4]
# hashmap = {}
# for i in range(len(list1)):
#   hashmap[list2[i]] = list1[i]
# print(hashmap)

# keys = {'a', 'b', 'c', 'd'}
# values = [10, 20, 30, 40]
# mydict = dict.fromkeys(keys, values)
# print(mydict)
# values.append(50)
# print(mydict)

# # Create a dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# # Get the keys, values, and items of the dictionary
# keys = my_dict.keys()
# values = my_dict.values()
# items = my_dict.items()

# # Print the keys, values, and items
# print("Keys:", keys)
# print("Values:", values)
# print("Items:", items)

# # Accessing a value for a given key using get function
# value_of_a = my_dict.get('a')
# print("Value of 'a':", value_of_a)

# # Adding a new key-value pair to the dictionary
# my_dict['d'] = 4
# print("Updated Dictionary:", my_dict)

# # Removing a key-value pair from the dictionary
# removed_value = my_dict.pop('b')
# print("Dictionary after removing 'b':", my_dict)
# print("Removed value:", removed_value)

# my_dict.popitem()
# print("Dictionary after popitem() function: ", my_dict)

# new_dict = {('abx', 'cder'): 1}
# print(new_dict)

# my_dict2 = {'Name': 'Ichigo', 'Age': 13, 'City': 'Nanimo'}
# for i in my_dict2.values():
#   print(i)

# for i in my_dict2.keys():
#   print(i)

# for i in my_dict2.items():
#   print(i)

# ap = 'Name' in my_dict2
# print(ap)

# my_dict3 = {'key': False}
# apr = all(my_dict3.values())
# print(apr)  # This will print False

# my_dict4 = {'key': True}
# apr2 = any(my_dict4)
# print(apr2)

# my_dict5 = {i : i * 2 for i in range(1, 6)}
# my_dict5 = {key: value for key, value in (input().split() for _ in range(5))}
# print(my_dict5)

# my_dict5 = {}
# while True:
#     try:
#         key, value = input("Enter a key-value pair separated by a space: ").split()
#         my_dict5[key] = value
#     except ValueError:
#         break

# print("Dictionary:", my_dict5)

# list21 = ['one', 'two', 'three', 'four']
# list31 = [1,2,3,4]

# my_dict7 = dict(zip(list21, list31)) # {k : v for k, v in zip(list1, list2)}
# print(my_dict7)

# print(type(zip(list21, list31)))

# my_dict8 = {'a': 10, 'b': 20, 'c': 30}
# my_dict8 = {k : v / 10 for k, v in my_dict8.items()}
# print(my_dict8)

# my_dict9 = {'a': 1, 'b': 2, 'c': 3}
# for index, (key, value) in enumerate(my_dict9.items()):
#     print(f"Index: {index}, Key: {key}, Value: {value}")

# a = 10
# b = 20
# c = a + b
# print("The sum of {1} and {0} is {2}".format(a, b, c))

# def add(*args):
#   return sum(args)

# print(add(1,2,3,4,5,6,7,8,9,10))

# def UserDetail(**kwargs):
#   print(kwargs)

# UserDetail(name = 'Ichigo', age = 13, city = 'Nanimo')

# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# class Solution:
#   def __init__(self, nums):
#     self.nums = nums
#   def insert(self, head):
#     for i in range(len(self.nums)):
#       if i == 0:
#         head = Node(self.nums[i])
#         temp = head
#       else:
#         temp.next = Node(self.nums[i])
#         temp = temp.next
#     return head
#   def display(self, head):
#     while head:
#       print(head.data)
#       head = head.next

# if __name__ == "__main__":
#   nums = [1,2,3,4,5]
#   head = None
#   obj = Solution(nums)
#   head = obj.insert(head)
#   obj.display(head)

# class Employee:
#   def Create(name, emp_id):
#     Employee.n = name
#     Employee.e = emp_id
#     print(id(Employee.n))
#     print(id(Employee.e))

# Employee.Create("Aryansh", 266)

# Inheritance :-

# class Person:
#   def __init__(self, name, age, gender):
#       self.name = name
#       self.age = age
#       self.gender = gender

#   def display_info(self):
#       print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


# class Student(Person):
#   def __init__(self, name, age, student_id):
#       super().__init__(name, age, "Male")
#       self.student_id = student_id

#   def display_info(self):
#       super().display_info()
#       print(f"Student ID: {self.student_id}")


# class Teacher(Person):
#   def __init__(self, name, age, employee_id):
#       super().__init__(name, age, "Female")
#       self.employee_id = employee_id

#   def display_info(self):
#       super().display_info()
#       print(f"Employee ID: {self.employee_id}")

# student1 = Student("Aryansh", 18, "S12345")
# teacher1 = Teacher("Kush", 35, "T78901")

# print("Student Information:")
# student1.display_info()
# print("\nTeacher Information:")
# teacher1.display_info()

# s = "Book"
# length = len(s) // 2
# list = ['a','e','i','o','u']
# left = 0
# right = 0
# leftstring = s[:length]
# rightstring = s[length:]
# for i in range(length):
#   if leftstring[i] in list:
#     left += 1
#   if rightstring[i] in list:
#     right += 1
# print(left == right)

# addition = lambda x, y: x + y
# substraction = lambda x, y: x - y
# multiplication = lambda x, y: x * y
# division = lambda x, y: x / y if y != 0 else "Division by zero error"
# print(addition(5, 3))
# print(substraction(5, 3))
# print(multiplication(5, 3))
# print(division(5, 3))

# def product(nums):
#   total = 1
#   for num in nums:
#     total *= num
#   return total

# res1 = (lambda **kwargs: product(kwargs.values()))
# print(res1(a=5, b=4, c=3))
# print(res1(a=5, b=4, c=3, d=2))

# def add(n):
#   return lambda a : a + n

# add5 = add(5)
# print(add5(3))

# class Solution:
#     factorial = lambda self, n: 1 if n == 0 else n * self.factorial(n-1)

# def main():
#     obj = Solution()
#     result = obj.factorial(5)
#     print(result)

# main()

# class Parent1:
#   def method1(self):
#     print("This is method 1 from Parent1")

# class Parent2:
#   def method2(self):
#     print("This is method 2 from Parent2")

# class Subclass(Parent1, Parent2):
#   def method3(self):
#     print("This is method 3 from Subclass")

# obj = Subclass()
# obj.method1()
# obj.method2()
# obj.method3()

# class Person():
#   def __init__(self, name, gender, age):
#     self.name = name
#     self.gender = gender
#     self.age = age

#   def display_info(self):
#     print(f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}")

# class Employee(Person):
#   def __init__(self, name, gender, age, emp_id, salary):
#     super().__init__(name, gender, age)
#     self.emp_id = emp_id
#     self.salary = salary

#   def display(self):
#     super().display_info()
#     print(f"Emp_Id: {self.emp_id}, Salary: {self.salary}")

# class Permanent(Employee):
#   def __init__(self, name, gender, age, emp_id, salary, bonus):
#     super().__init__(name, gender, age, emp_id, salary)
#     self.bonus = bonus

#   def display(self):
#     super().display()
#     print(f"Bonus: {self.bonus}")

# class Temporary(Employee):
#   def __init__(self, name, gender, age, emp_id, salary, hours):
#     super().__init__(name, gender, age, emp_id, salary)
#     self.hours = hours

#   def display(self):
#     super().display()
#     print(f"Emp_Id: {self.emp_id}, Salary: {self.salary}, Hours: {self.hours}")

# PermanentEmp = Permanent("Aryansh", "Male", 18, "E12345", 50000, 5000)
# TemporaryEmp = Temporary("Kush", "Male", 35, "E78901", 30000, 8)

# print("Permanent Employee:")
# PermanentEmp.display()

# print("\nTemporary Employee:")
# TemporaryEmp.display()


# class Solution:
#     def __init__(self):
#         self.result = 10 + 20
#         return self.result

# obj = Solution()
# print(obj)

# class ClassA:
#   def method_in_class_a(self, obj):
#       # Do something with the object
#       print(f"Method in ClassA received object: {obj}")

# class ClassB:
#   def method_in_class_b(self):
#       # Create an instance of ClassA
#       obj_a = ClassA()

#       # Call the method_in_class_a of ClassA and pass an object
#       obj_a.method_in_class_a("Hello from ClassB")

# # Create an instance of ClassB
# obj_b = ClassB()

# # Call the method_in_class_b of ClassB
# obj_b.method_in_class_b()

# class Solution:
#   def display(self):
#       print("Printing the method of Class A")

# class Sol:
#   def display(self):
#       print("Printing the method of Class B")

# class NewSol(Solution, Sol):
#   def display_all(self):
#     super().display()
#     super(Solution, self).display()  
#     Sol.display(self) 


# new_sol_instance = NewSol()
# new_sol_instance.display_all()


# class Father:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def display(self):
#     print(f"Name: {self.name}, Age: {self.age}")

# class Mother:
#   def __init__(self,name, age, gender):
#     super().__init__(name, age)
#     self.gender = gender
#   def display(self):
#     print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

# class Child(Mother, Father):
#   def __init__(self, name, age, gender, address):
#       super().__init__(name, age, gender)
#       self.address = address

#   def display(self):
#       print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}")

# child = Child("Aryansh", 18, "Male", "India")
# child.display()

# class Solution:
#   def sum(self, a, b):
#     return a +b
#   def sum(self, a, b, c):
#     return a + b + c

# obj = Solution()
# obj.sum(10, 20)
# obj.sum(10, 20, 30)

# class Parent:
#     def method(self):
#         print("This is the parent's method")

# class Child(Parent):
#     def method(self):
#       print("This is the child's overridden method")
#       super().method()

# child = Child()
# child.method()

# class Cat:
#     def sound(self):
#         print("Meow")

# class Dog:
#     def sound(self):
#         print("Woof")

# def make_sound(animal):
#     animal.sound()

# cat = Cat()
# dog = Dog()

# make_sound(cat)
# make_sound(dog)

# class Solution:
#   def sum(self, a, b):
#     print(a + b)

# class child:
#   def sum(self, a, b, c):
#     print

# def sum_two_numbers(a, b):
#   return a + b

# def sum_three_numbers(a, b, c):
#   return a + b + c

# result_two_numbers = sum_two_numbers(10, 5)
# result_three_numbers = sum_three_numbers(10, 5, 3)

# print(f"Sum of two numbers: {result_two_numbers}")
# print(f"Sum of three numbers: {result_three_numbers}")

# class SubClass():
#   def sum(self, a, b):
#     return a + b
#   def sum(self, a, b, c):
#     return a + b + c

# obj = SubClass()

# result1 = obj.sum(10, 5)
# result = obj.sum(10, 5, 3)

# print(f"Sum using overridden method: {result}")

# class test:
#   def __init__(self, i):
#     self.i = i
#   def __str__(self):
#     return self.i

# d = test("abc")
# print(d)


# def name(title, name, greeting="Hello"):
#   return f"{greeting} {title} {name}!"

# # positional arguments
# print(name("Dr", "Smith"))

# # Keyword Arguments
# print(name(name = "Smith", title = "Prof"))

# # Default Arguments
# print(name("Mr", "Brown"))

# # All combined
# print(name("Mr", "Brown", greeting="Good Morning"))

# from abc import ABC, abstractmethod

# class NameGenerator(ABC):
#     @abstractmethod
#     def generate_name(self, title, name, greeting="Hello"):
#         pass

# class ConcreteNameGenerator(NameGenerator):
#     def generate_name(self, title, name, greeting="Hello"):
#         return f"{greeting} {title} {name}!"

# # Instantiate the concrete class
# name_generator = ConcreteNameGenerator()

# # positional arguments
# print(name_generator.generate_name("Dr", "Smith"))

# # Keyword Arguments
# print(name_generator.generate_name(name="Smith", title="Prof"))

# # Default Arguments
# print(name_generator.generate_name("Mr", "Brown"))

# # All combined
# print(name_generator.generate_name("Mr", "Brown", greeting="Good Morning"))

# class Parent:
#   def show(self, a):
#     print(a)

# class Child(Parent):
#   def show(self, a, b):
#     print(a, b)

# obj = Child()
# obj.show(10, 20)
# obj.show(10)

# class Employee1:
#   def name(self):
#     print("Ichigo")
#   def age(self):
#     print("22")

# class Employee2:
#   def name(self):
#     print("Kurosaki")
#   def age(self):
#     print("25")

# def func(obj):
#   obj.name()
#   obj.age()

# obj_emp1 = Employee1()
# obj_emp2 = Employee2()

# func(obj_emp1)
# func(obj_emp2)

# class A:
#   def sum(self, *args):
#     #print(type(args))
#     print(None) if len(args) == 0 else print(args)
#     print(sum(args))

# obj = A()
# print("First Iteration")
# obj.sum(10, 20)
# print("Second Iteration")
# obj.sum(10, 20, 30)
# print("Third Iteration")
# obj.sum()

# class Test:
#   def __init__(self):
#     self.a = 10
#     self.b = 20

#   def m1(self):
#     self.c = 30
#     self.d = 40
#     return self.c, self.d


# if __name__ == "__main__":
#   t1 = Test()
#   print(t1.__dict__)
#   t2 = Test()
#   print(t2.__dict__)
#   t1.m1()
#   print(t1.m1())
#   t2.m1()
#   print("After calling instance method m1(): ", t2.__dict__)
#   t1.c = 300
#   print("After calling instance method m1(): ", t1.__dict__)

# class Test:
#   def sum(self, a = None, b = None, c = None):
#     if a != None and b != None and c != None:
#       print("The sum of 3 No.: ", a + b + c)
#     elif a != None and b != None:
#       print("The sum of 2 No.: ", a + b)
#     else:
#       print("Enter atleast 2 No.")

# t = Test()
# t.sum(10, 20, 30)
# t.sum(10, 20)
# t.sum(10)

# class Test():
#   def property(self):
#     print("cash + land + gold + power")
#   def fun(self):
#     print("Have Fun")

# class child(Test):
#   def fun(self):
#     super().fun()
#     print("Sleep")

# c = child()
# c.fun()
# c.property()

# from abc import ABC, abstractmethod
# class empolyee(ABC):
#   def emp_id(self, id, name, age, salary):
#     pass
# class childEmployee(empolyee):
#   def emp_id(self, id):
#     print("Employee ID: ", id)

# emp = childEmployee()
# emp.emp_id(101)


# f = open('Coma Notes.txt', mode = 'r')
# data = f.readlines()
# print(type(data))
# # print(data)
# for element in data:
#   print(element)
# f.close()

# import sys

# randomlist = ['a', 0, 1]
# for entry in randomlist:
#   try:
#     print("The entry is: ", entry)
#     r = 1/int(entry)
#     break
#   except:
#     print("Oops!", sys.exc_info()[0], "occured.")
#     print("Next entry.")
#     print()
# print("The reciprocal of", entry, "is", r)

# n = 99
# r = 5
# count = 0
# while n > r:
#   n = n - r
#   count += 1
# if (n != 0 and n < r):
#   count += (n/r)
# print(count)

# class MyException(Exception):
#   def __init__(self, message):
#     self.message = message

#   def __str__(self):
#     return f'Custom Exception: {self.message}'

# num = int(input("Enter a number greater than 10: "))
# if num <= 10:
#   raise MyException("Number should be greater than 10")
# else:
#   print("Number is greater than 10")

#SpecialException(Exception):
#   def __init__(self, message):
#     self.message = message

#   def __str__(self):
#     return f'Custom Exception: {self.message}'

# num = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num2 == 0:
#     raise SpecialException("Second number cannot be zero")
# else:
#     print(num/num2)

# import sys

# randomlist = ['a', 0, 1, 7]
# for entry in randomlist:
#   try:
#     print(entry)
#     print("The entry is: ", entry)
#     r = 1/int(entry)
#     break
#   except:
#     print("Oops!", sys.exc_info()[0], "occured.") # Here we can use 0 index for the exception type and 1 index for the exception value and 2 index for the traceback
#     print("Next entry.")
#     print()
# print("The reciprocal of", entry, "is", r)
# finally:
#     print("Finally!")

# class ValueTooSmallError(Exception):
#   pass

# class ValueTooLargeError(Exception):
#   pass

# number = 10
# while True:
#   try:
#     i_num = int(input("Enter a number: "))
#     if i_num < number:
#       raise ValueTooSmallError
#     elif i_num > number:
#       raise ValueTooLargeError
#     break
#   except ValueTooSmallError:
#     print("This value is too small, try again!")
#     print()
#   except ValueTooLargeError:
#     print("This value is too large, try again!")
#     print()
# print("Congratulations! You guessed it correctly!")
