
class Warehouse:

    def __init__(self):
        self.name = ""
        self.inventory = {}


    def load_warehouse_data(self, warehouse_data):
        """
        Initialize Warehouse info.
        :param warehouse_data: dict with warehouse name and inventory data.
        """
        self.name = warehouse_data["name"]
        self.inventory = warehouse_data["inventory"]


    def chk_item_availability(self, item) -> int:
        """
        Check the amount of stock for a given item in warehouse.
        :param item: Item name.
        :return: Amount of stock available in warehouse.
        """
        return self.inventory[item] if item in self.inventory.keys() else 0
