import datetime
from typing import List
from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self):
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing_date = min(
            [product.manufacturing_date for inventory in self.inventories
             for product in inventory.data]
        )
        closest_expiration_date = min(
            [product.expiration_date for inventory in self.inventories
             for product in inventory.data if product.expiration_date >
             datetime.datetime.now().strftime('%Y-%m-%d')]
        )
        company_with_largest_inventory = max(
            set(
                [product.company_name for inventory in self.inventories
                 for product in inventory.data]
            ), key=[product.company_name for inventory in self.inventories
                    for product in inventory.data].count
        )

        report = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: \
{company_with_largest_inventory}"
        )
        return report
