def sort_list(list = None):
    if not list:
        return list

    max_num = max(list)
    min_num = min(list)
    
    for position in range(len(list)):
        if list[position] == max_num:
            list[position] = min_num
                
        elif list[position] == min_num:
            list[position] = max_num
    
    list.append(min(list))
    return list            
print(sort_list([1, 2, 1, 3]))


#Done      
        
    
     
    
            
        
             
        