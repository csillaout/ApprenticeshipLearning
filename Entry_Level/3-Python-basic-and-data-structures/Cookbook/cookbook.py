from recipes import recipes #importing recipes from recipes.py

#listing recipes name from recipes.py
def list_recipes():
    for recipe in recipes:
        print(f'{recipe["ingredients"]}\nIngredients:{recipe["ingredients"]}\nInstructions:{recipe["instructions"]}')

#find recipe by name
def query_recipe():
    query_name = input("Enter the name of the recipe you want ot saerch for:")

    found_recipes = [recipe for recipe in recipes if query_name.lower() in recipe["name"].lower()]

    if found_recipes:
        print(f"Found {len(found_recipes)} matching recipes:")
        for recipe in found_recipes:
            ingredients_list = [ingredient["item"] for ingredient in recipe["ingredients"]]
            ingredients_str = ",  ".join(ingredients_list)
            print(f"\nRecipe: {recipe['name']}\nIngredients:{ingredients_str}\nInstructions:{recipe['instructions']}\n")
    else:
        print("No matching recipes found")

#find recipe by ingredient
def find_recipe_by_ingredients(available_ingredients):
    matching_recipe=[]
    for recipe in recipes:
        recipe_ingredients = [ingredient["item"] for ingredient in recipe["ingredients"]]
        if all(ingredient in recipe_ingredients for ingredient in available_ingredients):
            matching_recipe.append(recipe)
    return matching_recipe

def main():
    print("Welcome to the Recipe Book CLI Application!")

    while True:
        print("\nChoose an option:")
        print("1. List recipes")
        print("2. Query recipes")
        print("3. Search by ingredients")
        print("4. Exit")

        choice = input("Enter the number of your choice:")

        if choice == "1":
            list_recipes()
        elif choice =="2":
            query_recipe()
        elif choice == "3":
            available_ingredients = input("Enter the ingredients you have (comma-separated):").split(',')
            available_ingredients = [ingredient.strip() for ingredient in available_ingredients]

            matching_recipe = find_recipe_by_ingredients(available_ingredients)

            if matching_recipe:
                print("You can make the follwoing recipes:")
                for recipe in matching_recipe:
                    print(recipe["name"])
            else:
                print("No recipes found with the given ingredients.")
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else: 
            print("Invalid choice. Please choose again.")

if __name__ =="__main__":
    main()


