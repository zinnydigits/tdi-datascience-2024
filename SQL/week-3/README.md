## TDI STRUCTURED QUERY LANGUAGE WEEK 3

Introduction

### Welcome to SQL week 3!

In this assignment, you will delve into the crucial concepts of SQL joins, which are essential for combining data from multiple tables based on related columns. Understanding how to use different types of joins using the primary keys and foreign keys will allows you to extract meaningful information from relational databases effectively. The joins you will explore include:

1. Inner Join: Returns records that have matching values in both tables.

2. Left Join (or Left Outer Join): Returns all records from the left table and the matched records from the right table. Unmatched records from the left table will still be shown with NULL values for columns from the right table.

3. Right Join (or Right Outer Join): Returns all records from the right table and the matched records from the left table. Unmatched records from the right table will still be shown with NULL values for columns from the left table.

4. Full Outer Join: Returns all records when there is a match in either the left or right table. Unmatched records from both tables will be included, with NULL values in place of missing matches.

By understanding and applying these join types, you will be able to perform complex queries that can combine and present data from multiple tables in various ways. This knowledge is fundamental for data analysis, reporting, and building comprehensive database queries.

During this assignment, you will work with a provided dataset. You will use this dataset to practice and demonstrate your ability to perform different types of joins. This will help solidify your understanding and provide practical experience in handling real-world data scenarios.

The questions are designed to guide you through the following practical applications:

1. Inner Join: Identifying records that have common attributes in both tables.

2. Left Join: Ensuring all records from the primary table are included in the result set, with appropriate matches from the secondary table.

3. Right Join: Ensuring all records from the secondary table are included in the result set, with appropriate matches from the primary table.

4. Full Outer Join: Combining all records from both tables, including those without matches in the other table.

By the end of this assignment, you will be proficient in using various join operations in SQL, enabling you to merge data effectively and derive insightful information from relational databases. Let’s get started with the resources the answer the questions to enhance your SQL join capabilities!

### PART A

Resources:
Link 1: https://youtu.be/vncBSUNb4NA?si=rgxEKuCAsWbQIyi-

Link 2: https://youtu.be/KTvYHEntvn8?si=HsOXNotlEa76SGiH

Link 3: https://youtu.be/vncBSUNb4NA?si=lzBw6E5vFvnbcg60

Link 4: https://youtu.be/Yh4CrPHVBdE?si=JG8KNT1Yxu0jvt_W

### PART B

Questions:

#### Inner Join:
1. List the titles of books along with their authors.

2. Show the titles and prices of all fantasy books.

3. Display the authors who have written books and the titles of their books.

4. Find the titles and genres of books priced less than $15.

#### Outer Join:
1. List all books and their authors. If a book doesn't have an author, display "Unknown".

2. Show the titles and prices of all books. If a book doesn't have a price, display "Price not available".

3. Display all authors and the titles of their books. If an author hasn't written any books, display "No books written".

4. List all books and their genres. If a book doesn't have a genre, display "Genre not specified".

#### Right Join:
1. Show all products along with the order details. Include products that haven't been ordered.

2. Display the names of customers and the total amount spent on orders. Include customers who haven't placed any orders.

3. List all orders and their associated products. Include orders without products.

4. Show the product names and quantities ordered. Include product without orders.

#### Left Join:
5. Show all customers along with their orders. Include customers who haven't placed any orders.

6. Display the names of customers and the total amount spent on orders. Include customers who haven't placed any orders, showing "0" as the total amount for them.

7. List all orders and their associated products. Include orders without products.

8. Show the product names and quantities ordered. Include products without orders, displaying "0" as the quantity for them.

#### Full Outer Join:
9. List all orders along with the names of the customers who made them. Include orders without customers and customers without orders.

10. Show all products along with the order details. Include products that haven't been ordered and order details without products.

11. Display the names of customers and the total amount spent on orders. Include customers who haven't placed any orders and the total amount spent for orders without customers.

12. List all orders and their associated products. Include orders without products and products without orders.

### PART C
SUBMISSION MODE
You are expected to submit your assignment a week after it was given, with
this, Submission starts from Friday by 7am Nigerian time to Saturday by
3pm Nigerian time.
This submission will be done either on Twitter or LinkedIn, you can choose
either of the two to submit your assignment or you can submit on both
platforms. You would take a screenshot of your work Answers, you can add
a write up if you want.

For twitter Submission, you would tag:
1. The TDI Official page @TDataImmersed
2. Annie @ DabereNnamani
3. Ade @JacobAjala
4. Tag @SQLServer
5. Use the #TDI

For LinkedIn Submission, you would tag:
1. TDI page @TheData Immersed
2. Annie @ Anne Nnamani


#### PART D
CORRECTION CLASS

Correction Classes, holds every Saturday, 4pm-6pm Nigerian time.

Venue: The TDI official Discord page or a google meet link will be sent.