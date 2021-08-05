str1='Water'
str2='Milk'
print("Is str1 == str2? I predict False.")
print(str1==str2)

print("\nIs str1 == 'water' when ignoring case? I predict True.")
print(str1.lower()=='water')

n1=18
n2=16
print("\nIs n1 > n2? I predict True.")
print(n1>n2)

print("\nAre str1 == str2 and n1 > n2? I predict False.")
print(str1==str2 and n1>n2)

foods=['milk','water','bread']
print("\nIs 'water' in the foods? I predict True.")
print('water' in foods)

print("\nIs 'bread' not in the foods? I predict False.")
print('water' not in foods)
