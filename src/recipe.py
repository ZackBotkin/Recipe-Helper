import os
from ingredient import Ingredient


class TextFileRecipeLookup(object):
    def __init__(self, recipe_dir):
        self.recipes = {}
        for filename in os.listdir(recipe_dir):
            recipe_name = filename.split('.txt')[0]
            with open('%s\\%s' % (recipe_dir, filename), 'r') as f:
                recipe_text = f.readline()
                ingredients = recipe_text.split(',')
                self.recipes[recipe_name] = []
                for ingredient_name in ingredients:
                    self.recipes[recipe_name].append(
                        Ingredient(ingredient_name)
                    )

    def get_ingredients(self, name):
        if name not in self.recipes:
            raise Exception("Cannot find recipe %s" % name)
        else:
            return self.recipes[name]

class Recipe(object):
    def __init__(self, recipe_name, lookup):
        self.ingredients = lookup.get_ingredients(recipe_name)
