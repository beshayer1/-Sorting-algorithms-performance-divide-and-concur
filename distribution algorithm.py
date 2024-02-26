class Chocolate:  # create a class for the chocolates
    def __init__(self, id, weight, price, type):  # identify the attributes of the chocolates
        self.id = id
        self.weight = weight
        self.price = price
        self.type = type


def distribute_chocolates_iterative(chocolates, students):  #iterative distribution of the chocolates
    distributed_chocolates = []
    student_index = 0
    for chocolate in chocolates:
        if student_index >= len(students):
            student_index = 0
        distributed_chocolates.append((students[student_index], chocolate))
        student_index += 1
    return distributed_chocolates


def distribute_chocolates_recursive(chocolates, students, index=0):  # recursive distribution of the chocolates
    if index >= len(chocolates):
        return []
    return [(students[index % len(students)], chocolates[index])] + distribute_chocolates_recursive(chocolates, students, index + 1)

# Test cases


chocolates = [Chocolate("002", 5, 2, "Almond"), Chocolate("005", 7, 4, "Peanut Butter"), Chocolate ("001", 3, 3, "caramel")]
students = ["mariam", "ahmed", "saif"]

print("Iterative Distribution:")
for student, chocolate in distribute_chocolates_iterative(chocolates, students):
    print(f"{student} gets {chocolate.type} chocolate")

print("\nRecursive Distribution:")
for student, chocolate in distribute_chocolates_recursive(chocolates, students):
    print(f"{student} gets {chocolate.type} chocolate")