import math

def is_perfect_number(num):
    if num <= 1:
        return False
    
    sum_of_divisors = 1 
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:  
                sum_of_divisors += num // i

    return sum_of_divisors == num

try:
    num = int(input("Enter a number: "))
    
    if is_perfect_number(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
except ValueError:
    print("Please enter a valid integer.")