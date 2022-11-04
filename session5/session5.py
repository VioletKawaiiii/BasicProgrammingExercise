

def start_menu():
   print("""
--------------------------------------
No |     Product     |  price 
--------------------------------------
1. |     Masker      | Rp.10000
2. |     Powder      | Rp.5000
3. |     Lipstick    | Rp.10000
4. |     Blush-On    | Rp.15000 
--------------------------------------   
   """)
start_menu()

many_product = int(input("How many products do you want to buy: "))

product_name = []
product_price = []
total_items = []
product_number = []

total_stock = 0
product_stock = 0

total = []
i = 0

while i < many_product:
    print(f"""
Produk ke-{i + 1}
    """)
    product_number.append(input("Input number of product : "))
    total_items.append(int(input("input how many items do you buy : ")))

    if product_number[i] == "1":
        product_name.append("Masker")
        product_price.append(float(10000))
        product_stock = 5
        total_stock = product_stock - total_items[i]        
        print("total stock : ", product_stock)
        total.append(total_items[i] * int(10000))

    elif product_number[i] == "2":
        product_name.append("Powder")
        product_price.append(float(5000))
        product_stock = 4
        total_stock = product_stock - total_items[i]
        print("total stock : ",total_stock)
        total.append(total_items[i] * int(5000))

    elif product_number[i] == "3":
        product_name.append("Lipstick")
        product_price.append(float(10000))
        product_stock = 6
        total_stock = product_stock - total_items[i]
        print("total stock : ",total_stock)
        total.append(total_items[i] * int(10000)) 

    elif product_number[i] == "4":
        product_name.append("Blush-On")
        product_price.append(float(15000))
        product_stock = 5
        total_stock = product_stock - total_items[i]
        print("total stock : ",total_stock)
        total.append(total_items[i] * int(15000))  

    else:
        product_name.append("none")
        product_price.append(0)
        product_stock = 0
        total.append(total_items[i] * int("0"))

    i = i + 1

def end_menu():
    
    print("""
--------------------------------------------------------------        
| No | Product Name |     Price    | items |     Subtotal     
--------------------------------------------------------------
""")    
end_menu()

pay = 0
change_many = 0
one_product = []
total_profit = 0
calc_profit = 0
total_spending = 0
a = 0

while a < many_product:
    calc_profit = product_price[a] + (product_price[a] * (10 / 100))
    one_product.append(calc_profit)
    total_spending += total_items[a] * one_product[a]
    total_profit = (total_items[a] * calc_profit) - total[a]
    print(" %i.     %s        Rp.%i       %ipcs      Rp.%i "%(a + 1, product_name[a], product_price[a], total_items[a], one_product[a]))

    print(one_product[a])

    a = a + 1



print(f"""
---------------------------------------------------------------------
                                Total spending : Rp.{total_spending}
---------------------------------------------------------------------                          
""")


pay = int(input("pay : "))
change_many = pay -  total_spending

print(f"""
    Change : Rp.{int(change_many)}  
---------------------------------------------------------------------
            Profit earned : Rp.{(total_profit)}
""")






