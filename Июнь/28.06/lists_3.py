def save_div(a,b):
    
    try:
       
        return a/b
        
    except ZeroDivisionError:
        return"На ноль делить нельзя"
print(save_div(2,0))
print(save_div(2,6))


