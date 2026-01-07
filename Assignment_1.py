# Problem: 01 
# Write a Python program that takes a number as input and checks whether it is even or odd.


num = int(input("Enter the number :"))

if num % 2 == 0 :
    print("Your entered number is even :",num)
else :
    print("Your entered number is odd :",num)


#Problem: 02
# Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation            
                              

a = int(input("Enter the first number :"))
b = int(input("Enter the last number :"))

sum = a + b
sub = a - b
mul = a * b
div = round( a / b , 2)

print("The summmation is :",sum)
print("The subtraction is :",sub)
print("The multiplication is :",mul)
print("The division is :",div)


# Problem: 03
# Write a program using a for loop that calculates the sum of even numbers between 1 and 100.


Total = 0

for num in range(1 , 101):
    if num % 2 == 0 :
        Total+= num

print("Sum of the even numbers between 1 to 100 is :",Total)



