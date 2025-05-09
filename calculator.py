def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None
false        

# Main function to get user input and calculate BMI
def main():
    print("BMI Calculator - Calculate the Body Mass Index")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)

        if bmi is not None:
            print(f"Your BMI is: {bmi}")
            if bmi < 18.5:
                print("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                print("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                print("You are overweight.")
            else:
                print("You are obese.")
        else:
            print("Height cannot be zero. Please enter a valid height.")
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
