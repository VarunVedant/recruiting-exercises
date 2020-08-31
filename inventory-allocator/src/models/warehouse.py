
class Warehouse:

    def __init__(self):
        self.name = ""
        self.inventory = {}


    def load_warehouse_data(self, warehouse_data):
        # print(warehouse_data)
        self.name = warehouse_data["name"]
        self.inventory = warehouse_data["inventory"]
        # for item in inventory.keys():
        #     self.inventory[item] = inventory[item]


    def chk_item_availability(self, item):
        if item in self.inventory.keys():
            return self.inventory[item]
        return 0
    
    
    def chk_stocks(self, order):
        items_in_inventory = self.inventory.keys()
        item_stock = {}

        for item in order:
            qty = 0
            if item in items_in_inventory:
                qty = self.inventory[item]
            item_stock[item] = qty
        
        return item_stock