from inventory_report.product import Product


def test_product_report() -> None:
    product_data = {
        "id": "1",
        "product_name": "farinha",
        "company_name": "Farinini",
        "manufacturing_date": "01-05-2021",
        "expiration_date": "02-06-2023",
        "serial_number": "TY68 409C JJ43 ASD1 PL2F",
        "storage_instructions": "precisa ser armazenado em local protegido \
da luz"
    }

    product = Product(**product_data)

    assert "The product 1 - farinha" in str(product)
    assert "with serial number TY68 409C JJ43 ASD1 PL2F" in str(product)
    assert "manufactured on 01-05-2021" in str(product)
    assert "by the company Farinini" in str(product)
    assert "valid until 02-06-2023" in str(product)
    assert "must be stored according to the following instructions: precisa \
ser armazenado em local protegido da luz" in str(product)
