from management import product_handler
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    # print(product_handler.get_product_by_id(25))
    # print(product_handler.get_products_by_type("fruit"))

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(product_handler.add_product(products, **new_product))

    # print(product_handler.menu_report())

    ...
