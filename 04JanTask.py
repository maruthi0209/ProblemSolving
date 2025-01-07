# num = list(input("Enter a number: "))
# print(num)
# if ('1' or 0 in num):
#     num.pop(num.index('1'))
#     minvalue = int(min(num))
#     num.append('1')
# lcm= 1
# print(minvalue)
# for i in num:
#     print("the num is ", num)
#     print("i value is ", i)
#     if (int(i) != 1 or int(i) != 0): 
#         if ( int(i) % minvalue != 0):
#             lcm *= minvalue*int(i)
#             print("lcm in condition is ",lcm)
#             print("Entered not factor block")
#         elif (int(i) % minvalue == 0):
#             lcm *= minvalue
#             print("lcm in condition is ",lcm)
#             print("Entered factor block")
#         else:
#             print("some error occured")
#         num.remove(i)
#     else :
#         lcm *= 1
# print("the lcm of the given integers is",lcm)

# num = list(input("Enter a number: "))
# lcm_value = 1
# for i in range(len(num)):
#     print("i value is ", i)
#     if (int(num[i]) != 0 or int(num[i])!= 1):
#         for j in range(i+1, len(num)):
#             print("j value is ", j)
#             if (int(num[j]) != 0 or int(num[j]) != 1):
#                 if (int(num[i]) % int(num[j]) == 0) or (int(num[j]) % int(num[i]) == 0):
#                     print(max([int(num[i]), int(num[j])]))
#                     lcm_value *= max([int(num[i]), int(num[j])])
#                 elif (int(num[i]) % int(num[j]) != 0) or (int(num[j]) % int(num[i]) != 0):
#                     print("not a factor: ", int(num[j] ))
#                     lcm_value *= int(num[j])
#                 else:
#                     print("Some error occured")
#             else:
#                 continue
#     else :
#         continue
# print("The lcm value of given digits is: ", lcm_value)

def gcd(a, b):
    """Calculate the GCD of two numbers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the LCM of two numbers."""
    return abs(a * b) // gcd(a, b)

def lcm_of_digits(number):
    """Calculate the LCM of the digits of a given number."""
    digits = [int(digit) for digit in str(number) if digit != '0']  # Ignore zeros
    if not digits:
        return 0  # If all digits are zero, LCM is 0
    
    result = digits[0]
    for digit in digits[1:]:
        result = lcm(result, digit)
    
    return result

# Input number
number = int(input("Enter a number: "))

# Calculate and print the LCM of its digits
if number == 0:
    print("The LCM of the digits of 0 is undefined.")
else:
    result = lcm_of_digits(number)
    print(f"The LCM of the digits of {number} is: {result}")




