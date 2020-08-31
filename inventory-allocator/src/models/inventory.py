import copy

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


    # def fulfill_order(self, order):
    #     items_to_order = order.keys()
    #     order_unfulfilled = copy.deepcopy(order)
    #     shipment = []

    #     for warehouse in self.warehouses:
    #         warehouse_stock = warehouse.chk_stocks(order)
    #         # print(warehouse_stock)

    def stage_items_for_shipment(self, shipment, order, item, warehouse_name, item_stock):
        is_warehouse_unused = True
        
        item_staging_qty = order[item] if order[item] < item_stock else item_stock

        for warehouse in shipment:
            if warehouse_name in warehouse.keys():
                warehouse[warehouse_name][item] = item_staging_qty
                order[item] -= item_staging_qty
                is_warehouse_unused = False
                break
        if is_warehouse_unused:
            shipment.append({warehouse_name: {item: item_staging_qty}})
            order[item] -= item_staging_qty


    def remove_unfulfilled_items(self, order, order_unfulfilled, shipment):
        for warehouse in shipment:
            # print(warehouse, list(warehouse.values())[0])
            inventory_to_ship = list(warehouse.values())[0]
            for item in order.keys():
                if (item in inventory_to_ship) and (order_unfulfilled[item] != 0):
                    inventory_to_ship.pop(item, None)
                else:
                    continue
            if not inventory_to_ship:
                shipment.remove(warehouse)


    def fulfill_order(self, order):
        items_to_order = order.keys()
        order_unfulfilled = copy.deepcopy(order)
        shipment = []

        for warehouse in self.warehouses:
            for item in items_to_order:
                item_stock = warehouse.chk_item_availability(item)
                item_left = order_unfulfilled[item]
                items_to_fulfill = item_left if item_left < item_stock else item_stock
                if item_left <= 0:
                    continue
                else:
                    self.stage_items_for_shipment(shipment, order_unfulfilled, item, warehouse.name, item_stock)

        self.remove_unfulfilled_items(order, order_unfulfilled, shipment)
        return shipment