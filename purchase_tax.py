#get user info
def create_receipt():
    name = input("Please provide your name: ")
    purchase_amount = float(input("Enter the purchase amount: $"))

    #add tax of 10%
    tax_rate = .10
    tax_amount = purchase_amount * tax_rate

    
    #Grand total for receipt
    grand_total = tax_amount + purchase_amount
    
    
    #show receipt
    print("Thank you {}, please wait will I ready your receipt.".format(name))
    print("Subtotal = ${}".format(purchase_amount))
    print("Tax = {}".format(tax_amount))
    print("--------------------------------")
    print("Total = ${}".format(grand_total))
create_receipt()