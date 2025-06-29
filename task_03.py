def max_odd(array):
    
    max_odd_value = None
    
    
    for item in array:
        if isinstance(item, (int, float)):
            if isinstance(item, int) or (item.is_integer()):
                num = int(item)
                if num % 2 != 0:
                    if max_odd_value is None or item > max_odd_value:
                    
                        max_odd_value = num
                    
            
        
    return max_odd_value   

print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))

    
    
#Done