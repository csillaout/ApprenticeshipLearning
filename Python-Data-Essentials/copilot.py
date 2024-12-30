
name = input("What is your nanme?:")
def welcome_message(name, my_list):
    
    """
    This function checks if a name is in the list and prints a welcome message if it is.
    Otherwise, it prints a message saying the name is not in the team.
    
    :param name: The name to check in the list.
    :param my_list: The list of names to check against.
    """
    if name in my_list:
        print(f"Hi, {name}, welcome to the team!")
    else:
        print(f"Sorry, {name}, you are not in the team :(")
my_list = ["Alice", "Bob", "Charlie", "David"]
welcome_message(name, my_list)