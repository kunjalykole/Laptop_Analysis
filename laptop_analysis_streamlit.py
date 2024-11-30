# Streamlit app code for visualizing Price (Amount) variations with Plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("Cleaned_data.csv")  # Replace with the actual path if running locally

# Title and description
st.title("Price Analysis Dashboard")
st.markdown("Explore the variation of Price with other columns in the dataset.")

# Sidebar for column selection
categorical_cols = ['Company', 'TypeName', 'Cpu', 'Gpu', 'OpSys']
numerical_cols = ['Ram', 'Weight', 'Touchscreen', 'IPS', 'ppi']

all_columns = categorical_cols + numerical_cols
selected_column = st.sidebar.selectbox("Select a column to compare with Price:", all_columns)

# Plotting
if selected_column:
    if selected_column in categorical_cols:
        # Bar chart for categorical columns
        fig = px.box(df, x=selected_column, y="Price", title=f"Price variation by {selected_column}")
    else:
        # Scatter plot for numerical columns
        fig = px.scatter(df, x=selected_column, y="Price", trendline="ols",
                         title=f"Price vs {selected_column}")

    st.plotly_chart(fig)