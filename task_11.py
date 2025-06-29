class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name
    
    def get_calories(self):
        return self._calories
    
    def set_calories(self, new_calories):
        self._calories = new_calories
    
    def is_healthy(self):
        if self._calories is None:
            return False
        return self._calories < 200
    
    def is_delicious(self):
        return True
    

#Done