number = 147
n1 = number // 100
n2 = number // 10 % 10
n3 = number % 10

print(n1)
print(n2)
print(n3)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
# v1
print("Hello, ", name, "\nYou are ", age, "years old.")

age_after_ten_years = age + 10
print(age_after_ten_years)

# v2
print(f"Hello, {name}. You are {age} years old")

number: int = 10

print(number := 10)
