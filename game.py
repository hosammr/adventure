import json

from location import Location
from item import Item


class Game:
    def __init__(self, name, location=None, target=None, locations=None, items=None):
        self.name = name
        self.locations = {
            location["name"]: Location(**location) for location in (locations or [])
        }
        self.items = {item["name"]: Item(**item) for item in (items or [])}

        self.location = self.find_location(
            location, locations[0]["name"] if locations else None
        )
        self.target = self.find_location(
            target, locations[-1]["name"] if locations else None
        )

    def __str__(self):
        return self.name

    @classmethod
    def load(cls, filename):
        print('Loading game "%s"' % filename)
        with open(filename) as fin:
            data = json.load(fin)
        return Game(**data)

    def find_location(self, location, default=None):
        if len(self.locations) > 0:
            if location in self.locations:
                return self.locations[location]
            elif default in self.locations:
                return self.locations[default]
        return None

    def is_done(self):
        return self.location == self.target

    def move(self, destination):
        new_location = self.find_location(destination)
        if new_location == self.location:
            raise KeyError("Daar ben je al.")
        elif new_location and self.location.is_accessible(destination):
            self.location = new_location
        else:
            raise KeyError(
                "%s is vanuit %s niet te bereiken" % (destination, self.location)
            )

    def get(self, item):
        item = self.location.get(item)
        if item:
            self.items[item.name] = item

    def drop(self, item):
        if item in self.items:
            item = self.items.pop(item)
            self.location.drop(item)
        else:
            raise KeyError("Je hebt geen %s" % item)

    def describe(self, key):
        description = 'Een "%s" kan je hier niet zien.' % key
        if key == self.location.name:
            location = self.location
            description = location.description
            if len(location.items) > 0:
                items = [str(item) for item in location.items]
                description += "\nEr liggen hier: %s" % ", ".join(items)
            if len(location.exits) > 0:
                exits = [str(out) for out in location.exits]
                description += "\nJe kunt naar: %s" % ", ".join(exits)
        elif key in self.location.items:
            description = self.location.items[key].description
        elif key in self.items:
            description = self.items[key].description
        elif key == "spullen":
            items = [str(item) for item in self.items]
            description = ", ".join(items)

        return description
