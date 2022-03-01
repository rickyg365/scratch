


class Item:
    """

    """
    def __init__(self, id, name, type, reuse):
        self.id = id
        self.name = name
        self.type = type
        self.reuse = reuse
        self.used = False
        self.json = {
            'id': id,
            'name': name,
            'type': type,
            'reuse': reuse
        }

    def __str__(self):
        txt = f"[{self.id}] {self.name} {self.type}"
        return txt
    
    def use(self, player_obj):
        self.used = True
        return True, f"{self.name} used!"


class HealItem(Item):
    def __init__(self, id, name, reuse, amount):
        super().__init__(id, name, "heal", reuse)
        self.amount = amount

    def __str__(self):
        return super().__str__()

    def use(self, player_obj):
        heal_status, heal_result = player_obj.heal(self.amount)
        self.used = True
        return heal_status, heal_result


class Bag:
    """
    item_key: item_quantity
    """
    def __init__(self, pre_built_inventory=None):
        if pre_built_inventory is None:
            pre_built_inventory = {}
        self.items = pre_built_inventory

    def __str__(self):
        # txt = f"{'-'*40}"
        txt = f"\n[ {'BAG':^20} ]"
        txt += f"\n{'-'*24}"
        for item_key, item_qtty in self.items.items():
            txt += f"\n {item_qtty} {item_key}"
        txt += f"\n{'-'*24}"
        return txt

    def add_item(self, item_key, quantity):
        self.items[item_key] = quantity
    
    def use_item(self, item_key):
        # Check before use if in stock
        if self.items.get(item_key) <= 0:
            # remove from dict
            del self.items[item_key]
            return False, f"Failed to use item, none in stock..."
        
        self.items[item_key] -= 1

        if self.items[item_key] <= 0:
            del self.items[item_key]

        return True, f"{item_key} used!"


def main():
    # Test Item
    new_item = Item(9, 'item9', 'consumable', False)
    print(new_item)

    # Test Bag
    prebuit_inv = {
        'atk boost': 1,
        'hp boost': 1,
        'medicinal herb': 2,
        'small potion': 3,
        'medium potion': 1,
        'large potion': 1,
        'escape rope': 1,
    }
    new_bag = Bag(prebuit_inv)
    print(new_bag)


if __name__ == "__main__":
    main()

