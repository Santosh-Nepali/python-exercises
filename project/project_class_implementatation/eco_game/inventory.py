"""
inventory.py
Defies the inventory holding the lists of WasteItem objects the players is carrying at the moment
"""

class Inventory:

    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        new_items = []

        for i in self.items:
            if i is not item:
                new_items.append(i)

        self.items = new_items

    def find_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item

        return None

    def names(self):
        item_names = []

        for item in self.items:
            item_names.append(item.name)

        return item_names

    def show(self):
        if self.is_empty():
            print('Your inventory is empty.')
        else:
            print('Your inventory contains:')

            for item in self.items:
                print(' - ' + item.name)
