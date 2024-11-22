def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    
    roman = roman.upper()
    
    # Check if the input contains any invalid characters
    if not all(char in roman_values for char in roman):
        raise ValueError("Invalid Roman numeral. Please use only I, V, X, L, C, D, M.")
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        current_value = roman_values[char]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total

roman_input = input("Enter a Roman numeral: ")

try:
    result = roman_to_integer(roman_input)
    print(f"The integer value of '{roman_input.upper()}' is: {result}")
except ValueError as e:
    print(e)
