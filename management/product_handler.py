from menu import products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
        ...

    for x in products:
        list_id = x.get("_id")
        if list_id == id:
            return x
    nothing = {}
    return nothing
    ...


def get_products_by_type(type_name):
    if type(type_name) != str:
        raise TypeError("product type must be a str")
        ...
    filtered_list = []
    for x in products:
        list_type = x.get("type")
        if list_type == type_name:
            filtered_list.append(x)
    return filtered_list
    ...


def add_product(menu: list[dict[str]], **product):

    id_list = []
    if len(menu) > 0:
        for x in menu:
            product_id = x.get("_id")
            id_list.append(product_id)
    else:
        id_list.append(0)
        ...
    
    highest_id = max(id_list)
    new_id = highest_id + 1
    product.update({"_id": new_id})
    menu.append(product)
    return product
    ...


def menu_report():
    products_count = len(products)
    total_value = []
    all_types = []
    for product in products:
        product_value = product.get("price")
        total_value.append(product_value)
        
        product_type = product.get("type")
        all_types.append(product_type)
        ...
    type_most_recurrent = max(set(all_types), key=all_types.count)
    sum_values = sum(total_value)
    average_price = round(sum_values / products_count, 2)
    
    return f"Products Count: {products_count} - Average Price: ${average_price} - Most Common Type: {type_most_recurrent}"
    ...

