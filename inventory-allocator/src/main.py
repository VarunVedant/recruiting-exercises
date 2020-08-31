import os

from utils.utils import Utils
from models.inventory import Inventory


def main():
    order_json_path = os.path.join(".", "data", "order.json")
    order = Utils.json_file_to_dict(order_json_path)

    inventory_json_path = os.path.join(".", "data", "inventory.json")
    inventory_info = Utils.json_file_to_dict(inventory_json_path)

    inventory = Inventory()
    inventory.load_inventory_data(inventory_info["warehouses"])
    
    final_shipment = inventory.fulfill_order(order)
    print(final_shipment)


if __name__ == "__main__":
    main()
