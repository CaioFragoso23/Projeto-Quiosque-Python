from menu import products


def calculate_tab(dict_list: list[dict]):
    subtotal_values = []
    for dict in dict_list:
        product_id = dict.get("_id")
        product_amount = dict.get("amount")
        for product in products:
            product_menu_id = product.get("_id")
            if product_menu_id == product_id:
                product_menu_price = product.get("price")
                product_total = product_amount * product_menu_price
                subtotal_values.append(product_total)
                ...
            ...
    sum_subtotal_values = round(sum(subtotal_values), 2)
    # subtotal_values.append(list_values)
    total = {"subtotal": "$" + str(sum_subtotal_values)}
    return total
    ...