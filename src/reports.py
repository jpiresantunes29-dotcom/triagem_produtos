def show_all_orders(orders):
    if len(orders) == 0:
        print("No orders registered.")
        return

    print("\nAll orders:")
    for order in orders:
        print(f"Code: {order['code']}")
        print(f"Amount: {order['amount']}")
        print(f"Age: {order['age']}")
        print(f"Item count: {order['item_count']}")
        print(f"Payment approved: {order['payment_approved']}")
        print(f"Premium client: {order['premium_client']}")
        print(f"Address confirmed: {order['address_confirmed']}")
        print(f"Status: {order['status']}")
        print(f"Reason: {order['reason']}")
        print("-" * 30)


def show_summary(orders):
    if len(orders) == 0:
        print("No orders registered.")
        return

    approved = 0
    under_review = 0
    blocked = 0

    for order in orders:
        if order["status"] == "BLOCKED":
            blocked += 1
        elif order["status"] == "UNDER REVIEW":
            under_review += 1
        else:
            approved += 1

    print("\nFinal summary:")
    print(f"Total orders processed: {len(orders)}")
    print(f"Approved: {approved}")
    print(f"Under review: {under_review}")
    print(f"Blocked: {blocked}")


def show_highest_order(orders):
    if len(orders) == 0:
        print("No orders registered.")
        return

    highest = orders[0]

    for order in orders:
        if order["amount"] > highest["amount"]:
            highest = order

    print("\nHighest value order:")
    print(f"Code: {highest['code']}")
    print(f"Amount: {highest['amount']}")
    print(f"Status: {highest['status']}")
    print(f"Reason: {highest['reason']}")


def show_blocked(orders):
    if len(orders) == 0:
        print("No orders registered.")
        return

    print("\nBlocked orders:")
    has_blocked = False

    for order in orders:
        if order["status"] == "BLOCKED":
            print(f"{order['code']} - {order['reason']}")
            has_blocked = True

    if not has_blocked:
        print("No blocked orders.")
