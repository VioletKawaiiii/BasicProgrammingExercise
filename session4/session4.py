
def get_product():
    product_name = input("Product name: (Enter '/' to close the form) ")

    if product_name == "/" or not product_name:
        return None

    product_price = float(input(f"{product_name.capitalize()} price: "))

    amount_items = int(input("how many items do you buy : "))
    return {'name': product_name, 'price': product_price, "items" : amount_items}


def find_the_price():
    products = []
    while True:
        product = get_product()
        if not product:
            break
        else:
            products.append(product)

    if not len(products):
        print('No products')
        return

    for product in products:
        name = product.get('name')
        price = product.get('price')
        items = product.get("items")

        spend = price * items

        profit = price + (price * (10 / 100))

        total_sales = items * profit

        total_profit = (items * profit) - spend

        print(100*'=')
        print(f"""
        product name : {name} | {items} items | total pay : {total_sales} 

        ================ description ================

        price of one product + profit : 

        total product price : {profit}

        ================= my profit =================

        profit : {total_profit}
        """)


find_the_price()