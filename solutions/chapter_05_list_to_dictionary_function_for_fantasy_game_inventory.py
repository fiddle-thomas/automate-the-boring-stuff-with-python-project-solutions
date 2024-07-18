def add_to_inventory(inventory, added_items):
    # Iterate through each item in the added_items list
    for item in added_items:
        if item in inventory:
            # If the item already exists in the inventory, increment its count
            inventory[item] += 1
        else:
            # If the item is new, add it to the inventory with a count of 1
            inventory[item] = 1
    # Return the updated inventory
    return inventory

# Example usage
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

# Optional: print for verification
print(inv)