n = int(input("Enter an integer: "))
str_n = str(n)

if str_n == str_n[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")