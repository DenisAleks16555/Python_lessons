fl = open("_writelines.txt", "w", encoding="utf-8")

lst = [f'{i}. _____________________\n' for i in range(1,11)]
fl.writelines(lst)
fl.close()