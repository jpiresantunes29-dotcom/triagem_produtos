from validations import (
    read_positive_integer,
    read_non_negative_integer,
    read_non_negative_float,
    read_yes_or_no,
)
from rules import classify_order
from reports import (
    show_all_orders,
    show_summary,
    show_highest_order,
    show_blocked,
)
from storage import load_orders, save_orders


def register_orders(orders):
    count = read_positive_integer("How many orders do you want to analyze? ")

    for i in range(count):
        print(f"\nOrder {i + 1}")

        code = input("Order code: ").strip()
        amount = read_non_negative_float("Order amount: ")
        age = read_non_negative_integer("Client age: ")
        item_count = read_positive_integer("Item count: ")
        payment_approved = read_yes_or_no("Payment approved (yes/no): ")
        premium_client = read_yes_or_no("Premium client (yes/no): ")
        address_confirmed = read_yes_or_no("Address confirmed (yes/no): ")

        status, reason = classify_order(
            amount,
            age,
            item_count,
            payment_approved,
            premium_client,
            address_confirmed,
        )

        order = {
            "code": code,
            "amount": amount,
            "age": age,
            "item_count": item_count,
            "payment_approved": payment_approved,
            "premium_client": premium_client,
            "address_confirmed": address_confirmed,
            "status": status,
            "reason": reason,
        }

        orders.append(order)
        save_orders(orders)

        print(f"Code: {code}")
        print(f"Result: {status}")
        print(f"Reason: {reason}")


def main():
    orders = load_orders()

    while True:
        print("\n=== MENU ===")
        print("1 - Register orders")
        print("2 - Show all orders")
        print("3 - Show summary")
        print("4 - Show highest value order")
        print("5 - Show blocked orders")
        print("6 - Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            register_orders(orders)
        elif option == "2":
            show_all_orders(orders)
        elif option == "3":
            show_summary(orders)
        elif option == "4":
            show_highest_order(orders)
        elif option == "5":
            show_blocked(orders)
        elif option == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
