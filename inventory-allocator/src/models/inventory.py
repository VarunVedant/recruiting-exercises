from models.warehouse import Warehouse


class Inventory:

    def __init__(self, warehouses=None):
        if warehouses is None:
            warehouses = []
        self.warehouses = warehouses

    @classmethod
    def instantiate_default_inventory(cls):
        return cls()

    def load_inventory_data(self, inventory_data):
        for warehouse_data in inventory_data:
            warehouse = Warehouse()
            warehouse.load_warehouse_data(warehouse_data)
            self.warehouses.append(warehouse)