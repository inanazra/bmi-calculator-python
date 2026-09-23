"""

Description:
This is a simple Python program that calculates the user's Body Mass Index(BMI)
based on their height and weight.It takes input from the user, and prints the result according to
the BMI formula.
"""
def get_float_input(prompt):
    while True:
        try:
            value =float(input(prompt))
            if value <=0:
                print("please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input.Please enter a numeric value.")

def calculate_BMI(weight,height):
    
    return  (weight)/(height**2)

def categorize_BMI(BMI):
    if BMI<18.5:
        return "underweight"
    elif BMI<25:
        return "normal"
    elif BMI<30:
        return "overweight"
    else:
        return "obese"

def main():
    print("hi, welcome to the BMI calculator!")
    weight= get_float_input("please enter your weight first! ")
    height= get_float_input("please enter your height as meter! ")
    BMI = calculate_BMI(weight,height)
    category = categorize_BMI(BMI)
    print(f"your BMI is {BMI:.2f}. and you are classified as {category}. ")
    get_answer()

def choose_answer():
    return {
    "1": "yes",
    "2": "no"
}
def get_answer():
    while True:
            print("would you like to try again? Choose below")
            print("""'1' : yes
                     '2' : no""")
            choice = input("your choice__> ")
            answer = choose_answer().get(choice)

            if answer == "yes":
                main()
            elif answer == "no":
                break

            else:
                print("please choose a valid answer")
                

if __name__ =="__main__":
    main()
 

    
    
