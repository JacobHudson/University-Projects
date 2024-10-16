import streamlit as st

import pandas as pd

import plotly.express as px

from io import BytesIO

import matplotlib.pyplot as plt
 
# Custom CSS for royalty

def apply_custom_css():

    st.markdown("""
<style>

    body { background-color: #F5E8C7; }

    .stTitle { color: #4B0082; font-family: 'Serif'; text-align: center; }

    .stButton > button { background-color: #4B0082; color: white; border-radius: 10px; font-family: 'Georgia'; }

    .stTextInput > div > label { color: #4B0082; font-family: 'Georgia'; }

    .stDownloadButton > button { margin: 0 auto; display: block; background-color: #4B0082; color: white; border-radius: 10px; font-family: 'Georgia'; }

    .stSubheader { color: #B8860B; font-family: 'Georgia'; }

    .streamlit-expanderHeader { font-weight: bold; }
</style>

    """, unsafe_allow_html=True)
 
 
# Set page configuration

st.set_page_config(page_title="📊 Royal Data Kingdom", layout="wide")


apply_custom_css()
 
# Title and description

st.title("👑 Welcome to the Royal Data Kingdom 👑")

st.markdown("""

Your Majesty, you have entered the realm of data! Explore splendid visualizations, gain regal insights, and watch your data unfold.

""")
 
# File uploader

uploaded_file = st.file_uploader("Please select thy royal CSV file", type=["csv"])
 
# Clean the dataset

def clean_data(df):

    df_cleaned = df.dropna()

    if 'Date' in df_cleaned.columns:

        df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], errors='coerce')

    df_cleaned = df_cleaned.drop_duplicates()

    return df_cleaned
 
# Data summary for numeric columns

def royal_summary(df):

    st.subheader("📜 Royal Summary of Thy Dataset")

    st.write(df.describe())
 
# Time Series Visualizations for Date columns

def royal_time_series(df, date_col, y_col):

    fig = px.line(df, x=date_col, y=y_col, title=f"Majestic Time Series: {y_col} Over Time")

    st.plotly_chart(fig)
 
# AI-driven insights: Highlight interesting trends or anomalies

def royal_insights(df):

    st.subheader("🔮 Royal Insights")

    st.write("Your Majesty, based on your grand data, here are some notable insights:")

    if 'Total' in df.columns:

        highest_total = df['Total'].max()

        st.markdown(f"👑 The highest recorded sale is **{highest_total}**, a fortune indeed!")

    if 'Rating' in df.columns:

        avg_rating = df['Rating'].mean()

        st.markdown(f"⭐ The average customer rating is **{avg_rating:.2f}** — how your subjects adore your products!")
 
# Data preview and filtering with search functionality

def search_and_filter(df):

    st.subheader("👑 Search and Filter Your Royal Data")

    search_query = st.text_input("Search within your royal data:")
 
    if search_query:

        df_filtered = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]

        st.dataframe(df_filtered.head(10))

    else:

        st.dataframe(df.head(10))
 
    return df_filtered if search_query else df
 
# Visualization settings and charts

def visualize_data(df):

    st.sidebar.header("🎨 Royal Visualization Settings")

    plot_type = st.sidebar.selectbox("Select thy majestic plot type", ("Bar Chart", "Line Graph", "Scatter Plot", "Distribution Plot", "Time Series"))
 
    if plot_type == "Bar Chart":

        x_axis = st.sidebar.selectbox("X-axis", df.columns)

        y_axis = st.sidebar.selectbox("Y-axis", df.columns)

        fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart of {y_axis} by {x_axis}")

        st.plotly_chart(fig)
 
    elif plot_type == "Line Graph":

        x_axis = st.sidebar.selectbox("X-axis", df.columns)

        y_axis = st.sidebar.selectbox("Y-axis", df.columns)

        fig = px.line(df, x=x_axis, y=y_axis, title=f"Line Graph of {y_axis} over {x_axis}")

        st.plotly_chart(fig)
 
    elif plot_type == "Scatter Plot":

        x_axis = st.sidebar.selectbox("X-axis", df.columns)

        y_axis = st.sidebar.selectbox("Y-axis", df.columns)

        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot of {y_axis} vs {x_axis}")

        st.plotly_chart(fig)
 
    elif plot_type == "Distribution Plot":

        column = st.sidebar.selectbox("Select Column", df.select_dtypes(include=['float', 'int']).columns)

        fig = px.histogram(df, x=column, title=f"Distribution of {column}")

        st.plotly_chart(fig)
 
    elif plot_type == "Time Series":

        date_col = st.sidebar.selectbox("Select Date Column", df.select_dtypes(include=['datetime']).columns)

        y_col = st.sidebar.selectbox("Select Y-axis", df.columns)

        royal_time_series(df, date_col, y_col)
 
# Export royal PDF report

def export_pdf(df):

    with BytesIO() as buffer:

        fig, ax = plt.subplots()

        df.hist(ax=ax)

        fig.savefig(buffer, format="pdf")

        buffer.seek(0)

        return buffer.getvalue()
 
if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        df_cleaned = clean_data(df)

        st.success("The royal dataset has been cleansed for Your Majesty!")
 
        # Display royal data

        search_and_filter(df_cleaned)
 
        # Royal insights and summary

        royal_summary(df_cleaned)

        royal_insights(df_cleaned)
 
        # Visualize thy data

        visualize_data(df_cleaned)
 
        # Download buttons

        st.subheader("📥 Download thy Royal Data")

        csv = df_cleaned.to_csv(index=False).encode('utf-8')

        st.download_button("Download as CSV", data=csv, file_name='royal_data.csv', mime='text/csv')
 
        # PDF report

        st.download_button("Download Royal PDF Report", data=export_pdf(df_cleaned), file_name="royal_report.pdf", mime="application/pdf")
 
    except Exception as e:

        st.error(f"Apologies, Your Majesty, there was an error: {e}")
 
else:

    st.info("Your Majesty, we await your royal CSV file.")

 