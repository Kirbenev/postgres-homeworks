"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv, psycopg2

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='256987')

with open('north_data/customers_data.csv') as f:
    items = csv.DictReader(f)
    cur = conn.cursor()
    for item in items:
        cur.execute("INSERT INTO customers_data VALUES (%s, %s, %s)", (item['customer_id'],
                                                                     item['company_name'],
                                                                     item['contact_name']))
    conn.commit()
    cur.close()


with open('north_data/employees_data.csv') as f:
    items = csv.DictReader(f)
    cur = conn.cursor()
    employee_id = 1
    for item in items:
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (
            employee_id,
            item['first_name'],
            item['last_name'],
            item['title'],
            item['birth_date'],
            item['notes']
        ))

        employee_id = employee_id + 1

    conn.commit()
    cur.close()

with open('north_data/orders_data.csv') as f:
    items = csv.DictReader(f)
    cur = conn.cursor()
    for item in items:
        cur.execute("INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)", (
            (item['order_id']),
            item['customer_id'],
            item['employee_id'],
            item['order_date'],
            item['ship_city']
        ))

    conn.commit()
    cur.close()

conn.close()
