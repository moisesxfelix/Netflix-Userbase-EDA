import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Netflix_Userbase.csv")
plt.style.use("seaborn-v0_8-darkgrid")

#Get familiar with data
df.head()
df.info()
df.describe()

#Check duplicates
df.duplicated().value_counts()

#Check missing values
df.isna().sum()
df[df.isna().any(axis = 1)]
df["Plan Duration"] = df["Plan Duration"].fillna("1 Month")
df.loc[df["Plan Duration"] == "1 Month", "Plan Duration"] = 1
df.isna().sum()

#Convert/reformat data types
df["Last Payment Date"] = pd.to_datetime(df["Last Payment Date"], format = "mixed", dayfirst = True)
df[["Join Date", "Last Payment Date"]]
#Create new column
df["Subscription Duration (Days)"] = df["Last Payment Date"] - df["Join Date"]
df = df.rename(columns={"Plan Duration": "Subcription Plan (Month)"})

#Unify country format
df["Country"].unique()
data_dict = {
    "USA" : "United States",
    "mexico" : "Mexico",
    "canada" : "Canada",
    "UK" : "United Kingdom",
    "italy" : "Italy",
    "US" : "United States",
    "AUS" : "Australia",
    "MX" : "Mexico",
    "spain" : "Spain",
    "france" : "France",
    "brazil" : "Brazil"
}
df["Country"] = df["Country"].replace(data_dict)
df["Country"].unique()

#Double check data
df.info()

#Consider age range, gain possible insights
df["Age"].describe()
df["Age"].plot(kind = "hist", width = 2)
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Participants by Age")
plt.tight_layout()
plt.show()

#Analysis of Country and possible associations
df["Country"].value_counts(ascending = True).plot(kind="barh")
plt.grid(axis = 'y')
plt.xlabel("Subscriptions")
plt.ylabel("Country")
plt.title("Subscriptions per Country")
plt.tight_layout()
plt.show()

df_Country_mRevenue = df[["Country", "Monthly Revenue"]]
df_avgByCountry = df_Country_mRevenue.groupby("Country")["Monthly Revenue"].mean().round(2).sort_values(ascending= True)
ax = df_avgByCountry.plot(kind = 'barh')
ax.set_xlim(10, 15)
plt.xlabel("Average Monthly Revenue")
plt.ylabel("Country")
plt.title("Average Monthly Spend per Individual by Country")
plt.tight_layout()
plt.show()

df["Country"].value_counts()
df_avgByCountry
df_avgByCountry.median()

#Analysis of Subscription types and possible associations
df_Sub_Type_Count = df["Subscription Type"].value_counts()
slice_labels= df_Sub_Type_Count.index.to_numpy()
plt.pie(df_Sub_Type_Count, wedgeprops= {'edgecolor': 'k'}, shadow = True, 
        labels = slice_labels, autopct= '%1.1f%%')
plt.title("Subscription Type Popularity")
plt.tight_layout()
plt.show()

df_Sub_Type_Length = df.groupby("Subscription Type")["Subscription Duration (Days)"].mean().dt.days.sort_values(ascending= True)
ax = df_Sub_Type_Length.plot(kind = "barh")
ax.set_xlim(275,325)
plt.xlabel("Days")
plt.ylabel("Subscription Type")
plt.title("Average Subscription Lifetime by Subscription Type")
plt.tight_layout()
plt.show()

df_Sub_Type_Length