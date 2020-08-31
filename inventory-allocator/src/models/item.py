import os

from utils.utils import Utils

class Item:

    def __init__(self):
        self.name = ""

    
    @staticmethod
    def list_of_items_sold():
        inventory_json_path = os.path.join(".", "data", "inventory.json")
        inventory_info = Utils.json_file_to_dict(inventory_json_path)
        
        items_sold = {}
        item_id = 0
        for warehouse in inventory_info:
            inventory = warehouse["inventory"]
            for item in inventory:
                if item not in items_sold:
                    items_sold[item_id] = item