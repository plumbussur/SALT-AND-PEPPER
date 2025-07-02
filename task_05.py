from datetime import datetime, timedelta

def date_in_future(integer):
    
    now = datetime.now()


    if isinstance(integer, int):
        
        delta = timedelta(days = integer)
        
        new_date = now + delta
        
        new_date = new_date.strftime("%d-%m-%Y %H:%M:%S")
        return new_date 
    else:
        now = now.strftime("%d-%m-%Y %H:%M:%S")
        return now
    

    
print(date_in_future(2))      
        

#Done
