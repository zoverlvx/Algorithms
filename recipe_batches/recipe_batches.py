#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    recipe_amounts= list(recipe.values())
    amounts_of_ingredients = list(ingredients.values())
    if (len(recipe_amounts) > len(amounts_of_ingredients)):
        return 0
    for item in recipe:
        if item not in ingredients:
            return 0
    length = len(recipe_amounts)
    amounts = []
    for i in range(length):
        amount = amounts_of_ingredients[i] // recipe_amounts[i]
        if(amount == 0):
            return 0
        amounts.append(amount)
    amounts.sort()
    return amounts[0]


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
