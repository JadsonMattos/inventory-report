from abc import ABC, abstractmethod
import csv
import json
from typing import Dict, List, Type
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            products_data = json.load(file)

        products = []
        for data in products_data:
            product = Product(
                id=data["id"],
                product_name=data["product_name"],
                company_name=data["company_name"],
                manufacturing_date=data["manufacturing_date"],
                expiration_date=data["expiration_date"],
                serial_number=data["serial_number"],
                storage_instructions=data["storage_instructions"],
            )
            products.append(product)
        return products


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        products = []
        with open(self.path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                product = Product(
                    id=row["id"],
                    product_name=row["product_name"],
                    company_name=row["company_name"],
                    manufacturing_date=row["manufacturing_date"],
                    expiration_date=row["expiration_date"],
                    serial_number=row["serial_number"],
                    storage_instructions=row["storage_instructions"],
                )
                products.append(product)
        return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
