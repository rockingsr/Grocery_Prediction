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

import streamlit as st

from datetime import date

import time

today = date.today()

today = today.strftime("%d/%m/%Y")

st.sidebar.write("DATE:-", today)

add_selectbox = st.sidebar.selectbox('Select Project Running Environment', ["Home", 'Real Time Recommendation'])


def load_homepage() -> None:
    st.header('WELCOME TO MY PROJECT GROCERY RECOMMENDATION SYSTEM')

    st.write("-----------BY SRAJAN--------------")

    st.image('rec_sys.png', use_column_width=True)

    st.header("🎲 DASHBOARD FOR GROCERY RECOMMENDATION SYSTEM")

    st.write("Sentiment Analysis is the process of extracting the opinion or emotion from text data.   "

             "So Sometimes its called opinion mining or emotion AI. "

             "Moreover, it felt like a nice opportunity to see how much information can be "

             "extracted from relatively simple data.")


def recommend():
    st.sidebar.subheader("GROCERY RECOMMENDATION SYSTEM")

    st.header('WELCOME TO MY PROJECT GROCERY RECOMMENDATION SYSTEM')

    st.write("-----------BY SRAJAN--------------")

    st.header("Prediction section")

    for i in range(3):
        st.write(" ")

    st.subheader("Good to See You Here")

    user_input = st.text_input("Search Product")


    recomend_item = recommendation(user_input)

    if (st.button('Check_out')):
        for i in recomend_item:
            st.write(i)

if add_selectbox == 'Home':
    load_homepage()

if add_selectbox == 'Real Time Recommendation':
    recommend()