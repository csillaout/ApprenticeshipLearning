import pickle # Module Usage

recipes = []

def load_recipes(filename):
    try:
        with open(filename, 'rb') as file: #Pickling and Unpickling, File Modes
            unpickler = pickle.Unplickler(file) #Unpickler Class
            return unpickler.load()
    except FileNotFoundError:
        return []

def save_recipes(recipes, filename):
    try:
        with open(filename, 'wb') as file: #Pickling and Unpickling, File Modes
            pickler = pickle.Pickler(file) #Pickler Class
            pickler.dump(recipes)
    except pickle.PickleError:
        print("Failed to save recipes.")

def pickle_to_bytes(recipes): #Pickling without a file
    return pickle.dumps(recipes)

def unpickle_to_bytes(pickled_data): #Unpickling without a file
    return pickle.loads(pickled_data)

def add_recipe():
    name = input("Enter the recipe name:")
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    instructions = input("Enter the insturctions: ")
    prep_time = int(input("Enter the prep time (in minutes):"))

    recipe = {
        "name": name,
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "instructions": instructions,
        "prep_time": prep_time
    }

    recipes.append(recipe)
    print("Recipe added successfully!")

    #find recipe by name
def query_recipe():
    query_name = input("Enter the name of the recipe you want ot saerch for:")

    found_recipes = [recipe for recipe in recipes if query_name.lower() in recipe["name"].lower()]

    if found_recipes:
        print(f"Found {len(found_recipes)} matching recipes:")
        for recipe in found_recipes:
            print(f"\nRecipe: {recipe['name']}\nIngredients:{', '.join(recipe['ingredients'])}\nInstructions:{recipe['instructions']}\nPrep Time:{recipe['prep_time']} minutes\n")
    else:
        print("No matching recipes found")

#find recipe by ingredient
def find_recipe_by_ingredients(available_ingredients):
    matching_recipe=[]
    for recipe in recipes:
        if all(ingredient in recipe['ingredients'] for ingredient in available_ingredients):
            matching_recipe.append(recipe)
    return matching_recipe

def main():
    global recipes # to ensure we are modifying the global recipes list
    filename = 'recipes.pkl'
    recipes = load_recipes(filename)

    print("Welcome to the Recipe Book CLI Application!")

    while True:
        print("\nChoose an option:")
        print("1. Add a new recipe")
        print("2. Query recipes")
        print("3. Search by ingredients")
        print("4. Exit")

        choice = input("Enter the number of your choice:")

        if choice == "1":
            add_recipe()
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
            save_recipes(recipes,filename) # saving recipes before exiting
            print("Exiting the application. Goodbye!")
            break
        else: 
            print("Invalid choice. Please choose again.")

if __name__ =="__main__":
    main()


