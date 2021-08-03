import time

transactions = list()

choice = input("Type 1 to continue and 2 to Exit")
while choice == '1':
    name = input("Enter customer name: ")
    quantity = int(input("Enter quantity of bags: "))
    price = float(input("Enter price: "))

    total = quantity * price
    currentTime = time.ctime()

    transaction = (name, quantity, price, total, currentTime)
    transactions.append(transaction)

    print("\n%-16s%-10s%-10s%-10s%-10s" % ("name", "quantity", "price", "total", "time"))
    for transaction in transactions:
        print("%-16s%-10s%-10s%-10s%-10s" % transaction)
