# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
plt.hist(data['Rating'].dropna())
plt.show()
data = data[data['Rating']<=5]
plt.hist(data['Rating'])
plt.show()
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = total_null/data.isnull().count()
missing_data = pd.concat([total_null, percent_null], keys=['Total','Percent'], axis=1)
print(missing_data)
data.dropna(inplace=True)
total_null_1 = data.isnull().sum()
percent_null_1 = data.isnull().sum()/data.isnull().count()
missing_data_1 = pd.concat([total_null_1, percent_null_1], keys=['Total','Percent'], axis=1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here
import seaborn as sns

sc = sns.catplot(x='Category', y='Rating', data=data, kind='box', height=10)
sc.set_xticklabels(rotation=90)
sc.set_titles('Rating vs Category [Boxplot]')
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())
data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].str.replace('+','').astype(float)
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
sr = sns.regplot(x='Installs', y='Rating', data=data)
sr.set_title('Rating vs Istalls [Regplot]')
#Code ends here



# --------------
#Code starts here
data['Price'].value_counts()
data['Price'] = data['Price'].str.replace('$','').astype(float)
sr = sns.regplot(x='Price', y='Rating', data=data)
sr.set_title('Rating vs Price [Regplot]')

#Code ends here


# --------------

#Code starts here
data['Genres'].unique()
data['Genres'] = data['Genres'].str.split(';', expand=True)[0]
gr_mean = data.loc[:,['Genres','Rating']].groupby(['Genres'], as_index=False).mean()
gr_mean.describe()
gr_mean = gr_mean.sort_values(by=['Rating'])
print(gr_mean.head(1))
print(gr_mean.tail(1))
#Code ends here


# --------------

#Code starts here
print(data['Last Updated'])
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
sr = sns.regplot(x='Last Updated Days', y='Rating', data=data)
sr.set_title('Rating vs Last Updated [Regplot]')
#Code ends here


