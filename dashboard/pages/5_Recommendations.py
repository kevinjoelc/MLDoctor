import streamlit as st
import pandas as pd
import streamlit as st

if "df" not in st.session_state:
    st.warning("📁 Please upload a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
st.set_page_config(
    page_title="AI Recommendations",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI Dataset Recommendations")

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

st.subheader("📋 Dataset Summary")

rows, cols = df.shape

missing = df.isna().sum().sum()
duplicates = df.duplicated().sum()

numeric = len(df.select_dtypes(include="number").columns)
categorical = len(df.select_dtypes(exclude="number").columns)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", rows)
c2.metric("Columns", cols)
c3.metric("Missing", missing)
c4.metric("Duplicates", duplicates)

st.divider()

st.subheader("🧠 AI Recommendations")

# Missing Values
if missing == 0:
    st.success("✅ No missing values detected.")
elif missing < rows:
    st.warning("⚠ Fill missing values using Mean, Median, or Mode.")
else:
    st.error("❌ Large number of missing values. Consider removing columns with excessive missing data.")

# Duplicate Rows
if duplicates == 0:
    st.success("✅ No duplicate rows found.")
else:
    st.warning(f"⚠ Remove {duplicates} duplicate rows.")

# Categorical Columns
if categorical > 0:
    st.info(f"ℹ Encode {categorical} categorical column(s) using One-Hot or Label Encoding.")
else:
    st.success("✅ No categorical columns found.")

# Numeric Columns
if numeric > 0:
    st.info("ℹ Scale numeric features using StandardScaler or MinMaxScaler.")

# Correlation
corr = df.select_dtypes(include="number").corr().abs()

high_corr = []

for i in range(len(corr.columns)):
    for j in range(i + 1, len(corr.columns)):
        if corr.iloc[i, j] > 0.85:
            high_corr.append((corr.columns[i], corr.columns[j]))

if high_corr:
    st.warning("⚠ Highly correlated columns detected:")

    for a, b in high_corr:
        st.write(f"- {a} ↔ {b}")

else:
    st.success("✅ No highly correlated features.")

st.divider()

st.subheader("🏆 Recommended Machine Learning Models")

if categorical <= 5:
    st.success("✔ Logistic Regression")
    st.success("✔ Random Forest")
    st.success("✔ XGBoost")
    st.success("✔ Decision Tree")
else:
    st.success("✔ Linear Regression")
    st.success("✔ Random Forest Regressor")
    st.success("✔ XGBoost Regressor")
    st.success("✔ Gradient Boosting")

st.divider()

st.subheader("🚀 Suggested Pipeline")

st.code("""
1. Remove duplicates
2. Handle missing values
3. Encode categorical columns
4. Scale numerical columns
5. Train/Test Split
6. Train Model
7. Evaluate Performance
""")