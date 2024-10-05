### Global Wine Quality – Data Cleaning
Wine is one of the most in-demand products globally, with certain countries dominating the market. In this assignment, you will perform data cleaning and text analysis tasks to prepare the dataset for further exploration and insights.
Download data  from: [Kaggle.com- global wine quality](https://www.kaggle.com/datasets/priyamchoksi/global-wine-ratings-dataset/data)
#### References:
1.	 Text processing: https://www.youtube.com/watch?v=hhjn4HVEdy0

2.	 Natural Language Processing: https://www.youtube.com/watch?v=iQ1bfDMCv_c

3.	Pandas conditional columns: https://www.youtube.com/watch?v=lnks1IcoHUo&t=275s

### Section A: Data Cleaning

1.	 Identify and remove any duplicate rows and missing values from the global wine quality dataset. Store the cleaned dataset in a new dataframe named non_dm_data.
 
2.	The "Region" column contains both country and city names. Since you need to analyze wine quality by country, ensure that only country names are listed. Replace any cities without a corresponding country name with the relevant country.

3.	Create a table showing the percentage distribution of wine varieties, rounded to one decimal place.

4.	Based on wine ratings, classify the wines into the following categories:
- 'Good' for ratings between 85-89
- 'Outstanding' for ratings between 90-94
- 'Exceptional' for ratings between 95-100
Create a new column named "wine_quality" to store these categories.

### Section B: Text Preprocessing
Scenario: You are a data scientist working with text data containing noise, making it difficult to analyze. The "notes" column in your dataset has inconsistencies such as mixed cases, punctuation, numbers, and irrelevant words. Using your NLP expertise, you need to clean and preprocess the text.
**Tasks:**
1.	Convert all text to lowercase for uniformity.
2.	Remove numbers that do not contribute to meaningful analysis.
3.	Eliminate punctuation marks to simplify the text.
4.	Lemmatize the text using POS tagging to reduce words to their root forms while preserving context.
5.	Remove stopwords (e.g., "the", "and") to focus on relevant terms.
Create a new column  "description_token"  to store the cleaned text as tokens.

### Section C: Analysis
Use the cleaned data from section A and B to answer the following questions.
1.	Identify the top 5 words most strongly associated with wine quality (good, outstanding and exceptional). For each wine quality group, display top 5 words.

2.	Display the top 5 regions producing the highest number of Exceptional quality wines.

3.	Identify and display the regions with the highest diversity of wine varieties.

### Submission Mode
You are expected to submit your assignment a week after it was given, with this, Submission starts from Friday 7am Nigerian time to Saturday 3pm Nigerian time. 
This submission will be done either on Twitter or LinkedIn, you can choose either of the two to submit your assignment or you can submit on both platforms. You would take a screenshot of your work Answers, you can add a write up if you want.

(1)	Primary submission: GitHub – This time your git submission will be on branches; each one of you will be assigned a branch with their names. Feel free to ask for clarification

(2)	For twitter Submission, you would tag:
- a)	The TDI Official page @TDataInitiative
- b)	Annie @ DabereNnamnai
- c)	Jacob @Jacob_Ajala
- d)	Use the #TDIDataScience

(3)	For LinkedIn Submission, you would tag:
- a)	TDI page @TheData Initiative
- b)	Annie @ Anne Nnamani
