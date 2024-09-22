# DS - New York City Airbnb Open Data - Data Cleaning
The New York City Airbnb Open Data is a rich source of information for exploring the city's Airbnb market.<br> 
The dataset contains detailed information on Airbnb listings in the city, including their locations, prices, availability, and various other attributes. <br>

The goal of this capstone project is to help you develop your skills in data cleaning and preparation by working with real-world data using Python. <br>
You will use Pandas, a popular Python library for data manipulation and analysis, to read the data from a CSV file, handle missing values, deal with duplicates, and clean and transform the data to answer various questions about the Airbnb market in New York City. <br>

In this capstone project, you will complete a series of activities that cover different aspects of data cleaning and preparation using Pandas. <br> By the end of this project, you will have gained practical skills in data manipulation, cleaning, and preparation using Pandas, and be ready to tackle more complex data analysis tasks.

**Download Dataset**: [New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)

### References:

a)	**Data cleaning in pandas**: https://youtu.be/bDhvCp3_lYw?si=sNmd1xLWw6UlaX9e

b)	**Data cleaning project in pandas**: https://youtu.be/7mYbrpfAU6k?si=87dw1n2QIamExntW

c)	**Outliers**: https://youtu.be/rzR_cKnkD18?si=hshDjaV4u7wkBSMn

d)	**Remove outliers**: https://youtu.be/Vc4cXIAa69Y?si=4gAtFAoWzSaN9ZqN

### ACTIVITIES FOR DATA CLEANING CAPSTONE
 
1.	**Find out the missing values in each column.** <br>
Perform the calculation and store the results in the variable col_missing_values.

2.	**Drop the column reviews_per_month as it has many values missing, and we will not use it.** <br>
You have to drop this column permanently as we cannot use it for any purpose.

3.	**Drop the rows having more than 1 missing values.** <br>
Store the resulting DataFrame in the variable df_rows_dropped.

4.	**Fill the 21 missing values in host_name with the value Airbnb.** <br>
Store your result in the variable host_total.

5.	**Check if any name in the Column host_name has digit(s) or number(s) in it.** <br>
Select correct answer below.
a)	This Column has 6 digits. 
b)	This Column has 0 digits. 
c)	This Column has 44,929 alphabet values.
d)	This Column values with spaces.

6.	**Fill the 21 missing values of the column price with the mean of the column.** <br>
Store your result in the variable mean_df_price.

7.	**Fill all missing values in last_review using the forward filling method.** <br>
Store your result in the variable ffill_review.

8.	**Select duplicate hosts in a dataframe based on name, host_id, and price columns.** <br>
Perform the selection and store the results in the variable duplicate_hosts.

9.	**Which option to set for the keep parameter when dropping all duplicates is needed?** <br>
Select correct options – can be multiple: <br>
a)	First <br>
b)	True <br>
c)	False <br>
d)	Last <br>

10.	**Drop duplicates while keeping the first non-NaN value based on name, host_id, and price columns.** <br>
Perform the dropping and store the results in the variable df_unique_hosts.

11.	**How many users in the Column room_type are Private room?** <br>
Count all the Private rooms in the column room_type and sum them up. <br>
Store your sum in the private_rooms_counts variable.

12.	**Find the words in the Column name that contain the substring 'park'.** <br>
Store your selection in the variable names_having_park.

13.	**Replace the neighbourhood having 'Kitchen' with 'Restaurant'.** <br>
Store the output in the variable kitchen_to_restaurant.

14.	**Split the strings in the room_type column at (space) to find whether it is room or home/apt.** <br>
Store the output in the variable roomOrhome. <br>
Note: We are interested in the value at the second index once you split all the strings in the Column room_type on space.

15.	**Clean the column availability_365 by removing invalid values.** <br>
Invalid values are defined as any host that offers a value of 0 in availability_365. <br>
Store the results in the variable df_invalid_availability.

16.	**What is/are the most common value(s) to be set in case we want to fill NaN values?** <br>
Select correct answer: <br>
a)	Median <br>
b)	IQR <br>
c)	Standard Deviation <br>
d)	Mean <br>

17.	**Identify outliers in the minimum_nights column.** <br>
Outliers are defined as any values 43 or more std to the left or right of the mean. <br>
Store the results in a new column df_nights['Min_Nights_cleaned']. <br>
Use df_nights as a copy of the original dataframe df.

18.	**Identify outliers in the price column.** <br>
Outliers are defined as any values that are 1.5 * IQR to the left or right. <br>
Store the results in a new column df_Price['Price_cleaned'].

### SUBMISSION MODE
You are expected to submit your assignment a week after it was given, with this, Submission starts from Friday 7am Nigerian time to Saturday 3pm Nigerian time. <br>
This submission will be done either on Twitter or LinkedIn, you can choose either of the two to submit your assignment or you can submit on both platforms. You would take a screenshot of your work Answers, you can add a write up if you want.

(1)	**Primary submission**: 

GitHub – If you would need assistance configuring git, please post on the DS group; <br>
Thus a session will be conducted for demonstration.

(2)	**For twitter Submission, you would tag:**
- The TDI Official page @TDataInitiative
- Annie @ DabereNnamnai
- Jacob @Jacob_Ajala
- Use the #TDIDataScience

(3)	**For LinkedIn Submission, you would tag:**
- TDI page @TheData Initiative
- Annie @ Anne Nnamani