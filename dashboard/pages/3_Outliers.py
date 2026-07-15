import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

if "df" not in st.session_state:
    st.warning("📁 Please upload a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
st.set_page_config(page_title="Outliers", page_icon="📊", layout="wide")

st.title("📊 Outlier Detection")

uploaded_file = st.session_state.get("uploaded_file")

if uploaded_file is None:
    st.warning("⚠ Please upload a dataset from the Home page.")
    st.stop()

uploaded_file.seek(0)
df = pd.read_csv(uploaded_file)

numeric = df.select_dtypes(include="number").columns

col = st.selectbox("Select Numeric Column", numeric)

fig = px.box(
    df,
    y=col,
    title=f"Outliers in {col}"
)

st.plotly_chart(fig, use_container_width=True)

Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df[col] < Q1 - 1.5 * IQR) |
    (df[col] > Q3 + 1.5 * IQR)
]

st.metric("Outliers Found", len(outliers))

st.dataframe(outliers)