import unittest

from models.inventory import Inventory

class TestInventory(unittest.TestCase):

    def test_fulfill_order_one_warehouse(self):
        order = { "apple": 1 }
        inventory_info = [{ "name": "owd", "inventory": { "apple": 1 } }]

        inventory = Inventory.load_inventory_data(inventory_info)
        final_shipment = inventory.fulfill_order(order)
        expected_shipment = [{ "owd": { "apple": 1 } }]
        self.assertEqual(final_shipment, expected_shipment)


    def test_fulfill_order_multi_warehouse(self):
        order = { "apple": 10 }
        inventory_info = [
            { "name": "owd", "inventory": { "apple": 5 } },
            { "name": "dm", "inventory": { "apple": 5 }}
        ]

        inventory = Inventory.load_inventory_data(inventory_info)
        final_shipment = inventory.fulfill_order(order)
        expected_shipment = [{ "dm": { "apple": 5 }}, { "owd": { "apple": 5 } }]
        self.assertEqual(final_shipment, expected_shipment)


    def test_fulfill_order_no_inventory_1(self):
        order = { "apple": 1 }
        inventory_info = [{ "name": "owd", "inventory": { "apple": 0 } }]

        inventory = Inventory.load_inventory_data(inventory_info)
        final_shipment = inventory.fulfill_order(order)
        expected_shipment = []
        self.assertEqual(final_shipment, expected_shipment)


    def test_fulfill_order_no_inventory_2(self):
        order = { "apple": 2 }
        inventory_info = [{ "name": "owd", "inventory": { "apple": 1 } }]

        inventory = Inventory.load_inventory_data(inventory_info)
        final_shipment = inventory.fulfill_order(order)
        expected_shipment = []
        self.assertEqual(final_shipment, expected_shipment)


    def test_fulfill_order_multi_items(self):
        order = {"apple": 5, "banana": 5, "orange": 5}
        inventory_info = [
            {"name": "owd", "inventory": {
                "apple": 5,
                "orange": 10
            }}, {"name": "dm", "inventory": {
                "banana": 5,
                "orange": 10
            }}
        ]
        inventory = Inventory.load_inventory_data(inventory_info)
        final_shipment = inventory.fulfill_order(order)
        expected_shipment = [
            {'dm': {'banana': 5}},
            {'owd': {'apple': 5, 'orange': 5}}
        ]
        self.assertEqual(final_shipment, expected_shipment)

if __name__ == '__main__':
    unittest.main()