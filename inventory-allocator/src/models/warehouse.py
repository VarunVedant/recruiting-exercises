
class Warehouse:

    def __init__(self, name="", inventory=None):
        if inventory is None:
            inventory = {}
        self.name = name
        self.inventory = inventory


    @classmethod
    def load_warehouse_data(cls, warehouse_data):
        """
        Factory method to create warehouse.
        :param warehouse_data: dict with warehouse name and inventory data.
        :return: Returns Warehouse object after loading warehouse data.
        """
        return cls(warehouse_data["name"], warehouse_data["inventory"])


    def chk_item_availability(self, item) -> int:
        """
        Check the amount of stock for a given item in warehouse.
        :param item: Item name.
        :return: Amount of stock available in warehouse.
        """
        return self.inventory[item] if item in self.inventory.keys() else 0
