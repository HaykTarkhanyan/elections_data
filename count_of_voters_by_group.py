import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_parquet("elections.parquet")

df['birth_date'] = pd.to_datetime(df['or_amis_tari'], format='%d/%m/%Y', errors='coerce')
today = pd.to_datetime("today")
df['age'] = (today - df['birth_date']).dt.days // 365

age_bins = [18, 25, 35, 50, 65, 150]
age_labels = ['18-25', '26-35', '36-50', '51-65', '66+']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=True)

age_group_percentages = df['age_group'].value_counts(normalize=True).sort_index() * 100

age_df = age_group_percentages.reset_index()
age_df.columns = ['Age Group', 'Percentage']

st.title("Voter Distribution by Age Groups")

st.dataframe(age_df.round(2))

fig = px.bar(
    age_df,
    x="Age Group",
    y="Percentage",
    text="Percentage",
    labels={"Percentage": "Percentage of Voters (%)", "Age Group": "Age Groups"},
    color="Age Group",
    title="Distribution of Voters by Age Group"
)

fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig.update_layout(yaxis_title="Percentage of Voters (%)", xaxis_title="Age Groups", uniformtext_minsize=8)

st.subheader("📊 Visualisation by Bar Chart")
st.plotly_chart(fig, use_container_width=True)

st.success("✅ Age group distribution calculated and visualized!")
