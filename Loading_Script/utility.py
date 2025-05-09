import pandas as pd

path = "E:/dataEngineering/Brazilian_Sales_New/Dataset/"
file_names = [
    f"{path}customers.csv",
    f"{path}geolocation.csv",
    f"{path}order_items.csv",
    f"{path}order_payments.csv",
    f"{path}order_reviews.csv",
    f"{path}orders.csv",
    f"{path}product_category_name_translation.csv",
    f"{path}products.csv",
    f"{path}sellers.csv",
]


customers_df = pd.read_csv(file_names[0])
geolocation_df = pd.read_csv(file_names[1])
order_items_df = pd.read_csv(file_names[2])
order_payments_df = pd.read_csv(file_names[3])
order_reviews_df = pd.read_csv(file_names[4])
orders_df = pd.read_csv(file_names[5])
product_category_name_translation_df = pd.read_csv(file_names[6])
products_df = pd.read_csv(file_names[7])
sellers_df = pd.read_csv(file_names[8])

print(sellers_df)


from sqlalchemy import create_engine

local_host = "localhost"
username = "postgres"
password = "postgres"
port = "5432"
database = "Brazil_Sales"
schema = "stage_sales"


db_url = f"postgresql://{username}:{password}@{local_host}:{port}/{database}"

engine = create_engine(db_url)

print(engine)

# Assuming you have the engine created as in the previous response

# Load each DataFrame into a PostgreSQL table
customers_df.to_sql('customers', engine, schema=schema, if_exists='replace', index=False)
geolocation_df.to_sql('geolocation', engine, schema=schema, if_exists='replace', index=False)
order_items_df.to_sql('order_items', engine, schema=schema, if_exists='replace', index=False)
order_payments_df.to_sql('order_payments', engine, schema=schema, if_exists='replace', index=False)
order_reviews_df.to_sql('order_reviews', engine, schema=schema, if_exists='replace', index=False)
orders_df.to_sql('orders', engine, schema=schema, if_exists='replace', index=False)
product_category_name_translation_df.to_sql('product_category_name_translation', engine, schema=schema, if_exists='replace', index=False)
products_df.to_sql('products', engine, schema=schema, if_exists='replace', index=False)
sellers_df.to_sql('sellers', engine, schema=schema, if_exists='replace', index=False)

print("Data loading to PostgreSQL tables complete!")