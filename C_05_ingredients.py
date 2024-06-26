# Checks that input is either a float or an integer that is more than zero
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Checks that input is not blank
def not_blank(question):

    while True:
        response = input(question)

        # If response is blank, output error
        if response == "":
            print("Cannot be blank\n")
        else:
            return response


# checks that users enter a valid response (e.g. yes/ no
# units) based on a list of options
def string_checker(question, valid_responses):

    error = "Please choose a valid answer"

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item:
                return item

        print(error)


# Unit dictionary
unit_list = ["kilograms", "kg", "grams", "g", "milligrams", "mg", "litres", "l", "millilitres", "ml", "cups", "c",
             "tablespoons", "tbsp", "teaspoons", "tsp"]

# Main routine
ing_name = not_blank("What is the name of the ingredient? ")
ing_unit = string_checker("What unit of measurement does the ingredient use? ", unit_list)
ing_amount = num_check("How many of this unit? ", "Please enter only a number more than 0", float)

# unit conversion
if ing_unit == "kilograms":
    ing_unit = "kg"
elif ing_unit == "grams":
    ing_unit = "g"
elif ing_unit == "milligrams":
    ing_unit = "mg"
elif ing_unit == "litre":
    ing_unit = "l"
elif ing_unit == "millilitre":
    ing_unit = "ml"
elif ing_unit == "cups":
    ing_unit = "c"
elif ing_unit == "tablespoons":
    ing_unit = "tbsp"
elif ing_unit == "teaspoons":
    ing_unit = "tsp"
else:
    ing_unit = ing_unit

# printing
print("\n**** Ingredient ****\n")
print(f"{ing_name}\n", f"{ing_amount}{ing_unit}")
