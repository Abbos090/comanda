class Korzinka:
    def __init__(self):
        self.products = {}  
        self.chiqim = 0  
        self.kirim = 0  
        self.foyda = 0  
    
    def add_product(self, name, quantity, price, sell_price):
        """Mahsulot qo'shish yoki borini yangilash."""
        if name in self.products:
            self.products[name]['quantity'] += quantity
        else:
            self.products[name] = {'quantity': quantity, 'price': price, 'sell_price': sell_price}
        
        self.chiqim += quantity * price  
    
    def sell_product(self, name, quantity):
        """Mahsulot sotish va foydani hisoblash."""
        if name in self.products and self.products[name]['quantity'] >= quantity:
            self.products[name]['quantity'] -= quantity
            sotish_summasi = quantity * self.products[name]['sell_price']
            tannarx_summasi = quantity * self.products[name]['price']
            
            self.kirim += tannarx_summasi  
            self.foyda += (sotish_summasi - tannarx_summasi)
        else:
            print("Xatolik: yetarli mahsulot mavjud emas yoki umuman yo'q!")
    
    def get_info_product(self, name):
        """Mahsulot haqida ma'lumot olish."""
        if name in self.products:
            return f"{name}: {self.products[name]['quantity']} dona, narxi: {self.products[name]['price']} so'm, sotish narxi: {self.products[name]['sell_price']} so'm"
        else:
            return "Mahsulot mavjud emas."
    
    def get_summary(self):
        """Do'konning umumiy holati haqida ma'lumot."""
        return f"Kirim: {self.chiqim} so'm, Chiqim: {self.kirim} so'm, Sof foyda: {self.foyda} so'm"
    
    def get_all_products(self):
        """Barcha mahsulotlarni ro'yxat shaklida chiqarish."""
        return self.products

k1 = Korzinka()
k1.add_product('pepsi', 10, 8000, 10000)
k1.add_product('pepsi', 5, 8000, 10000)
print(k1.get_info_product('pepsi'))