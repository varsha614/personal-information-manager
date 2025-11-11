# Step 1: Collect user details
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
hobbies = input("Enter your hobbies (separated by commas): ")

# Step 2: Format hobbies into a list
hobby_list = [hobby.strip() for hobby in hobbies.split(",")]

# Step 3: Display the formatted personal information
print("\n----- Personal Information -----")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"City    : {city}")
print("Hobbies :")

# Step 4: Display each hobby neatly
for index, hobby in enumerate(hobby_list, start=1):
    print(f"   {index}. {hobby}")

print("--------------------------------")
