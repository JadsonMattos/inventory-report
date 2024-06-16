import datetime
from typing import List
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        oldest_manufacturing_date = min(
            [product.manufacturing_date for inventory in self.inventories
             for product in inventory.data]
        )
        closest_expiration_date = min(
            [product.expiration_date for inventory in self.inventories
             for product in inventory.data
             if product.expiration_date > datetime.datetime.now()
             .strftime('%Y-%m-%d')]
        )
        company_with_largest_inventory = max(
            set(
                [product.company_name for inventory in self.inventories
                 for product in inventory.data]
            ), key=[product.company_name for inventory in self.inventories
                    for product in inventory.data].count
        )

        stocked_products_by_company = "\n".join([
            f"- {company_name}: {product_count}"
            for company_name, product_count in sorted(
                self.get_stocked_products_by_company()
            )
        ])

        report = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: \
{company_with_largest_inventory}\n"
            f"Stocked products by company:\n{stocked_products_by_company}\n"
        )
        return report

    def get_stocked_products_by_company(self) -> List[tuple]:
        stocked_products = {}
        for inventory in self.inventories:
            for product in inventory.data:
                if product.expiration_date > datetime.datetime.now(
                ).strftime('%Y-%m-%d'):
                    if product.company_name in stocked_products:
                        stocked_products[product.company_name] += 1
                    else:
                        stocked_products[product.company_name] = 1
        return sorted(stocked_products.items())
