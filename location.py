import json

from item import Item


class Location:
    def __init__(self, name, description=None, exits=None, items=None):
        self.name = name
        self.description = description or ""
        self.exits = exits or []
        self.items = {item["name"]: Item(**item) for item in (items or [])}

    def __str__(self):
        return self.name

    def is_accessible(self, destination):
        return destination in self.exits

    def get(self, item):
        if item in self.items:
            return self.items.pop(item)
        else:
            raise KeyError("Er is geen %s in %s" % (item, self))

    def drop(self, item):
        self.items[item.name] = item
