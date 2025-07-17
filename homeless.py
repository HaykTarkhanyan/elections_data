import pandas as pd
import streamlit as st

df = pd.read_parquet("elections.parquet")

st.title("🏠 Homeless People Percentage in Armenia")

st.caption(
    "This dashboard shows the percentage of voters who **do not have a registered address**, "
    "based on official election data. "
    "Such voters can be considered as *homeless* in essence."
)

st.divider()

empty_address_count = df['hasce'].apply(
    lambda x: pd.isna(x) or str(x).strip().lower() in ['', 'nan', 'null', 'none']
).sum()

total_rows = len(df)

percentage_of_homeless = empty_address_count / total_rows * 100

st.subheader("📊 Summary of Findings")
st.markdown(
    f"""
    - ✅ **Total voters**: **{total_rows:,}**
    - 🚫 **Voters without address (homeless)**: **{empty_address_count:,}**
    - 📈 **Percentage of homeless voters**: **{percentage_of_homeless:.4f}%**
    """
)

st.metric(label="Homeless Percentage", value=f"{percentage_of_homeless:.4f}%", delta=None)

st.success("✅ Analysis completed successfully!")
