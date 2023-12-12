def min_counter(pages, number_of_books, number_of_students):
  if number_of_books < number_of_students:
    return -1

  if number_of_students == 1:
    return sum(pages)

  temp = number_of_books - number_of_students + 1

  pages.sort()
  result = 0

  for i in range(temp):
    result += pages[i]

  return result


number_of_books = int(input("Enter the numbers of books: "))
number_of_pages = [
  int(x) for x in input("Enter the number of pages: ").split()
]
number_of_students = int(input("Enter the number of students: "))

result = min_counter(number_of_pages, number_of_books, number_of_students)
print(result)
