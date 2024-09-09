# TDI DATA SCIENCE ASSIGNMENT WEEK 5

## Project Overview:
In this project, you will develop a Python-based system for managing and analyzing employee data without using external libraries like Pandas or NumPy. The focus will be on core Python data structures and object-oriented programming (OOP) principles. This project involves creating classes with private and public attributes, implementing inheritance, and performing dataset operations such as reading from CSV files and slicing data using standard Python techniques.

## Project Objective:
The objective of this project is to build a Python-based employee management system that showcases your proficiency in core Python programming concepts. 
By the end of this project, you should be able to:
i.	Implement and manage classes with private and public attributes.
ii.	Use inheritance to design a class hierarchy.
iii.	Read data from CSV files using Python’s built-in capabilities.
iv.	Perform data slicing and manipulation using standard Python data structures, such as lists and dictionaries.

### Download CSV Employees Data:
When reading the CSV file, please ensure to skip any rows with empty values. You can download the sample CSV file containing employee data from the following link: [Download Employee Data CSV](https://drive.google.com/drive/u/1/folders/1_P4Bi0oMBJyOfXx3z3LBqz-gXZJj_65G)

### Video References:
1.	[Python Classes and Objects – Python Classes and Objects - OOP for Beginners.](https://youtu.be/f0TrMH9s-VE?si=QVWw_pZBfvtfYXVe)

2.	[Understanding Inheritance in Python – OOP Class Inheritance and Private Class Members - Python for Beginners!](https://youtu.be/6c6NYPjO_rI?si=Rr09IV4sOR-Shf3A)

3.	[Reading CSV Files in Python – Python 3 Script to Read & Write CSV Files Using csv Module in Command Line](https://youtu.be/DB8mnz30w4c?si=hswAF0exC764XLbZ)

4.	[Data Slicing and Manipulation in Python – Slicing and Indexing](https://youtu.be/ZOxs7grEjWM?si=UHddqXJwsIIGR7vw)

## Questions:
### 1.	Classes and Inheritance
a.	Define a Python class named Employee with attributes for name, age, and salary (The salary attribute should be private):
i.	Describe the difference between private and public attributes in Python classes. When would you choose to make an attribute private?
ii.	A method to get and set the value of the salary.
iii. A method to display the employee’s details.

b.	Explain how inheritance can be used to create a class hierarchy for different employee types such as Employee, Manager, and Intern. You can provide code examples if necessary.

c.	Create a Python program where the Manager class extends the Employee class. Override the method responsible for displaying employee details to include extra information about the manager's departments and their respective positions.


### 2.	Reading and Slicing Datasets
a.	Write a Python function to read data from a CSV file into a list of dictionaries, where each dictionary represents a row in the file. 
Limit the data read to the first 20 rows.
b.	Given a dataset loaded into a list of dictionaries with keys Name, Age, Salary, and Department, write a Python code snippet to:
•	Slice the dataset to get all employees with a salary above average salary.
•	Extract only the Name and Department fields from each dictionary. The output should be sorted by name in ascending order.

### 3.	Integrating Classes with Dataset Operations
**a.	Create Employee Objects from CSV:**
i.	Write a function using the Employee class that reads employee data from a CSV file. 
For each row in the CSV, create an employee object and store these objects in a list.
**b.	Answer the Following Questions:**
**Filter by Age:**
i.	How many employees are over 30 years old?  
ii.	Which employees are younger than 25 years?  
iii.	List the employees who are between 28 and 35 years old.  
iv.	Who are the employees that are exactly 40 years old?
**Filter by Salary:**
v.	Which employees have a salary higher than ₦1,500,000 per month?  
vi.	Can you find the employees earning less than ₦800,000 per month?  
vii.	List the employees whose salaries are between ₦1,000,000 and ₦2,000,000 per month.  
viii.	Who earns exactly ₦1,200,000 per month?
**Combined Filters:**
ix.	Which employees over 30 years old earn more than ₦1,500,000 per month?  
x.	Can you list the employees who are under 35, earn between ₦1,000,000 and ₦2,000,000 per month, and work in the Sales department?
**Filter by Department and Position:**
xi.	Who are the employees working in the Engineering department?  
xii.	List the employees who hold the title of Manager.  
xiii.	Which employees are Managers in the Finance department?

## SUBMISSION MODE
You are expected to submit your assignment a week after it was given, with this, Submission starts from Friday 7am Nigerian time to Saturday 3pm Nigerian time. 

This submission will be done either on Twitter or LinkedIn, you can choose either of the two to submit your assignment or you can submit on both platforms. You would take a screenshot of your work Answers, you can add a write up if you want.

For twitter Submission, you would tag:
1.	The TDI Official page @TDataInitiative
2.	Annie @ DabereNnamnai
3.	Jacob @Jacob_Ajala
4.	Use the #TDIDataScience

For LinkedIn Submission, you would tag:
1.	TDI page @TheData Initiative
2.	Annie @ Anne Nnamani