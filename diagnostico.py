class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.category = Category

class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        product.category = self


cat = Category("Electronicos")


producto1 = Product("iPhone 12", 15000)
producto2 = Product("Samsung Galaxy S21", 14000)
producto3 = Product("Apple Watch", 10000)
producto4 = Product("Samsung Galaxy S22", 16000)



cat.add_product(producto1)
cat.add_product(producto2)
cat.add_product(producto3)


print(f"Categoria: {cat.name}")
for product in cat.products:
    print(f"- {product.name} (${product.price})")
    print(f"  Categoría: {product.category.name}")