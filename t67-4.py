def analyze_purchases(purchases: list) -> dict:
    customer_check = {}
    product_check = {}
    result = {}
    for customer, category, product in purchases:
        if customer not in customer_check:
            customer_check[customer] = {}

        if category not in customer_check[customer]:
            customer_check[customer][category] = {}

        if product in customer_check[customer][category]:
            customer_check[customer][category][product] += 1
        else:
            customer_check[customer][category][product] = 1
        if category not in product_check:
            product_check[category] = {}
        if product in product_check[category]:
            product_check[category][product] += 1
        else:
            product_check[category][product] = 1

    for customer, categories in customer_check.items():
        result[customer] = {}

        for category, products in categories.items():
            duplicate_count = 0

            for product, count in products.items():
                if count > 1:
                    duplicate_count += count
            if duplicate_count > 0:
                result[customer][category] = duplicate_count

    most_frequent = {}
    for category, products in product_check.items():
        max_count = 0
        choices = []

        for product, count in products.items():
            if count > max_count:
                max_count = count
                choices = [product]
            elif count == max_count:
                choices.append(product)
        most_frequent[category] = sorted(choices)[0]

    result["most_frequent"] = most_frequent

    return result


purchases = [
    ("cust1", "electronics", "laptop"),
    ("cust2", "groceries", "apple"),
    ("cust1", "electronics", "laptop"),
    ("cust1", "electronics", "mouse"),
    ("cust2", "groceries", "apple"),
    ("cust2", "groceries", "banana"),
    ("cust3", "groceries", "banana"),
    ("cust3", "groceries", "apple"),
    ("cust3", "electronics", "camera"),
]


print(analyze_purchases(purchases))