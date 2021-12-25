import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data = pd.read_csv("newdata11.csv")
data = data.drop(["Unnamed: 0"],axis = 1)

frequent_itemset = apriori(data, min_support=0.01, use_colnames=True)
association_rule = association_rules(frequent_itemset,metric="lift",min_threshold=1)

x = association_rule
x = x[x["lift"]>=1.5]

def recommendation(item_check):
    count = 0
    recommend_item = []
    for i in list(x["antecedents"]):
        for j in list(i):
            if(j == item_check):
                if x.iloc[count][1] not in recommend_item:
                    recommend_item.append(set(x.iloc[count][1]))
        count = count + 1
    return recommend_item

print(recommendation("whole milk"))