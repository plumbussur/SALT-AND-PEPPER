def is_palindrome(string):
    if string is None:
        return False
    
    s = str(string)
    
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned == cleaned[::-1]


#Done