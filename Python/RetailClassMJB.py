class RetailItem:
    def __init__(self, description='', units_on_hand=0, price=0.0):
        self.__description = description
        self.__units_on_hand = units_on_hand
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_units_on_hand(self, units_on_hand):
        self.__units_on_hand = units_on_hand

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units_on_hand(self):
        return self.__units_on_hand

    def get_price(self):
        return self.__price
 


class CashRegister:
    def __init__(self):
        self.__items = []

    def purchase_item(self, item):
        self.__items.append(item)

    def get_total(self):
        total = 0.0
        for item in self.__items:
            total += item.get_price()
        return total

    def show_items(self):
        print("Items in Cash Register:")
        for item in self.__items:
            print(f"Description: {item.get_description()}, Units on Hand: {item.get_units_on_hand()}, Price: ${item.get_price():.2f}")

    def clear(self):
        self.__items.clear()

def main():
    # Create a CashRegister object
    cash_register = CashRegister()

    # Create some RetailItem objects
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Purchase items
    cash_register.purchase_item(item1)
    cash_register.purchase_item(item2)
    cash_register.purchase_item(item3)

    # Show items in the cash register
    cash_register.show_items()

    # Get total price of items
    print(f"\nTotal Price: ${cash_register.get_total():.2f}")

    # Clear the cash register
    cash_register.clear()
    print("\nCash Register cleared.")

main()