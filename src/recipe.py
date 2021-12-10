from ingredient import Ingredient


class RecipeLookup(object):
    def __init__(self):
        pass
    def get_ingredients(self, name):
        if name == "ceaser_salad":
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
    def __init__(self, lookup):
        self.ingredients = lookup.get_ingredients('ceaser_salad')
