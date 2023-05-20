-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(50) NOT NULL,
	birh_date date NOT NULL,
	notes text
);

CREATE TABLE customers_data
(
	customer_id varchar(50) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(50) REFERENCES customers_data(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(50) NOT NULL
);

