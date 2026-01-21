#Assignment on Module 2

# 1. Write a Python program that takes a list of numbers as input, removes duplicates using a suitable list method,and returns a dictionary containing the original list,
the unique values, and their count. Use a function with parameters and a return statement to perform this task.


def removes_duplicates(numbers):
    # Remove duplicates without changing the original order
    unique_num = list(dict.fromkeys(numbers))

    # Create a dictionary with original list, unique values, and count
    my_dict = {
        "Original_list": numbers,
        "Unique values": unique_num,
        "Count": len(unique_num)
    }

    return my_dict

# Take input from user
numbers = list(map(int, input('Enter numbers (space separated): ').split()))

# Call the function and display results
print(removes_duplicates(numbers))


# 2. Create a function that accepts two sets as parameters and returns their union, intersection, and difference.
Use keyword arguments with default parameter values so the function can work even if one of the sets is not provided by the user. Display the results clearly.


def set_operation(set1, set2={3, 4, 2, 5}):
    # Union
    union_result = set1.union(set2)
    # Intersection
    intersection_result = set1 & set2
    # Difference
    difference_result = set1 - set2

    return union_result, intersection_result, difference_result

# Example usage
union, intersection, difference = set_operation({3, 4, 23, 53, 5})

print("\nSet Operations Results:")
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)



# 3. Define a tuple containing mixed data types, unpack its values into separate variables, and compare them with another tuple using comparison operators.
Then, explain in code comments the main difference between lists and tuples in Python.


tuple_1 = ("Tyhan hasan", 'Abid hasan', 55, 42, 3.85, 3.42)

# Unpacking tuple
(a, b, c, d, e, f) = tuple_1

tuple_2 = ("Tyhan hasan", 'Abid hasan', 55, 42, 3.85, 3.42)

# Comparison operators
print("\nTuple Comparisons:")
print("Equal:", tuple_1 == tuple_2)
print("Not Equal:", tuple_1 != tuple_2)
print("Less than:", tuple_1 < tuple_2)
print("Greater than:", tuple_1 > tuple_2)
print("Greater than or equal:", tuple_1 >= tuple_2)
print("Less than or equal:", tuple_1 <= tuple_2)

# -----------------------------
# Differences between List and Tuple
# -----------------------------
# 1. Mutability:
#    - List: mutable → elements can be changed
#    - Tuple: immutable → elements cannot be changed
# 2. Syntax:
#    - List: []
#    - Tuple: ()
# 3. Performance:
#    - Tuple is faster than list
#    - Suitable for fixed data






