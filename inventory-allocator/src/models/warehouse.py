
class Warehouse:

    def __init__(self):
        self.name = ""
        self.inventory = {}


    def load_warehouse_data(self, warehouse_data):
        print(warehouse_data)
        self.name = warehouse_data["name"]
        self.inventory = warehouse_data["inventory"]
        # for item in inventory.keys():
        #     self.inventory[item] = inventory[item]

