# Arturo Juarez Jr.
# Final Project: Baking Supply Shop 
# June 27, 2025
# This program allows the user to purchase or return items. It reads an Inventory.txt, prints inventory menu,
# updates inventory, and provides an invoice if transcation occurred (purhcase or returm). Allows the user
# to make multiple transactions at once.

# Import
import Juarez_Arturo_FP_Functions as func
import inventory # used in function file, not needed here
import transactionitem

# Start the main
def main():
    # use function to process the inventory file
    inventory_list = func.process_inventory_file()

    # start list to store transaction items(purchases or returns)
    transaction_list = []

    # use function to print the initial inventory menu
    func.print_inventory_menu(inventory_list)

    # start user input (while loop)
    while True:
        # get valid item id with function from inventory list
        item_id = func.get_valid_item_id(inventory_list)

        # if 0, the user is done
        if item_id == "0":
            break # this breaks the while loop it proceeds to invoice

        # ask for quantity in a loop until valid or user cancels
        while True:
            try:
                quantity = int(input("Enter quantity (negative to return): "))
            except Exception:
                print("Error: Quantity must be a whole number. Try again.")
                continue  # ask for quantity again (restart quantity while loop)

             # 0 is a valid integer, ask if user wants to cancel transaction
            if quantity == 0:
                confirm = input("You entered 0. Do you want to cancel this item and return to item selection? (Y/N): ").strip().lower()
                if confirm == "y":
                    quantity = None  # cancel item
                    break # stops the while quantity loop
                else:
                    continue  # restart quantity loop
            break  # valid quantity

        # if user cancelled item, go back to item id input
        if quantity is None:
            continue # restarts the while loop  (back to item id)

        # search for item in inventory (for loop)
        for item in inventory_list:
            if item.get_id() == item_id:
                # if it's a purchase
                if quantity > 0:
                    #check if enough inventory
                    success = item.purchase(quantity)
                    if not success:
                        print("Error: Not enough stock available.")
                        break # break the for loop
                # for return
                else:
                    item.purchase(quantity) # input should already be neg.

                # start transaction object
                trans = transactionitem.TransactionItemClass()
                # set the values
                trans.set_id(item.get_id())
                trans.set_name(item.get_name())
                trans.set_qty(quantity)
                trans.set_price(item.get_price())
                transaction_list.append(trans)
                break # breaks the search loop since item has been found

        # Display updated inventory
        func.print_inventory_menu(inventory_list)


    # Print invoice
    func.print_invoice(transaction_list)

    # Write updated inventory
    func.write_updated_inventory(inventory_list)

# Call the main
if __name__ == "__main__":
    main()
