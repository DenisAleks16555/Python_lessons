fl = open("task2.txt", "w", encoding="utf-8")
for i in range(1,10):
    for j in range(1,11):
       fl.write(f"{i} x {j} = {j*i}\n")
    fl.write("\n")
fl.close