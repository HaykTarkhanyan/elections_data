import pandas as pd
import streamlit as st
import altair as alt

#load data
df = pd.read_parquet("elections.parquet")

region_counts = df['marz'].value_counts().reset_index()
sorted_region_counts = region_counts.sort_values(by= "count", ascending= False)

first_region = sorted_region_counts.iloc[0]
top5 = region_counts.head(5)

st.title("🗳️ Voter Activity by Region in Armenia")
st.markdown("---")

st.subheader("🏆 Most Active Region")
st.success(f"🏆 The most active region is **{first_region['marz']}** with **{first_region['count']}** voters.")

st.markdown("---")

st.subheader("🏅 Top 5 Most Active Regions")
st.dataframe(top5)

st.markdown("---")

st.markdown("### 📊 **Sorted Voter Counts by Region**")
chart = alt.Chart(sorted_region_counts).mark_bar(color="#4E79A7").encode(
    x=alt.X('marz:N', sort='-y', title="Region"),
    y=alt.Y('count:Q', title="Number of Voters"),
    tooltip=["marz", "count"]
).properties(
    height=400,
    width=700
)

st.altair_chart(chart, use_container_width=True)






