def multiply_numbers(inputs = None):

    x = 1
    
    if isinstance(inputs, (str, list)):

        for number in inputs:

            if isinstance(number, int):
                x *= number
            

            elif number.isdigit() == True:
                x *= int(number)


        if x == 1:
            return None

        return x

    elif isinstance(inputs, float):
        numbers = str(inputs)

        for number in numbers:
            if number.isdigit() == True:
                x *= int(number)

        return x 
    
    else: 
        return None 
       
        

print(multiply_numbers([5, 6, 4]))


#Done

