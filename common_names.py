import pandas as pd
import streamlit as st

df = pd.read_parquet("elections.parquet")

common_first_names = df['anun'].value_counts().head(5).reset_index()
common_first_names.columns = ['Name', 'Count']
common_first_names.index = ['🥇','🥈','🥉','🏅', '🎖']

common_last_names = df['azganun'].value_counts().head(5).reset_index()
common_last_names.columns = ['LastName', 'Count']
common_last_names.index = ['🥇','🥈','🥉','🏅', '🎖']

st.header("🔝 Most Common First and Last Names in the Dataset")

#Common Names
st.subheader("Most Common First Names")
for emoji, row in common_first_names.iterrows():
    st.markdown(f"{emoji} **{row['Name']}** — {row['Count']} times")

#Common LastNames
st.subheader("Most Common Last Names")
for emoji, row in common_last_names.iterrows():
    st.markdown(f"{emoji} **{row['LastName']}** — {row['Count']} times")

st.markdown("---")
#Search a Name
st.subheader("🔍 Search for a name")
input_name = st.text_input(
    "Enter a first name (in Armenian letters):",
    key="first_name_input",
    placeholder="e.g. Անահիտ")

if input_name:
    count = df['anun'].str.strip().str.lower().value_counts().get(input_name.strip().lower(), 0)
    if count > 0:
        st.success(f"✅ The name **{input_name}** appears **{count}** times in the dataset.")
    else:
        st.warning(f"⚠️ The name **{input_name}** was not found in the dataset.")

#Search a LastName
st.subheader("🔍 Search for a last name")
input_last_name = st.text_input(
    "Enter a last name (in Armenian letters):",
    key="last_name_input",
    placeholder="e.g. Գրիգորյան"
)

if input_last_name:
    count = df['azganun'].str.strip().str.lower().value_counts().get(input_last_name.strip().lower(), 0)
    if count > 0:
        st.success(f"✅ The name **{input_last_name}** appears **{count}** times in the dataset.")
    else:
        st.warning(f"⚠️ The name **{input_last_name}** was not found in the dataset.")
