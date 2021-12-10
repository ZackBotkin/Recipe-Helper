from ingredient import Ingredient


CAESAR_SALAD = ['caesar_salad', 'ceasar_salad', 'caeser_salad', 'ceaser_salad']

class RecipeLookup(object):
    def __init__(self):
        pass
    def get_ingredients(self, name):
        if name in CAESAR_SALAD:
            return [
                Ingredient("Lettuce"),
                Ingredient("Dill"),
                Ingredient("Mayonaise"),
                Ingredient("Anchovies"),
                Ingredient("Parmesean"),
                Ingredient("Croutons"),
                Ingredient("Salt"),
                Ingredient("Pepper")
            ]
        else:
            raise Exception("Unknown recipe %s" % name)

class Recipe(object):
    def __init__(self, recipe_name, lookup):
        self.ingredients = lookup.get_ingredients(recipe_name)
