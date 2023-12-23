class Recipe:
    
    def __init__(self):
        self.recipe_book:list = []

    def add_to_recipe(self):
        self.recipe_book.append(input("Enter the recipe you want to add: "))
        print(self.recipe_book)

    def view_recipe(self,):
        if not self.recipe_book:
            print('There is no recipe in you book. Please add recipe!')
        else:
            print(f'Your recipe book is here..{self.recipe_book}')

    def remove_recipe(self,):
        recipe_to_remove = input("\nEnter the recipe you want  to remove from recipe book: ")
        if recipe_to_remove in self.recipe_book:
            self.recipe_book.remove(recipe_to_remove)
            print(f'{recipe_to_remove} recipe is removed..')       
        else:
            print("There is no such a recipe to remove!!")

    

