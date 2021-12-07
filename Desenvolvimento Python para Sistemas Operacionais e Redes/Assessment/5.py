def read_file(file):
  with open(file, "r") as inFile:
    for column in inFile:
      yield column

file_list = ["a.txt", "b.txt"]
file_generators = [read_file(path) for path in file_list]


# def countList(file_list):
#     if len(file_list[0]) > len(file_list[1]):
#         index = len(file_list[0]) - len(file_list[1])
#         while index != 0:
#             listB.append('0')
#             index -= 1
#     else:
#         index = len(listB) - len(listA)
#         while index != 0:
#             listA.append('0')
#             index -= 1
#     return listA, listB

# def itemsAddUp(file_list[0], file_list[1]):
#     for i in range(len(listA)):
#         print(f"{listA[i]} + {listB[i]} = {int(listA[i]) + int(listB[i])}")


with open("totals.txt", "w+") as outFile:
  while True:
    try:
      outFile.write(f"{sum([int(next(gen)) for gen in file_generators])}\n")
    except StopIteration:
      break