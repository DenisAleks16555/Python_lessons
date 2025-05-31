lst = [0.3, 0.76, 1.22, 0.05, 1.5]
# lst = list(map(lambda number: int(number * 100), lst))
# lst = list(map(lambda x: str(int(x * 100)) + '%', lst))
lst = list(map(lambda x: f"{int(x * 100)}%", lst))
print(lst) 
# '30' + '%' => '30%'
# lst = [30%, 76, 122, 5, 150]
ls = ["30%", '76%', '122%', '5%', '150%']
ls = list(map(lambda x: int(x[:-1]) /100,ls))
print(ls)

