```sql
DROP TABLE IF EXISTS customers;

CREATE TABLE customers(
	CustomerID INT PRIMARY KEY,
	Name VARCHAR(100),
	Email VARCHAR(100),
	Phone VARCHAR(100)
);
-- import customers.csv file

SELECT *
FROM customers;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/customers.PNG)
```sql
DROP TABLE IF EXISTS authors;
CREATE TABLE authors(
	AuthorID INT PRIMARY KEY,
	AuthorName VARCHAR(100)
);

-- import author.csv file
SELECT *
FROM authors;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/authors.PNG)
```sql
DROP TABLE IF EXISTS books;
CREATE TABLE books(
	BookID INT PRIMARY KEY,	
	Title VARCHAR(100),
	AuthorID INT,
	Genre VARCHAR(100),
	Price NUMERIC
);
-- import books.csv

SELECT *
FROM books;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/books.PNG)
```sql
DROP TABLE IF EXISTS products;
CREATE TABLE products(
	ProductID	INT PRIMARY KEY,
	ProductName	VARCHAR(100),
	Price NUMERIC
);

-- import products.csv

SELECT *
FROM products;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/products.PNG)
```sql
DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
	OrderID	INT,
	CustomerID	INT,
	OrderDate DATE,
	TotalAmount NUMERIC
);

-- import orders.csv
SELECT *
FROM orders;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/orders.PNG)
```sql
DROP TABLE IF EXISTS order_details;
CREATE TABLE order_details(
	OrderID	INT,
	ProductID	INT,
	Quantity INT
);

-- import order_details.csv
SELECT *
FROM order_details;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/order_details.PNG)

## SQL QUERIES

### Inner Join:
```sql
-- 1. List the titles of books along with their authors.
SELECT 
	AuthorName, 
	Title
FROM books
INNER JOIN authors
USING(AuthorID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/inner-join-1.PNG)

```sql
-- 2. Show the titles and prices of all fantasy books
SELECT 
	Title, 
	Price
FROM books
WHERE Genre = 'Fantasy';
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/inner-join-2.PNG)

```sql
-- 3. Display the authors who have written books and the titles of their books.
SELECT 
	AuthorName, 
	Title
FROM authors
INNER JOIN books
USING(AuthorID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/inner-join-3.PNG)
	
```sql
-- 4. Find the titles and genres of books priced less than $15.
SELECT 
	title, 
	genre
FROM books
WHERE price < 15;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/inner-join-4.PNG)

### Outer Join:
```sql
-- 1. List all books and their authors. If a book doesn't have an author, display "Unknown".
SELECT 
	b.Title, 
	COALESCE(a.AuthorName, 'Not Found') AS AuthorName
FROM books b
JOIN authors a
USING(AuthorID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/outer-join-1.PNG)
```sql
-- 2. Show the titles and prices of all books. If a book doesn't have a price, display "Price not available".

SELECT 
	Title, 
	COALESCE(CAST(Price AS VARCHAR), 'Price not available') AS price 
FROM books;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/outer-join-2.PNG)	
```sql
-- 3. Display all authors and the titles of their books. If an author hasn't written any books, display "No books written".
SELECT 
	a.AuthorName,
	COALESCE(b.Title, 'No books written') AS book_title
FROM authors a
LEFT JOIN books b
USING(AuthorID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/outer-join-3.PNG)
```sql
-- 4. List all books and their genres. If a book doesn't have a genre, display "Genre not specified".
SELECT 
	title,
	COALESCE(Genre, 'Genre Not Specified') AS genre
FROM books;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/outer-join-4.PNG)

### Right Join:
```sql
-- 1. Show all products along with the order details. Include products that haven't been ordered.
SELECT 
	ProductID,
	ProductName,
	OrderID,
	Quantity,
	Price
FROM order_details
RIGHT JOIN products
USING(ProductID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/right-join-1.PNG)	
```sql
-- 2. Display the names of customers and the total amount spent on orders. Include customers who haven't placed any orders.
SELECT 
	Name,
	SUM(TotalAmount) AS amount_spent
FROM orders
RIGHT JOIN customers
USING(CustomerID)
GROUP BY CustomerID;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/right-join-2.PNG)
```sql
-- 3. List all orders and their associated products. Include orders without products.
SELECT 
	OrderID,
	ProductName,
	Quantity
FROM products
RIGHT JOIN order_details
USING(ProductID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/right-join-3.PNG)
```sql
-- 4. Show the product names and quantities ordered. Include products without orders.
SELECT 
	p.ProductName,
	SUM(od.Quantity) AS total_quantity
FROM order_details od
RIGHT JOIN products p
USING(ProductID)
GROUP BY p.ProductName
ORDER BY SUM(od.Quantity) DESC;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/right-join-4.PNG)

### Left Join:
```sql

-- 5. Show all customers along with their orders. Include customers who haven't placed any orders.
SELECT 
	CustomerID,
	Name,
	COUNT(DISTINCT OrderID) AS total_orders
FROM customers c
LEFT JOIN orders
USING(CustomerID)
GROUP BY CustomerID;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/left-join-5.PNG)
```sql
-- 6. Display the names of customers and the total amount spent on orders. Include customers who haven't placed any orders, showing "0" as the total amount for them.
SELECT 
	CustomerID,
	Name,
	COALESCE(SUM(TotalAmount), 0) AS total_amount  
FROM customers c
LEFT JOIN orders
USING(CustomerID)
GROUP BY CustomerID
ORDER BY total_amount DESC;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/left-join-6.PNG)
```sql
-- 7. List all orders and their associated products. Include orders without products.
SELECT 
	orderID,
	ProductName,
	Quantity
FROM order_details
LEFT JOIN products
USING(ProductID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/left-join-7.PNG)
```sql
-- 8. Show the product names and quantities ordered. Include products without orders, displaying "0" as the quantity for them.
SELECT 
	ProductID,
	ProductName,
	COALESCE(SUM(Quantity), 0) AS total_quantity 
FROM products
LEFT JOIN order_details
USING(ProductID)
GROUP BY ProductID
ORDER BY total_quantity DESC;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/left-join-8.PNG)
### Full Outer Join:
```sql
-- 9. List all orders along with the names of the customers who made them. Include orders without customers and customers without orders.
SELECT 
	OrderDate,
	Name,
	SUM(TotalAmount) AS total_amount
FROM customers
FULL OUTER JOIN orders
USING(CustomerID)
GROUP BY OrderDate, Name
ORDER BY total_amount DESC;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/full-outer-9.PNG)
```sql
-- 10. Show all products along with the order details. Include products that haven't been ordered and order details without products.
SELECT 
	productName,
	price,
	quantity
FROM products
FULL OUTER JOIN order_details
USING(productID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/full-outer-10.PNG)	
```sql
-- 11. Display the names of customers and the total amount spent on orders.  Include customers who haven't placed any orders and the total amount spent for orders without customers.
SELECT 
	OrderDate,
	Name,
	SUM(totalAmount) AS total_amount
FROM customers
FULL OUTER JOIN orders
USING(customerID)
GROUP BY Name, OrderDate;
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/full-outer-11.PNG)	
```sql
-- 12. List all orders and their associated products. Include orders without products and products without orders.
SELECT *
FROM order_details
FULL OUTER JOIN products
USING(ProductID);
```
![Query Execution Screenshot](https://github.com/zinnydigits/tdi-datascience-2024/blob/main/SQL/week-3/output/full-outer-12.PNG)
