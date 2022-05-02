import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
# çıktının tek bir satırda olmasını sağlar.
pd.set_option('display.expand_frame_repr', False)
from mlxtend.frequent_patterns import apriori, association_rules

#Preparing the Data

df_ = pd.read_csv("databases/armut_data.csv")

df = df_.copy()
df.head()
df.describe().T
df.isnull().sum()
df.shape

#ServiceID represents a different service for each CategoryID.
#ServiceID and CategoryID are combined with "_" to create a new variable to represent the services.
df["Hizmet"]=df["ServiceId"].astype(str)+"_"+df["CategoryId"].astype(str)

# The data set consists of the date and time of the receipt of services, there is no basket definition (invoice, etc.).
# In order to apply Association Rule Learning, a basket (invoice, etc.) definition must be created.
# Here, the definition of basket is the services that each customer receives monthly.
# For example, a customer with id 25446 received a basket of 4_5, 48_5, 6_7, 47_7 services received in the 8th month of 2017; In the 9th month of 2017
# 17_5, 14_7 services it receives represent another basket.
# Baskets must be identified with a unique ID. First of all, a new date variable containing only the year and month is created.
# By combining UserID and newly created date variable with "_" on user basis, it is assigned to a new variable named ID

df['CreateDate'] = pd.to_datetime(df['CreateDate'])


type(df["CreateDate"][0])

df["year"]=df['CreateDate'].dt.year
df["month"]=df['CreateDate'].dt.month
df["SepetID"]=df["UserId"].astype(str)+"_"+df["year"].astype(str)+"-"+df["month"].astype(str)



#The basket service pivot table has been created as follows.

# Hizmet         0_8  10_9  11_11  12_7  13_11  14_7  15_1  16_8  17_5  18_4..
# SepetID
# 0_2017-08        0     0      0     0      0     0     0     0     0     0..
# 0_2017-09        0     0      0     0      0     0     0     0     0     0..
# 0_2018-01        0     0      0     0      0     0     0     0     0     0..
# 0_2018-04        0     0      0     0      0     1     0     0     0     0..
# 10000_2017-08    0     0      0     0      0     0     0     0     0     0..

table=df.groupby(["SepetID", "Hizmet"])["Hizmet"].count().unstack().fillna(0).  applymap(lambda x: 1 if x > 0 else 0)


#Association rules were created.


frequent_itemsets = apriori(table,
                            min_support=0.01,
                            use_colnames=True)

frequent_itemsets.sort_values("support", ascending=False)

rules = association_rules(frequent_itemsets,
                          metric="support",
                          min_threshold=0.01)
today_date = df["CreateDate"].max()

df.head()



#A service recommendation was made to a user who received the 2_0 service in the last 1 month using the arl_recommender function.

for i, product in enumerate(rules["antecedents"]):
    print(i)
    print(product)
    for j in list(product):
        print(j)

for i, product in rules["antecedents"].items():
    print(i)
    print(product)
    for j in list(product):
        print(j)


def arl_recommender(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)
    recommendation_list = []
    for i, product in sorted_rules["antecedents"].items():
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"]))
    recommendation_list = list({item for item_list in recommendation_list for item in item_list})
    return recommendation_list[:rec_count]


arl_recommender(rules, "2_0", 2)


