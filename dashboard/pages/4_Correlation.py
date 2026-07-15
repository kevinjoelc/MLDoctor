import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

if "df" not in st.session_state:
    st.warning("📁 Please upload a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
st.set_page_config(
    page_title="Correlation Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Correlation Analysis")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

uploaded_file = st.session_state.get("uploaded_file")

if uploaded_file is None:
    st.warning("⚠ Please upload a dataset from the Home page.")
    st.stop()

uploaded_file.seek(0)
df = pd.read_csv(uploaded_file)

numeric_df = df.select_dtypes(include="number")

if numeric_df.shape[1] < 2:
    st.error("Need at least 2 numeric columns.")
    st.stop()

corr = numeric_df.corr()

st.subheader("🔥 Correlation Heatmap")

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    aspect="auto"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📋 Correlation Matrix")

st.dataframe(
    corr.round(2),
    use_container_width=True
)

st.subheader("🔍 Highly Correlated Features")

threshold = st.slider(
    "Correlation Threshold",
    0.5,
    1.0,
    0.8,
    0.05
)

pairs = []

columns = corr.columns

for i in range(len(columns)):
    for j in range(i + 1, len(columns)):
        value = abs(corr.iloc[i, j])
        if value >= threshold:
            pairs.append([
                columns[i],
                columns[j],
                round(value, 2)
            ])

if pairs:
    result = pd.DataFrame(
        pairs,
        columns=[
            "Feature 1",
            "Feature 2",
            "Correlation"
        ]
    )

    st.dataframe(
        result,
        use_container_width=True
    )
else:
    st.success("No highly correlated features found.")