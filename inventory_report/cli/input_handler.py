from typing import List
from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    importers = {
        '.json': JsonImporter,
        '.csv': CsvImporter,
    }

    if report_type not in ['simple', 'complete']:
        raise ValueError("Report type is invalid.")

    data = []
    for file_path in file_paths:
        file_extension = file_path.split('.')[-1]
        if file_extension not in importers:
            continue

        importer = importers[file_extension](file_path)
        imported_data = importer.import_data()
        if imported_data:
            data.extend(imported_data)

    inventory = Inventory()
    for product in data:
        inventory.add_product(product)
    if report_type == 'simple':
        report = SimpleReport()
    else:
        report = CompleteReport()

    report.generate(inventory)
    return report.generate()
