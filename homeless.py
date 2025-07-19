import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(layout="wide")

st.title("🏠 Homeless Voters Dashboard - Armenia Elections")

st.caption(
    "This dashboard shows the **percentage and distribution of homeless voters** in Armenia, "
    "based on official election data. "
    "Homeless voters are identified as those without a registered address."
)

st.divider()

df = pd.read_parquet("elections.parquet")

def is_homeless(x):
    if pd.isna(x):
        return True
    x = str(x).strip().lower()
    return x in ['', 'nan', 'null', 'none']

homeless_df = df[df['hasce'].apply(is_homeless)]

empty_address_count = len(homeless_df)
total_rows = len(df)
percentage_of_homeless = empty_address_count / total_rows * 100

st.subheader("📊 Summary")
st.markdown(
    f"""
    - ✅ **Total voters**: **{total_rows:,}**
    - 🚫 **Voters without address (homeless)**: **{empty_address_count:,}**
    - 📈 **Percentage of homeless voters**: **{percentage_of_homeless:.4f}%**
    """
)
st.metric(label="Homeless Percentage", value=f"{percentage_of_homeless:.4f}%")

st.divider()


st.subheader("📊 Distribution by Region (marz)")

homeless_by_marz = homeless_df.groupby('marz').size().reset_index(name='count').sort_values(by='count', ascending=False)

fig_bar = px.bar(
    homeless_by_marz,
    x='marz',
    y='count',
    text='count',
    color='count',
    color_continuous_scale="Reds",
    labels={'marz': 'Region (marz)', 'count': 'Homeless Count'},
    title="Homeless Voters Count by Region",
)
fig_bar.update_layout(
    xaxis_title="Region (marz)",
    yaxis_title="Homeless Count",
    title_x=0.5,
    showlegend=False
)

st.plotly_chart(fig_bar, use_container_width=True)

st.success("✅ Dashboard loaded successfully!")
