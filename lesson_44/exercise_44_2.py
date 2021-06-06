from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    discount: float


class Collection:
    def __init__(self):
        self.items = []

    @classmethod
    def create_with_items(cls, *args):
        collection = cls()
        collection.items.extend(args)
        return collection


item1 = Item('chleb', 4, 0.1)
item2 = Item('mleko', 5, 0.2)

col = Collection.create_with_items(item1, item2)
print(col.items)
