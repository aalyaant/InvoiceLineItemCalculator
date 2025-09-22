#Alyce Gaines
#CSI261
#InvoiceLineItemCalculator

def get_price():
    while True:
        try:
            price = float(input("Enter Price: "))
            return price
        except ValueError:
            print("Invalid Entry - Non-Decimal Format. Try Again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            return quantity
        except ValueError:
            print("Invalid Entry - Non-Interger Format. Try Again.")

if __name__ == "__main__":
    print("Invoice Line Item Calculator \n")
    answer = "y"
    while answer.lower() =="y":
        price = get_price()
        quantity = get_quantity()
        total = price * quantity
        
        print("Price: ", f"{price: .2f}")
        print("Quantity:  ", quantity)
        print("Total: ", f"{total: .2f}")
        answer = input("Add Another Line Item? (y/n): ")

    print("adios!")