#1. and
#and means both conditions must be True.

age = 20
has_id = True

print(age >= 18 and has_id)

#2. or
#or means at least one condition must be True.

age = 20
has_student_id = False

print(age >= 18 or has_student_id)

#3. not
#not reverses the result.

is_raining = False

print(not is_raining)

#Practice Program

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("You can enter")
else:
    print("You cannot enter")