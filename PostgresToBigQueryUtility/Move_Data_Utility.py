import pandas as pd
import psycopg2
from google.cloud import bigquery

# PostgreSQL connection parameters
pg_host = "localhost"
pg_database = "Brazil_Sales"
pg_user = "postgres"
pg_password = "postgres"

# SQL queries
order_items_query = "SELECT * FROM stage_sales.order_items"
products_query = "SELECT * FROM stage_sales.products"
orders_query = "SELECT * FROM stage_sales.orders"
category_translation_query = "SELECT * FROM stage_sales.product_category_name_translation"

# Extract data
with psycopg2.connect(host=pg_host, database=pg_database, user=pg_user, password=pg_password) as conn:
    order_items_df = pd.read_sql_query(order_items_query, conn)
    products_df = pd.read_sql_query(products_query, conn)
    orders_df = pd.read_sql_query(orders_query, conn)
    category_translation_df = pd.read_sql_query(category_translation_query, conn)

# BigQuery Client

client = bigquery.Client(project="brazilian-ecommerce-457518")
dataset_id = "brazil_sales"


def load_df_to_bigquery(df, table_name):
    table_id = f"{client.project}.{dataset_id}.{table_name}"
    job_config = bigquery.LoadJobConfig(write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE)
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()
    print(f"Loaded {df.shape[0]} rows into {table_id}")


# Example usage for your tables:
load_df_to_bigquery(order_items_df, "order_items")
load_df_to_bigquery(products_df, "products")
load_df_to_bigquery(orders_df, "orders")
load_df_to_bigquery(category_translation_df, "category_translation")



