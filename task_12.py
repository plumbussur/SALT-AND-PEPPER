class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, new_calories):
        self._calories = new_calories
    
    def is_healthy(self):
        if self._calories is None:
            return False
        try:
            return float(self._calories) < 200
        except (TypeError, ValueError):
            return False
    
    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor
    
    @property
    def flavor(self):
        return self._flavor
    
    @flavor.setter
    def flavor(self, new_flavor):
        self._flavor = new_flavor
    
    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return True
    

#Done