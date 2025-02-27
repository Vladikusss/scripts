"""
 /*
 * Created by Vladdy | 27.02.2025
 * Last Updated: 27.02.2025
 * Program: Recipe script to search and output information on meals.
 * Version: 1.0
 * Status: In progress
 * Detailed description:
---> Search and output information about meal recipes for specific time of the day,
e.g. morning, day, dinner.
---> Search and output information about meals based on the ingredients available.
---> Output if meals searched have any allergens, and if so which ones.
---> The user can then choose the meal from the list searched, and the program will output the information about the meal.

 *** Own Reference: Fix the loop in the class, add _str_ to the Meal class, fix any other issues
 */
"""

import json
import sys


class Meal:
    """Class to hold information about specific meals."""
    def __init__(self, name: str, ingredients: list[str], best_served: str, allergens: list[str]):
        self.name = name
        self.ingredients = ingredients
        self.time = best_served
        self.allergens = allergens

    def PrintMealDetails(self):
        print(f"Recipe: {self.name}")
        print(f"Ingredients:", ", ".join(self.ingredients))
        print(f"Time to serve: {self.time}")
        print(f"Allergens:", ", ".join(self.allergens))

class RecipeManager:
    def __init__(self):
        self.meals = list()

    def AddMeal(self, meal):
        self.meals.append(meal)

    def SearchByTimeOfDay(self, time_of_day):
        for meal in self.meals:
            if time_of_day == meal.time:
                print("It works :)))")

    def PrintMeals(self):
        if not self.meals:
            print("No meals available.")
        else:
            print("Stored meals:")
            for meal in self.meals:
                print(f"- {meal}")





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # For testing:
    Meal1 = Meal("example", ["list", "of", "ingredients"], "day", ["prawn", "crabs"])
    Meal1.PrintMealDetails()
    print(Meal1.allergens)

    recipeManager = RecipeManager()
    # Add a meal
    test = recipeManager.AddMeal(Meal1)
    print(test)
    # Search for meals by time of day
    test = recipeManager.SearchByTimeOfDay("day")
    print(test)
    # Print all stored meals
    test = recipeManager.PrintMeals()
    print(test)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
