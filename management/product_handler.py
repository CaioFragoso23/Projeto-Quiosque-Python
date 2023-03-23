from menu import products


def get_product_by_id(id):
    for x in products:
        list_id = x.get("_id")
        if list_id == id:
            return x
    nothing = {}
    return nothing
    ...


def get_products_by_type(type):
    filtered_list = []
    for x in products:
        list_type = x.get("type")
        if list_type == type:
            filtered_list.append(x)
    return filtered_list
    ...