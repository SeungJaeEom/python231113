#엑셀파일쓰기.py
from openpyxl import Workbook
from random import randint, uniform

def generate_sample_data():
    products = [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Smartphone", "price": 499.99},
        {"id": 3, "name": "Tablet", "price": 299.99},
        {"id": 4, "name": "Headphones", "price": 79.99},
        {"id": 5, "name": "Smartwatch", "price": 149.99}
    ]

    sample_data = []

    for _ in range(100):
        product = products[randint(0, len(products) - 1)]
        quantity = randint(1, 10)
        total_price = round(quantity * product["price"], 2)

        sample_data.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity,
            "total_price": total_price
        })

    return sample_data

def write_to_excel(data):
    wb = Workbook()
    ws = wb.active

    # write the column names to the first row of the sheet
    ws.append(["Product ID", "Product Name", "Price", "Quantity", "Total Price"])

    for row in data:
        ws.append([row["id"], row["name"], row["price"], row["quantity"], row["total_price"]])

    # Save the workbook to a file
    file_path = 'sales.xlsx'
    wb.save(file_path)
    print(f"Data written to {file_path}")

if __name__ == "__main__":
    sample_data = generate_sample_data()
    write_to_excel(sample_data)

