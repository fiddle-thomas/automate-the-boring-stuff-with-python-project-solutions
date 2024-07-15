def print_table(data):
    # Iterate over each row
    for row in range(len(data[0])):
        # Iterate over each column
        for col in range(len(data)):
            # Find the length of the longest string in the current column
            just_value = max([len(item) for item in data[col]])
            
            # Print the current item, right-justified
            print(data[col][row].rjust(just_value), end=" ")
        
        # Move to the next line after completing a row
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)