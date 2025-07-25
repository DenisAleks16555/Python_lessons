def is_lucky_number(number):
    #123 456
    left = number // 1000
    right = number % 1000
    # 123
    sum_left = (left // 100) + ((left // 10) % 10) + (left % 10)
    sum_right = (right // 100) + ((right // 10) % 10) + (right % 10)

    
    return sum_left == sum_right #Выдаёт либо False, либо True
    
print(is_lucky_number(123456))
print(is_lucky_number(123420)) #Счастливое число

# number = 123456
# left = number // 1000
# right = number % 1000
# print(left)
# print(right)

def is_lucky_number(number):
    #123 456
    #"123456"
    #['1', '2', '3', '4', '5', '6']
    #[1, 2, 3, 4, 5, 6]
    #sum(ls[:3] == sum(ls[3:]
  
    ls = [int(i) for i in str(number)]
    return sum(ls[:3]) == sum(ls[3:])

      
print(is_lucky_number(123456))
print(is_lucky_number(123420)) #Счастливое число

   