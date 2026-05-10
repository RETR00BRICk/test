def load_orders():
    orders = []
    try:
        with open("orders.txt", "r") as file:
            for line in file:
                if line.strip():
                    orders.append(line.strip().split(","))
    except FileNotFoundError:
        pass
    return orders

def save_orders(orders):
    with open("orders.txt", "w") as file:
        for order in orders:
            file.write(",".join(order) + "\n")

while True:
    print("--- Order Management System ---")
    print("1. Add new order")
    print("2. View all orders")
    print("3. Search order by ID")
    print("4. Update order")
    print("5. Delete order")
    print("6. Exit")
    
    choice = input("Select an option: ")
    orders = load_orders()

    if choice == "1":
        order_id = input("Enter Order ID: ")
        item = input("Enter Item Name: ")
        qty = input("Enter Quantity: ")
        price = input("Enter Price: ")
        orders.append([order_id, item, qty, price])
        save_orders(orders)
        print("Order added successfully")

    elif choice == "2":
        if not orders:
            print("No orders found")
        else:
            print("All Orders:")
            for o in orders:
                print(f"ID: {o[0]} | Item: {o[1]} | Qty: {o[2]} | Price: {o[3]}")

    elif choice == "3":
        search_id = input("Enter Order ID to search: ")
        found = False
        for o in orders:
            if o[0] == search_id:
                print(f"Found: Item: {o[1]}, Qty: {o[2]}, Price: {o[3]}")
                found = True
                break
        if not found:
            print("Order not found")

    elif choice == "4":
        update_id = input("Enter Order ID to update: ")
        found = False
        for o in orders:
            if o[0] == update_id:
                o[2] = input("Enter new Quantity: ")
                o[3] = input("Enter new Price: ")
                save_orders(orders)
                print("Order updated")
                found = True
                break
        if not found:
            print("Order not found")

    elif choice == "5":
        delete_id = input("Enter Order ID to delete: ")
        initial_count = len(orders)
        orders = [o for o in orders if o[0] != delete_id]
        
        if len(orders) < initial_count:
            save_orders(orders)
            print("Order deleted")
        else:
            print("Order not found")

    elif choice == "6":
        break
    else:
        print("Invalid choice")