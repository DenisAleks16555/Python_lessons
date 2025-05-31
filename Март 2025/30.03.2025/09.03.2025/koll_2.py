# print("*")
# print("*" * 2)
# print("*" * 3)
# for i in range(1, 11):
    # print("*" * i)
print("Введите размер фигуры:")
count = int(input())

for i in range(1, count + 1):
     print(" " * (count - i), end="")
     print("* " * i)
for i in range(count -1, 0, -1):
      print(" " * (count -i), end="")
      print("* " * i )