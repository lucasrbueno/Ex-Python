def read_file(file):
  with open(file, "r") as inFile:
    for column in inFile:
      yield column

file_list = ["a.txt", "b.txt"]
file_generators = [read_file(path) for path in file_list]

with open("totals.txt", "w+") as outFile:
  while True:
    try:
      outFile.write(f"{sum([int(next(gen)) for gen in file_generators])}\n")
    except StopIteration:
      break