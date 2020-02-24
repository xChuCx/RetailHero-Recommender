import pandas as pd


def parse_data(query_data):
    client = query_data.get("client_id", None)
    history = query_data.get("transaction_history", None)
    products = []

    if not client:
        return None, None

    if history:
        for session in history:
            session_products = session.get("products", None)
            if session_products:
                for product in session_products:
                    products.append([client, product["product_id"]])
        return client, pd.DataFrame(products, columns=["client_id", "product_id"])
    else:
        return None, None
