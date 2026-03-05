# Arturo Juarez Jr.
# Final Project: Functions
# June 27, 2025
# Functions to process and manage inventory and transactions

# Import
import inventory

# Reads inventory.txt and returns a list of Inventory objects
def process_inventory_file():
    # start the list 
    inventory_list = []
    # read the Inventory.txt
    inventory_file = open("Inventory.txt", "r")

    # Read the first line
    product_id = inventory_file.readline()

    while product_id != "":
        name = inventory_file.readline()
        stock = int(inventory_file.readline())
        price = float(inventory_file.readline())

        # Create inventory object and add to the list
        item = inventory.InventoryClass(product_id.strip(), name.strip(), stock, price)
        inventory_list.append(item)

        product_id = inventory_file.readline()

    inventory_file.close()
    return inventory_list

# Prints the current inventory menu to the user
def print_inventory_menu(inventory_list):
    print("\nID     Item                     Price     Qty Available")
    print("--------------------------------------------------------")
    for item in inventory_list:
        print(item)

# Validates user input for item ID
def get_valid_item_id(inventory_list):
    valid_ids = [item.get_id() for item in inventory_list]
    while True:
        user_input = input("Enter Item ID (or 0 to finish): ").strip()
        # check if user enteres 0 or a valid id
        if user_input == "0" or user_input in valid_ids:
            return user_input
        else:
            print("Invalid Item ID. Try again.")

# Writes updated inventory list to UpdatedInventory.txt
def write_updated_inventory(inventory_list):
    # Use w to overwrite or create new file
    updated_file = open("UpdatedInventory.txt", "w")
    for item in inventory_list:
        updated_file.write(item.get_id() + "\n")
        updated_file.write(item.get_name() + "\n")
        updated_file.write(str(item.get_stock()) + "\n")
        updated_file.write(str(item.get_price()) + "\n")
    updated_file.close()

# Prints a formatted invoice to the console
def print_invoice(transaction_list):
    if not transaction_list:
        print("\nNo items purchased or returned. Thank you for visiting.")
        return

    print("\nINVOICE")
    print("ID     Item                     Qty   Unit Price   Total")
    print("--------------------------------------------------------------")
    subtotal = 0
    for j in transaction_list:
        print(j)
        subtotal += j.calc_cost()
    tax = subtotal * 0.085
    total = subtotal + tax
    print("--------------------------------------------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (8.5%): ${tax:.2f}")
    print(f"Total Due: ${total:.2f}")
