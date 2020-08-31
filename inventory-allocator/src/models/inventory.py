import copy

from models.warehouse import Warehouse


class Inventory:

    def __init__(self, warehouses=None):
        self.warehouses = [] if warehouses is None else warehouses


    @classmethod
    def load_inventory_data(cls, inventory_data):
        """
        Factory method to create an inventory.
        :param inventory_data: A list of warehouses with their respective inventories.
        :returns: Returns Inventory object after loading inventory data.
        """
        warehouses = []
        for warehouse_data in inventory_data:
            warehouse = Warehouse.load_warehouse_data(warehouse_data)
            warehouses.append(warehouse)
        return cls(warehouses)


    def stock_to_commit_from_warehouse(self, items_left, items_in_curr_warehouse) -> int:
        """
        The Item count to commit from current warehouse to fulfill shipment.
        :param items_left: Total no. of the item left to be added to shipment staging area.
        :param items_in_curr_warehouse: Total stock of the item in the warehouse under consideration.
        :rtype: An int
        """
        return items_left if items_left < items_in_curr_warehouse else items_in_curr_warehouse


    def stage_items_for_shipment(self, shipment, order_left, item, warehouse_name, item_stock):
        """
        Commit stocks of item from the warehouse for shipment.
        :param shipment: Shipment having amt of items to be shipped from warehouses.
        :param order_left: Items and their quantities left to be fulfilled.
        :param item: The Item staged for shipment
        :param warehouse_name: The name of warehouse which will commit its stock for shipment.
        :param item_stock:  The stock of warehouse to be committed for shipment.
        """
        is_warehouse_unused = True
        
        item_staging_qty = order_left[item] if order_left[item] < item_stock else item_stock

        for warehouse in shipment:
            if warehouse_name in warehouse.keys():
                warehouse[warehouse_name][item] = item_staging_qty
                order_left[item] -= item_staging_qty
                is_warehouse_unused = False
                break

        if is_warehouse_unused:
            shipment.append({warehouse_name: {item: item_staging_qty}})
            order_left[item] -= item_staging_qty


    def remove_unfulfilled_items(self, order, order_unfulfilled, shipment):
        """
        Remove items without enough inventory from shipment.
        It is assumed that only items which do not have inventory are not shipped, and not the entire order.
        :param order: The order placed.
        :param order_unfulfilled: The order to be completed.
        :param shipment: The shipment of items from each warehouse met so far.
        """
        for warehouse in shipment:
            inventory_to_ship = list(warehouse.values())[0]
            for item in order.keys():
                # Remove item which is readied to be shipped but still hasn't met the desired amount in the order.
                if (item in inventory_to_ship) and (order_unfulfilled[item] != 0):
                    inventory_to_ship.pop(item, None)
                else:
                    continue
            # None of the items to be shipped from the curr warehouse have met the desired amt in the order.
            if not inventory_to_ship:
                shipment.remove(warehouse)


    def fulfill_order(self, order):
        """
        Generate shipment to meet order.
        :param order: dictionary of items and their respective qty.
        :return: Items and their respective qty from each warehouse to be shipped.
        """
        items_to_order = order.keys()
        order_unfulfilled = copy.deepcopy(order)
        shipment = []

        for warehouse in self.warehouses:
            for item in items_to_order:
                item_stock = warehouse.chk_item_availability(item)
                item_left = order_unfulfilled[item]
                
                items_to_fulfill = self.stock_to_commit_from_warehouse(item_left, item_stock)

                # The current item has not met the quantity desired by the order, and won't be shipped yet.
                if items_to_fulfill <= 0:
                    continue
                self.stage_items_for_shipment(shipment, order_unfulfilled, item, warehouse.name, item_stock)

        self.remove_unfulfilled_items(order, order_unfulfilled, shipment)
        return shipment