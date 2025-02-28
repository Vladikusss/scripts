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

    def __str__(self):
        """Function to specify how to output Meal objects."""
        return (f"Name: {self.name} | "
                f"Ingredients: {self.ingredients} | "
                f"Time to serve: {self.time} | "
                f"Allergens: {self.allergens}")

    def PrintMealDetails(self):
        """Function to print out the details about the meal."""
        print(f"Recipe: {self.name}")
        print(f"Ingredients:", ", ".join(self.ingredients))
        print(f"Time to serve: {self.time}")
        print(f"Allergens:", ", ".join(self.allergens))

class RecipeManager:
    """A class to manage all meals."""
    def __init__(self):
        self.meals = list()

    def AddMeal(self, meal: object):
        """Function to add a meal."""
        self.meals.append(meal)

    def SearchByTimeOfDay(self, time_of_day: str):
        """Function to search and filter out meals by the time of the day."""
        found = False
        for meal in self.meals:
            if time_of_day.lower() == meal.time.lower():
                print(f"- {meal}")
                found = True
        if not found:
            print("We don't have any meals for the given time.")

    def SearchByIngredients(self, ingredients: list[str]):
        found = False
        for meal in self.meals:
            if all(ingrs in ingredients for ingrs in meal.ingredients):
                print(f"- {meal.name} | Contains: {meal.allergens}")
                found = True
        if not found:
            print("We don't have any meals with these ingredients")



    def PrintMeals(self):
        """Function to print all available meals."""
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
    Meal1 = Meal("pasta", ["milk", "bread", "water"], "day", ["prawn", "crabs"])
    Meal1.PrintMealDetails()
    print(Meal1.allergens)

    recipeManager = RecipeManager()
    # Add a meal
    test = recipeManager.AddMeal(Meal1)
    # Search for meals by time of day
    test = recipeManager.SearchByTimeOfDay("day")
    print(test)
    # Print all stored meals
    test = recipeManager.PrintMeals()
    print(test)
    test = recipeManager.SearchByIngredients(["milk", "bread", "water"])
    print(test)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
