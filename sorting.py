def merge_sort(chocolates, key):
    if len(chocolates) <= 1:
        return chocolates

    mid = len(chocolates) // 2
    left_half = merge_sort(chocolates[:mid], key)
    right_half = merge_sort(chocolates[mid:], key)

    return merge(left_half, right_half, key)


def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_chocolates(chocolates, sort_by):
    if sort_by == 'weight':
        return merge_sort(chocolates, 'weight')
    elif sort_by == 'price':
        return merge_sort(chocolates, 'price')
    else:
        raise ValueError("Invalid sort_by parameter. Use 'weight' or 'price'.")


# Test Cases
chocolates = [
    {'type': 'Almond', 'weight': 5, 'price': 2, 'id': '002'},
    {'type': 'caramel', 'weight': 3, 'price': 3, 'id': '001'},
    {'type': 'Peanut Butter', 'weight': 7, 'price': 4, 'id': '005'},
    {'type': 'coconut', 'weight': 6, 'price': 3, 'id': '003'},
]

# Sort by weight
sorted_by_weight = sort_chocolates(chocolates, 'weight')
print("Sorted by weight:", sorted_by_weight)

# Sort by price
sorted_by_price = sort_chocolates(chocolates, 'price')
print("Sorted by price:", sorted_by_price)

