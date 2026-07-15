import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

if "df" not in st.session_state:
    st.warning("📁 Please upload a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
# ---------------- Page ---------------- #

st.set_page_config(
    page_title="Missing Values",
    page_icon="🧹",
    layout="wide"
)

# ---------------- CSS ---------------- #

with open("dashboard/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- Title ---------------- #

st.title("🧹 Missing Values Analysis")
st.caption("Analyze missing values and receive AI recommendations.")
st.divider()

# ---------------- Upload ---------------- #

uploaded_file = st.session_state.get("uploaded_file")

if uploaded_file is None:
    st.warning("⚠ Please upload a dataset from the Home page.")
    st.stop()

uploaded_file.seek(0)
df = pd.read_csv(uploaded_file)
# ---------------- Missing Statistics ---------------- #

missing = df.isnull().sum()

missing_df = pd.DataFrame({
    "Column": missing.index,
    "Missing Values": missing.values
})

missing_df["Percentage"] = (
    missing_df["Missing Values"] / len(df) * 100
).round(2)

missing_df = missing_df.sort_values(
    "Missing Values",
    ascending=False
)

# ---------------- KPI ---------------- #

total_missing = int(missing.sum())

cols_with_missing = int((missing > 0).sum())

c1, c2, c3 = st.columns(3)

c1.metric("Total Missing", total_missing)

c2.metric("Affected Columns", cols_with_missing)

c3.metric("Dataset Size", f"{len(df):,}")

st.divider()

# ---------------- Bar Chart ---------------- #

st.subheader("📊 Missing Values by Column")

fig = px.bar(
    missing_df,
    x="Column",
    y="Missing Values",
    color="Percentage",
    text="Missing Values",
    title="Missing Values per Column"
)

fig.update_layout(height=500)

st.plotly_chart(fig, use_container_width=True)

# ---------------- Table ---------------- #

st.subheader("📋 Missing Value Report")

st.dataframe(
    missing_df,
    use_container_width=True,
    height=450
)

# ---------------- AI Suggestions ---------------- #

st.subheader("🤖 AI Recommendations")

for _, row in missing_df.iterrows():

    if row["Missing Values"] == 0:
        continue

    pct = row["Percentage"]

    if pct < 5:
        rec = "Fill with Mean / Median / Mode"

    elif pct < 30:
        rec = "Use KNN Imputer or Median"

    else:
        rec = "Consider Dropping the Column"

    st.info(
        f"**{row['Column']}** → {pct}% missing → **{rec}**"
    )