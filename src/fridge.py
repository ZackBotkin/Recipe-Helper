
class Fridge(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name not in self.items:
            self.items[item.name] = 0
        self.items[item.name] += 1

    def has_item(self, item):
        return item.name in self.items and self.items[item.name] > 0

class FridgeChecker(object):

    def __init__(self, fridge):
        self.fridge = fridge

    def has_item(self, item):
        return self.fridge.has_item(item)
