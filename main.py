from management import product_handler
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(product_handler.get_product_by_id(25))
    print(product_handler.get_products_by_type("fruit"))
    ...
