def coincidence(list, range):
    new_list = []
    
    start_obj = range.start
    stop_obj = range.stop
    
    for item in list:
        if isinstance(item, (int, float)):
            if start_obj <= item < stop_obj:    
                new_list.append(item)
            
            
    return new_list


print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))


#Done