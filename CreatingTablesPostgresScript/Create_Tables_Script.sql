-- Customers Table
CREATE TABLE stage_sales.customers (
    customer_id VARCHAR(32) PRIMARY KEY,
    customer_unique_id VARCHAR(32),
    customer_zip_code_prefix VARCHAR(5),
    customer_city VARCHAR(50),
    customer_state VARCHAR(2)
);

-- Geolocation Table
CREATE TABLE stage_sales.geolocation (
    geolocation_zip_code_prefix VARCHAR(5),
    geolocation_lat DECIMAL(10, 8),
    geolocation_lng DECIMAL(11, 8),
    geolocation_city VARCHAR(50),
    geolocation_state VARCHAR(2)
);

-- Order Items Table
CREATE TABLE stage_sales.order_items (
    order_id VARCHAR(32),
    order_item_id INTEGER,
    product_id VARCHAR(32),
    seller_id VARCHAR(32),
    shipping_limit_date TIMESTAMP,
    price DECIMAL(10, 2),
    freight_value DECIMAL(10, 2)
);

-- Order Payments Table
CREATE TABLE stage_sales.order_payments (
    order_id VARCHAR(32),
    payment_sequential INTEGER,
    payment_type VARCHAR(50),
    payment_installments INTEGER,
    payment_value DECIMAL(10, 2)
);

-- Order Reviews Table
CREATE TABLE stage_sales.order_reviews (
    review_id VARCHAR(32) PRIMARY KEY,
    order_id VARCHAR(32),
    review_score INTEGER,
    review_comment_title VARCHAR(100),
    review_comment_message TEXT,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP
);

-- Orders Table
CREATE TABLE stage_sales.orders (
    order_id VARCHAR(32) PRIMARY KEY,
    customer_id VARCHAR(32),
    order_status VARCHAR(30),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);

-- Products Table
CREATE TABLE stage_sales.products (
    product_id VARCHAR(32) PRIMARY KEY,
    product_category_name VARCHAR(50),
    product_name_length INTEGER,
    product_description_length INTEGER,
    product_photos_qty INTEGER,
    product_weight_g INTEGER,
    product_length_cm INTEGER,
    product_height_cm INTEGER,
    product_width_cm INTEGER
);

-- Sellers Table
CREATE TABLE stage_sales.sellers (
    seller_id VARCHAR(32) PRIMARY KEY,
    seller_zip_code_prefix VARCHAR(5),
    seller_city VARCHAR(50),
    seller_state VARCHAR(2)
);

-- Product Category Name Translation Table
CREATE TABLE stage_sales.product_category_name_translation (
    product_category_name VARCHAR(50),
    product_category_name_english VARCHAR(50)
);
