import argparse

from recipe import Recipe, RecipeLookup
from emailer import Emailer, EmailerCreds
from ingredient import Ingredient
from fridge import Fridge, FridgeChecker
from contact_book import ContactBook



class Program(object):

    def __init__(self, emailer, fridge_checker, emailing_list):
        self.emailing_list = emailing_list
        self.emailer = emailer
        self.fridge_checker = fridge_checker

    def run_recipe(self, recipe_name):
        recipe = Recipe(recipe_name, RecipeLookup())
        ingredients_to_buy = []
        for ingredient in recipe.ingredients:
            if not self.fridge_checker.has_item(ingredient):
                ingredients_to_buy.append(ingredient)

        ## TODO : no need to reformat the message for each recipient
        for recipient in self.emailing_list:
            self.emailer.email_ingredients(
                ingredients_to_buy, recipient
            )


def main():

    default_recipe = 'ceasar_salad'

    parser = argparse.ArgumentParser(description='default parser')
    parser.add_argument('--recipe', help='the recipe')
    parser.add_argument('--to', help='the email recipient')
    args = parser.parse_args()

    recipe = default_recipe
    if args.recipe == '' or args.recipe is None:
        print('No recipe given, going with default')
    else:
        recipe = args.recipe

    recipient = 'zackbotkin@gmail.com'
    if not (args.to == '' or args.to is None):
        recipient = args.to

    contact_book = ContactBook("C:\\Users\\zackb\\contact_book\\contact_book.txt")

    recipient = contact_book.lookup_recipient(recipient)


    fridge = Fridge()
    fridge.add_item(Ingredient("Lettuce"))
    fridge_checker = FridgeChecker(fridge)

    creds = EmailerCreds("C:\\Users\\zackb\\emailer_creds\\creds.txt")
    emailer = Emailer(creds)

    program = Program(emailer, fridge_checker, [recipient])
    program.run_recipe(recipe)


if __name__ == "__main__":
    main()
