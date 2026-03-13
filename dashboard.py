import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Talent Analytics", layout="wide")
st.title("🎯 My First Talent Dashboard")

# Load data
df = pd.read_csv('employee_data.csv')

# Show raw data
st.subheader("📋 Employee Data")
st.dataframe(df)

# Basic metrics
st.subheader("📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Employees", len(df))
with col2:
    attrition_rate = df['attrition'].mean() * 100
    st.metric("Attrition Rate", f"{attrition_rate:.1f}%")
with col3:
    avg_salary = df['salary'].mean()
    st.metric("Avg Salary", f"${avg_salary:,.0f}")
with col4:
    avg_tenure = df['tenure'].mean()
    st.metric("Avg Tenure", f"{avg_tenure:.1f} years")

# Simple chart
st.subheader("📈 Employees by Department")
dept_counts = df['department'].value_counts()

fig, ax = plt.subplots()
dept_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
st.pyplot(fig)

# Filter by department
st.subheader("🔍 Filter Data")
selected_dept = st.selectbox("Select Department", df['department'].unique())

# Show filtered data
filtered_df = df[df['department'] == selected_dept]
st.write(f"Showing {len(filtered_df)} employees from {selected_dept}")

st.dataframe(filtered_df)
