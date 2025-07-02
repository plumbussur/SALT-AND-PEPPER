def coincidence(list=None, range=None):
    new_list = []
    if not list or not range:
        return new_list


    start_obj = range.start
    stop_obj = range.stop
    
    for item in list:
        if isinstance(item, (int, float)):
            if start_obj <= item < stop_obj:    
                new_list.append(item)
            
            
    return new_list





#Done