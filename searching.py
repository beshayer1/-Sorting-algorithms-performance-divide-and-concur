def binary_search(chocolates, target, key):
    left, right = 0, len(chocolates) - 1

    while left <= right:
        mid = (left + right) // 2
        if chocolates[mid][key] == target:
            return mid  # Chocolate found
        elif chocolates[mid][key] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Chocolate not found


def search_chocolate(chocolates, target, search_by):
    if search_by == 'price':
        chocolates.sort(key=lambda x: x['price'])
    elif search_by == 'weight':
        chocolates.sort(key=lambda x: x['weight'])
    else:
        raise ValueError("Invalid search_by parameter. Use 'price' or 'weight'.")

    index = binary_search(chocolates, target, search_by)
    if index != -1:
        return chocolates[index]
    else:
        return None  # Chocolate not found


# Test Cases
chocolates = [
    {'type': 'Almond', 'weight': 5, 'price': 2, 'id': '002'},
    {'type': 'Peanut Butter', 'weight': 7, 'price': 4, 'id': '005'},
    {'type': 'caramel', 'weight': 3, 'price': 3, 'id': '007'}
]

# Test searching by price
print("Search by price:")
print("Chocolates:", chocolates)
target_price = 4
found_chocolate = search_chocolate(chocolates, target_price, 'price')
print("Chocolate with price", target_price, ":", found_chocolate)

# Test searching by weight
print("\nSearch by weight:")
print("Chocolates:", chocolates)
target_weight = 7
found_chocolate = search_chocolate(chocolates, target_weight, 'weight')
print("Chocolate with weight", target_weight, ":", found_chocolate)
