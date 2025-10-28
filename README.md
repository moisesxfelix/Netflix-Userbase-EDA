# Netflix Userbase - Exploratory Data Analysis
Dataset: ```Netflix_Userbase.csv```
 
**Guiding Questions:**
1) What country contains the most Netflix subscribers?
2) What is the average monthly spend per individual, by country?
3) What is the most popular Netflix subscription plan amongst users?
4) What Netflix subscription plan has the longest lifespan amongst users?

## Key Insights

From our Exploratory Data Analysis we can extract these key insights:
- Spain and the United States have the most user subscriptions, 2.6 times larger than the country with the least user subscriptions. However, the United Kingdom has the highest average monthly spend per individual, 0.01% ahead of Italy.
- Of the three Subscription Types, the Basic plan is the most popular amongst users, 36.5% more popular than the Premium plan. However, users subscribe to the Standard plan for a longer period of time (1.01% longer), suggesting better retention.

## Overview
Using this data set we examined questions that could provide insight for business decisions, such as international affairs and product popularity.
We analyze the Netflix Userbase dataset over a year of user activity, focusing on a monthly subscriber plan, limited to active users across 10 countries.
The analysis is descriptive, summarizing mean/median monthly spend per individual, participating countries, plan popularity, and retention with basic cleaning.
Key assumption and limitations re documented.

## Notebook Guide
To begin we started by importing the ```Netflix_Userbase.csv``` and made our initial examination of the data to understand the structure and characteristics of the dataset.

We then began the process of cleaning the data set by:
- Checking for duplicates
- Checking for missing Values
- Replacing missing values with logical data
- Converted messy dates to a uniform format and datetime data type
- Replaced variations of different countries for uniformity

We created a new cloumn to extract additional insight from already existing columns like "Join Date" and "Last Payment Date."

We then begin our analysis by looking at the age range of our dataset
- We conclude minimum age (26), maximum age (51), and average age (38.8)

We take a look at participating countries and identify that:
- Spain and the United States have the most subscribers according to our dataset.
- The United Kingdom leads the was for highest average monthly spend per individual, followed closely by Italy (0.01% behind).

Having examined subsciption types we concluded that:
- The basic subsciption was the most popular, 36.5% more than the least popular plan.
- The standard plan had the longest average lifetime (311 days), ahead of the Premium and Basic plans by 4 days.

## Limitations Observed
**Data Coverage:**
- The countries with the highest users were more than twice as large of a sample size than the countries with the lowest amount of users indicating an imbalance of sample size.
- The time window of our data only encompasses a small time period of the lifespan of Netflix.

**Temporal Effects:**
- Data set only covers a static point in time. Does not consider price changes, subsciption adjustments, promotional periods.

**No Causality**
- Findings do not establish that plan type causes higher revenue or longer retention.
