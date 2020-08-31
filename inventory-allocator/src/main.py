import os

from utils.utils import Utils
from models.inventory import Inventory


def main():
    cart_json_path = os.path.join(".", "data", "cart.json")
    cart = Utils.json_file_to_dict(cart_json_path)

    inventory_json_path = os.path.join(".", "data", "inventory.json")
    inventory_info = Utils.json_file_to_dict(inventory_json_path)

    inventory = Inventory()
    inventory.load_inventory_data(inventory_info["warehouses"])
    
    print(inventory.warehouses)


if __name__ == "__main__":
    main()
