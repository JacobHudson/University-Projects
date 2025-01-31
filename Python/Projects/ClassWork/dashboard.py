import streamlit as st

import seaborn as sns

import pandas as pd

import matplotlib.pyplot as plt
 
# Load the tips dataset

tips = sns.load_dataset('tips')
 
# Streamlit app

st.title("Tips Dataset Analysis Dashboard")
 
# Sidebar filters

st.sidebar.header("Filter Options")
 
# Day filter

day = st.sidebar.multiselect("Select Day", options=tips['day'].unique(), default=tips['day'].unique())
 
# Gender filter

sex = st.sidebar.multiselect("Select Gender", options=tips['sex'].unique(), default=tips['sex'].unique())
 
# Time filter

time = st.sidebar.multiselect("Select Time", options=tips['time'].unique(), default=tips['time'].unique())
 
# Filter data based on selections

filtered_data = tips[(tips['day'].isin(day)) & (tips['sex'].isin(sex)) & (tips['time'].isin(time))]
 
# Show filtered data

st.write("Filtered Data", filtered_data)
 
# Create visualizations

st.subheader("Visualizations")
 
# Total bill vs tip

fig1, ax1 = plt.subplots()

sns.scatterplot(data=filtered_data, x='total_bill', y='tip', hue='sex', ax=ax1)

ax1.set_title('Total Bill vs Tip')

st.pyplot(fig1)
 
# Tips distribution

fig2, ax2 = plt.subplots()

sns.histplot(filtered_data['tip'], bins=10, kde=True, ax=ax2)

ax2.set_title('Distribution of Tips')

st.pyplot(fig2)
 
# Average tip by day

avg_tip_by_day = filtered_data.groupby('day')['tip'].mean().reset_index()

fig3, ax3 = plt.subplots()

sns.barplot(data=avg_tip_by_day, x='day', y='tip', ax=ax3)

ax3.set_title('Average Tip by Day')

st.pyplot(fig3)
 
# Display raw data as a table

st.subheader("Raw Data")

st.dataframe(filtered_data)