set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}
set_difference = set1 - set2
set_difference1= set2 - set1
union_set = set1 | set2
symmetric_difference = set1 ^ set2
symmetric_difference1 = set2 ^ set1
set_interesection = set1 & set2
set_interesection1 = set2 & set1

print ("SET DIFFERENCE")
print (f"set1 - set 2 = ",set_difference)
print (f"set1 - set 2 = ",set_difference1)
print("UNION SETS")
print (f"set1 | set2 = ",union_set)
print ("SYMMETRIC DIFFERENCE")
print (f"set1 ^ set2 = ",symmetric_difference)
print (f"set2 ^ set1 = ",symmetric_difference1)
print("SET INTERSECTION")
print (f"set1 & set2 = ",set_interesection)
print (f"set2 & set1 = ",set_interesection1)

