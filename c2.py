
def div_names(names):
    """Function of group items into six lists"""
    # Create six empty lists in one list
    grouped_lists = [[] for _ in range(6)]

    # Distribute them into the lists
    for i, name in enumerate(names):
        grouped_lists[i // 6].append(name)

    return grouped_lists


# Accepting names from the user
user_input = input("Enter names separated by space: ")
names = [name for name in user_input.split(" ")]

# Group the names
grouped_names = div_names(names)

# Print the group of listed names
for i, group in enumerate(grouped_names, 1):
    print(f"{i}. {group}")

