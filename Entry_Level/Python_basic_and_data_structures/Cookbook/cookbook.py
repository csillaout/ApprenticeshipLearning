from recipes import recipes #importing recipes from recipes.py

#listing recipes name from recipes.py
def list_recipes():
    for recipe in recipes:
        print(f'{recipe["ingredients"]}\nIngredients:{recipe["ingredients"]}\nInstructions:{recipe["instructions"]}')

list_recipes()