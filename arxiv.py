
class Waters:
    def __init__(self):
        self.waters = {}

    def add_water(self, water, soni):
        if water in self.waters:
            self.waters[water] += soni
        else:
            self.waters[water] = soni
        
    def remove_water(self, water, soni):
        if soni < self.waters[water]:
            self.waters[water] -= soni
        else:
            print('Xatolik kelib chiqdi !')

    def get_info_water(self, water):
        if water in self.waters:
            return f"Do'konda {self.waters[water]} ta {water} bor"
        else:
            return f"Do'konda {water} mahsuloti yo'q"
        
    def get_info(self):
        return self.waters

# p1 = Waters()

# p1.add_water('cola', 10)
# p1.remove_water('cola', 5)

# p1.add_water('cola', 203)
# print(p1.get_info_water('cola'))


class Icecream:
    def __init__(self):
        self.icecream = {}

    def add_icecream(self, name, number):
        if name in self.icecream:
            self.icecream[name] += number
        else:
            self.icecream[name] = number
    
    def remove_icecream(self, name, number):
        if self.icecream[name] > number:
            self.icecream[name] -= number
        else:
            print('Xatolik yuzaga keldi')

    def get_info_icecream(self, icecream):
        if icecream in self.icecream:
            return f"{self.icecream[icecream]}ta {icecream} bor"
        else:
            return f"Do'konda {icecream} yo'q"
        
    def get_info(self):
        return self.icecream

# i1 = Icecream()

# i1.add_icecream('musa', 10)
# print(i1.get_info_icecream('musa'))
# i1.remove_icecream('musa', 5)
# print(i1.get_info_icecream('musa'))
# i1.add_icecream('musa', 10)
# print(i1.get_info_icecream('musa'))

# print(i1.get_info())

class Sweets:
    def __init__(self):
        self.sweets = {}

    def add_sweets(self, name, kg):
        if name in self.sweets:
            self.sweets[name] += kg
        else:
            self.sweets[name] = kg
        
    def remove_sweets(self, name, kg):
        if name in self.sweets and kg < self.sweets[name]:
            self.sweets[name] -= kg
        else:
            return 'Xatolik yuz berdi'
        
    def get_info_sweet(self, name):
        if name in self.sweets:
            return f"{self.sweets[name]} kg {name} shirinligi bor"
        else:
            return f"Do'konda {name} qolmagan"
    def get_info(self):
        return self.sweets
    
# s1 = Sweets()

# s1.add_sweets('sfad', 20)
# print(s1.get_info_sweet('sfad'))
# s1.remove_sweets('sfad', 15)
# print(s1.get_info_sweet('sfad'))