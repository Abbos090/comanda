import json

admin_username = 'admin'
admin_password = '1234'

class Korzinka:
    def __init__(self, filename = "products.json"):
        self.filename = filename
        self.products = self.load_data()
        self.kirim = 0
        self.chiqim = 0
        self.foyda = 0

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.products, file, indent=4)

    def add_product(self, name, quantity, price, sell_price):
        if name in self.products:
            self.products[name]['quantity'] += quantity
        else:
            self.products[name] = {'quantity':quantity, 'price':price, 'sell_price':sell_price}

        self.chiqim += quantity * price
        self.save_data()

    def sell_product(self, name, quantity):
        if name in self.products and self.products[name]['quantity'] > quantity:
            self.products[name]['quantity'] -= quantity

            sotish_summasi = (self.products[name]['sell_price'] * quantity)
            tannnarx_summasi = (self.products[name]['price'] * quantity)

            self.chiqim += tannnarx_summasi
            self.foyda += (sotish_summasi - tannnarx_summasi)
        
        else:
            print("Xatolik: mahsulot kam yoki umuman yo'q")
            
    def get_info_product(self, name):
        if name in self.products:
            return f"{name} : {self.products[name]['quantity']}dona, narxi : {self.products[name]['price']}, sotish narxi : {self.products[name]['sell_price']}"
        
    def get_summary(self):
        return f"Chiqim : {self.chiqim}, Kirim : {self.kirim}, Sof foyda : {self.foyda}"

    def get_all_product(self):
        return {name : data['sell_price'] for name, data in self.products.items()}
    
store = Korzinka()

def manager_login(): 
    username = input("Username kiriting >> ".lower())
    password = input("Password kiriting >> ")
    return username == admin_username and password == admin_password

def for_admin():
    if not manager_login:
        print("Noto'g'ri parol yoki username. Siz manager sifatida kira olmaysiz")
        return

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

def for_customer():
    print("\nMahsulotlar va ularning narxlari:")
    products = store.get_all_product()
    for name, price in products.items():
        print(f"{name} : {price} so'm")

ans = input("1.Manager sifatida kirish\n2.Xaridor sifatida kirish\nTanlang (1/2)")

if ans == '1':
    for_admin()
elif ans == '2':
    for_customer()
else:
    print("Noto'g'ri tanlov")

