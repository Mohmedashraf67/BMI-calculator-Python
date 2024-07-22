def main():
    # Input weight and height from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    while height>3.5:
       height = float(input("Enter your height in meters: "))  
        
    calculate_bmi(weight, height)
    # Calculate BMI

    # Print results

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    bmi = weight / (height*height)
    print(f"Your BMI is: {bmi:.2f}")
    get_bmi_category(bmi)

def get_bmi_category(bmi):
    """Return the BMI category based on the calculated BMI value."""
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif 25 <= bmi < 29.9:
        print("Overweight")
    else:
        print("Obesity")

if __name__ == "__main__":
    main()
