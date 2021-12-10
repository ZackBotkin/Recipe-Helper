from recipe import Recipe, RecipeLookup
from emailer import Emailer, EmailerCreds
from ingredient import Ingredient
from fridge import Fridge, FridgeChecker



class Program(object):

    def __init__(self, emailer, fridge_checker):
        self.user = "zackbotkin@gmail.com"
        self.emailer = emailer
        self.fridge_checker = fridge_checker

    def run_recipe(self):
        lookup = RecipeLookup()
        recipe = Recipe(lookup)
        ingredients_to_buy = []
        for ingredient in recipe.ingredients:
            if not self.fridge_checker.has_item(ingredient):
                ingredients_to_buy.append(ingredient)
        self.emailer.email_ingredients(ingredients_to_buy, self.user)

def main():

    fridge = Fridge()
    fridge.add_item(Ingredient("Lettuce"))
    fridge_checker = FridgeChecker(fridge)

    creds = EmailerCreds("C:\\Users\\zackb\\emailer_creds\\creds.txt")
    emailer = Emailer(creds)

    program = Program(emailer, fridge_checker)
    program.run_recipe()


if __name__ == "__main__":
    main()
