def display_inventory(inventory):
    # Print the header
    print("Inventory:")
    
    # Iterate through each item and its count in the inventory
    for item, count in inventory.items():
        # Print the count and name of each item
        print(count, item)
    
    # Calculate and print the total number of items
    print("Total number of items: ", sum(inventory.values()))

# Sample inventory dictionary
sample_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Call the function with the sample inventory
display_inventory(sample_inventory)