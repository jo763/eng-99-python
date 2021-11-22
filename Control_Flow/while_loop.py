while True:
    age = input("What is your age in years?\n")
    if age.isdigit():
        age = int(age)
        if age <= 120:
            break
    print("Please provide your age in digits.")

print(age, type(age))