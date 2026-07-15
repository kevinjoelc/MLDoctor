import streamlit as st
import pandas as pd
import streamlit as st

if "df" not in st.session_state:
    st.warning("📁 Please upload a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
# ---------------- Page ---------------- #

st.set_page_config(
    page_title="Model Recommendation",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #

with open("dashboard/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- Title ---------------- #

st.title("💻 AI Model Recommendation")
st.caption("Automatically recommend the best Machine Learning models")

st.divider()

# ---------------- Upload ---------------- #

uploaded_file = st.sidebar.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

uploaded_file = st.session_state.get("uploaded_file")

if uploaded_file is None:
    st.warning("⚠ Please upload a dataset from the Home page.")
    st.stop()

uploaded_file.seek(0)
df = pd.read_csv(uploaded_file)

# ---------------- Target Selection ---------------- #

target = st.selectbox(
    "🎯 Select Target Column",
    df.columns
)

st.divider()

# ---------------- Detect Problem Type ---------------- #

if df[target].dtype == "object":

    problem = "Classification"

elif df[target].nunique() <= 10:

    problem = "Classification"

else:

    problem = "Regression"

st.success(f"Detected Problem Type: **{problem}**")

# ---------------- Recommendations ---------------- #

if problem == "Classification":

    models = pd.DataFrame({

        "Model":[
            "Logistic Regression",
            "Random Forest",
            "XGBoost",
            "Support Vector Machine",
            "Naive Bayes"
        ],

        "Accuracy":"High",

        "Speed":[
            "Fast",
            "Medium",
            "Medium",
            "Slow",
            "Fast"
        ],

        "Interpretability":[
            "Excellent",
            "Good",
            "Medium",
            "Low",
            "Excellent"
        ]
    })

else:

    models = pd.DataFrame({

        "Model":[
            "Linear Regression",
            "Random Forest Regressor",
            "XGBoost Regressor",
            "Decision Tree",
            "SVR"
        ],

        "Accuracy":"High",

        "Speed":[
            "Fast",
            "Medium",
            "Medium",
            "Fast",
            "Slow"
        ],

        "Interpretability":[
            "Excellent",
            "Good",
            "Medium",
            "Excellent",
            "Low"
        ]
    })

st.subheader("🏆 Recommended Models")

st.dataframe(
    models,
    use_container_width=True,
    hide_index=True
)

# ---------------- AI Suggestions ---------------- #

st.subheader("🧠 AI Suggestions")

missing = df.isna().sum().sum()

duplicates = df.duplicated().sum()

if missing:
    st.warning("⚠ Handle missing values before training.")

if duplicates:
    st.warning("⚠ Remove duplicate rows.")

if len(df.select_dtypes(include="object").columns):
    st.info("ℹ Encode categorical columns.")

st.success("✔ Scale numeric features if required.")

st.success("✔ Perform train-test split.")

st.success("✔ Use cross-validation.")

# ---------------- Metrics ---------------- #

st.subheader("📏 Recommended Evaluation Metrics")

if problem == "Classification":

    st.write("- Accuracy")
    st.write("- Precision")
    st.write("- Recall")
    st.write("- F1 Score")
    st.write("- ROC-AUC")

else:

    st.write("- MAE")
    st.write("- MSE")
    st.write("- RMSE")
    st.write("- R² Score")