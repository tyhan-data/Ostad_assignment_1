#Assignment on Module 2

# 1. Write a Python program that takes a list of numbers as input, removes duplicates using a suitable list method, and returns a dictionary containing the original list, the unique values, and their count. Use a function with parameters and a return statement to perform this task.
f

def removes_duplicates(numbers):

    # removing duplicates by set() method.(optional)
    unique_n = list(set(numbers))

    # without set() method.
    unique_num = list(dict.fromkeys(numbers))

    # create a dictionary..
    my_dict = {
      "Original_list": numbers ,
      "Unique values": unique_num,
      "Count": len(unique_num)
    }

    return my_dict

# Take a list from user.
numbers = list(map(int,input('Enter numbers :').split()))

# call the fucntion.
print(removes_duplicates(numbers))



# 2. Create a function that accepts two sets as parameters and returns their union, intersection, and difference. Use keyword arguments with default parameter values so the function can work even if one of the sets is not provided by the user. Display the results clearly.


def set_operation(set1, set2 ={3,4,2,5}):
      
      # Union operation..
      result1 = set1.union(set2)
     
      # Intersection operation..
      result2  = set1 & set2
      
      # Difference operation..
      result3 = set1 - set2
       
     # Return the results..
      return result1 , result2 ,result3
      
# unpack the results..
u , i , d =set_operation({3,4,23,53,5})

# Display the results clearly..
print("Union :", u)
print("Intersection :", i)
print("Difference :", d)



# 3. Define a tuple containing mixed data types, unpack its values into separate variables, and compare them with another tuple using comparison operators. Then, explain in code comments the main difference between lists and tuples in Python.


tuple_1 = ("Tyhan hasan", 'Abid hasan',55, 42, 3.85, 3.42)

# Unpacking the tuple..
(a, b, c, d, e, f) = tuple_1

tuple_2 = ("Tyhan hasan", 'Abid hasan',55, 42, 3.85, 3.42)

# compare touple..
print(tuple_1 == tuple_2)
print(tuple_1 != tuple_2)
print(tuple_1 < tuple_2)
print(tuple_1 > tuple_2)
print(tuple_1 >= tuple_2)
print(tuple_1 <= tuple_2)

# Main differences between lists and tuples:

# 1. Mutability:
#    - List: mutable → elements change করা যায়
#    - Tuple: immutable → elements change করা যায় না

# 2. Syntax:
#    - List: []
#    - Tuple: ()

# 3. Performance:
#    - Tuple faster than list 
#    - Suitable for fixed data





