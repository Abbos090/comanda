import json

class Korzinka:
    def __init__(self, filename="products.json"):
        self.filename = filename
        self.products = self.load_data()
        self.kirim = 0
        self.chiqim = 0
        self.foyda = 0
    
    def load_data(self):
        """Mahsulotlarni JSON fayldan yuklash."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_data(self):
        """Mahsulotlarni JSON faylga saqlash."""
        with open(self.filename, "w") as file:
            json.dump(self.products, file, indent=4)
    
    def add_product(self, name, quantity, price, sell_price):
        """Mahsulot qo'shish yoki borini yangilash."""
        if name in self.products:
            self.products[name]['quantity'] += quantity
        else:
            self.products[name] = {'quantity': quantity, 'price': price, 'sell_price': sell_price}
        
        self.kirim += quantity * price
        self.save_data()
    
    def sell_product(self, name, quantity):
        """Mahsulot sotish va foydani hisoblash."""
        if name in self.products and self.products[name]['quantity'] >= quantity:
            self.products[name]['quantity'] -= quantity
            sotish_summasi = quantity * self.products[name]['sell_price']
            tannarx_summasi = quantity * self.products[name]['price']
            
            self.chiqim += tannarx_summasi
            self.foyda += (sotish_summasi - tannarx_summasi)
            self.save_data()
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
        return f"Kirim: {self.kirim} so'm, Chiqim: {self.chiqim} so'm, Sof foyda: {self.foyda} so'm"
    
    def get_all_products(self):
        """Barcha mahsulotlarni ro'yxat shaklida chiqarish."""
        return self.products

if __name__ == "__main__":
    store = Korzinka()
    
    while True:
        print("\n1. Mahsulot qo'shish")
        print("2. Mahsulot sotish")
        print("3. Mahsulot haqida ma'lumot olish")
        print("4. Umumiy hisobot")
        print("5. Chiqish")
        
        choice = input("Tanlang (1-5): ")
        
        if choice == "1":
            name = input("Mahsulot nomi: ")
            quantity = int(input("Miqdori: "))
            price = int(input("Kirim narxi: "))
            sell_price = int(input("Sotish narxi: "))
            store.add_product(name, quantity, price, sell_price)
        elif choice == "2":
            name = input("Mahsulot nomi: ")
            quantity = int(input("Miqdori: "))
            store.sell_product(name, quantity)
        elif choice == "3":
            name = input("Mahsulot nomi: ")
            print(store.get_info_product(name))
        elif choice == "4":
            print(store.get_summary())
        elif choice == "5":
            break
        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring!")
