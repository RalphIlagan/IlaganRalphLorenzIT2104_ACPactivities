from Capybara import Capybara

capybara1 = Capybara("Biscoff", "M", 5)
capybara2 = Capybara("Churro", "F", 4)
capybara3 = Capybara("Cinnamon", "M", 3)

capybaras = [capybara1, capybara2, capybara3]

test_case = int(input("Enter the test case number: "))

if 1 <= test_case <= len(capybaras):
    capybara = capybaras[test_case - 1]
    print(f"Test case {test_case}: Name: {capybara.name}, Gender: {capybara.gender}, Age: {capybara.age} years old")
else:
    print("Invalid test case number.")
