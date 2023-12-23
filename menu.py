from user import User
from recipe_book import Recipe
is_exit = 0
is_back = 0
user = User()

user.add_user()

while is_exit == 0:
        # print("\nEnter your choice :")
        # print("\nEnter Profile to enter  into profile\nEnter Recipe Book for recipe book option ")
        print("\nEnter Profile to enter into profile\nEnter Recipe Book for recipe book option\n Enter Exit to exit")

        inp = input("Enter your choice :")
        if inp == "Profile" or inp ==  "Recipe Book":
             is_back = 0
        elif inp == "Exit":
             is_exit = 1
             is_back = 1
             
        while is_back == 0:
            if inp == "Profile":
                print("\nEnter View to view the users:\nEnter Back to main menu ")
                inpt = input("Enter your choice: ")
                if inpt == "View":
                     user.view_user()
                elif inpt == "Back":
                     is_back = 1

            elif inp == "Recipe Book":
                #  recipe = Recipe()
                print("\n Press 1 to Add Recipe\n Press 2 to View Recipes\n Press 3 to Remove Recipe\n Press 4 to Back ")
                number = input("Enter your choice: ")
                if number == "1":
                    user.recipe_book.add_to_recipe()
                elif number =="2":
                    user.recipe_book.view_recipe()
                elif number == "3":
                    user.recipe_book.remove_recipe()
                elif number == "4":
                    is_back = 1
            
                    print("Bye, Thank you!")
        