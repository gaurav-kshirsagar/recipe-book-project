from recipe_book import Recipe

class User:
    def __init__(self,):
        self.name = None
        self.email = None
        self.recipe_book = Recipe()
        # self.password = password
    
    def add_user(self):
        self.name = input("\nEnter your name: ")
        self.email = input("\nEnter your email: ")
    
    def view_user(self):
        print(f'Your name: {self.name}')
        print(f'Your email: {self.email}')

    def upadte_user(self):
        print(f'Your name: {self.name} and Email" {self.email} ')
        print("\nPlease update your information: ")
        self.name = input("\nEnter your name: ")
        self.email = input("\nEnter your email: ")
