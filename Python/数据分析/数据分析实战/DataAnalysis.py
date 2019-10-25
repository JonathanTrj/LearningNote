#coding='utf-8'

import pandas as pd
import numpy as np

def cut_word(word, method):
	position = word.find("-")
	length = len(word)
	if position != -1:
		bottomsalary = word[:position-1]
		topsalary = word[position+1:length-1]
	else:
		bottomsalary = word[:word.upper().find("K")]
		topsalary = bottomsalary
	if method == "top":
		return topsalary
	else:
		return bottomsalary
	# return pd.Series([bottomsalary, topsalary])

df = pd.read_csv("data.csv", encoding= 'gb2312')

df_duplicates = df.drop_duplicates(subset="positionId", keep="first")

df_duplicates["bottomSalary"] = df_duplicates.salary.apply(cut_word, method = "bottom")
df_duplicates["topSalaru"] = df_duplicates.salary.apply(cut_word, method = "top")

df_duplicates.bottomSalary = df_duplicates.bottomSalary.astype("int")
df_duplicates.topSalaru = df_duplicates.topSalaru.astype("int")
df_duplicates["avgSalary"] = df_duplicates.apply(lambda x: (x.bottomSalary+x.topSalaru)/2, axis=1)

df_clean = df_duplicates[['city','companyShortName','companySize','education','positionName','positionLables','workYear','avgSalary']]

df_clean_city = df_clean.city.value_counts()

print(df_clean.describe())

import matplotlib.pyplot as plt

# %matplotlib inline
plt.style.use('ggplot')

ax = df_clean.groupby('city').mean().plot.bar()