import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="MLDoctor",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

def load_css():
    with open("dashboard/assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

col1, col2, col3 = st.sidebar.columns([1.2, 1, 1.2])

with col2:
    st.image("dashboard/assets/logo.png", width=65)

st.sidebar.markdown(
    """
    <h2 style="
        color:white;
        text-align:center;
        margin-top:-10px;
        margin-bottom:5px;
    ">
    MLDoctor
    </h2>

    <p style="
        text-align:center;
        color:#cbd5e1;
        font-size:15px;
        margin-bottom:25px;
    ">
    AI Powered Dataset Diagnostic System
    </p>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV Dataset",
    type=["csv"],
    key="file_uploader"
)


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df
    st.session_state["uploaded_file"] = uploaded_file

elif "df" in st.session_state:
    df = st.session_state["df"]

else:
    df = None
# --------------------------------------------------
# Hero
# --------------------------------------------------

logo_col, title_col = st.columns([1, 8])

logo_col, title_col = st.columns([1, 8])

with logo_col:
    st.markdown(
        """
        <div style="margin-top:20px; margin-left:18px;"></div>
        """,
        unsafe_allow_html=True
    )

    st.image(
        "dashboard/assets/logo.png",
        width=80
    )

with title_col:

    st.markdown("""
    <h1 style="
        margin-bottom:0;
        color:#0F172A;
        font-size:52px;
        font-weight:700;">
        MLDoctor
    </h1>

    <p style="
        font-size:24px;
        color:#64748B;
        margin-top:-8px;">
        AI Powered Dataset Diagnostic System
    </p>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>🩺 Diagnose Your Dataset in Seconds</h1>

<p>
Upload any CSV dataset and instantly receive:
</p>

<div class="feature-grid">

<div>
✅ Dataset Health Score<br>
✅ Missing Value Analysis<br>
✅ Duplicate Detection<br>
✅ Outlier Detection
</div>

<div>
✅ Correlation Analysis<br>
✅ ML Readiness Score<br>
✅ Data Cleaning Suggestions<br>
✅ Feature Importance
</div>

<div>
✅ Best ML Models<br>
✅ AI Recommendations<br>
✅ Interactive Charts<br>
✅ Export Reports
</div>

</div>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# No Dataset
# --------------------------------------------------

uploaded_file = st.session_state.get("uploaded_file")

if df is None:

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

col1, col2, col3, col4 = st.columns(4)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card green">
        <div class="icon">📊</div>
        <h3>Data Quality</h3>
        <p>100%</p>
        <span>Health Check</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card purple">
        <div class="icon">🧠</div>
        <h3>AI Analysis</h3>
        <p>8+</p>
        <span>Modules</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card blue">
        <div class="icon">📈</div>
        <h3>Visualizations</h3>
        <p>10+</p>
        <span>Charts</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card orange">
        <div class="icon">💻</div>
        <h3>ML Models</h3>
        <p>12+</p>
        <span>Recommendations</span>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# --------------------------------------------------
# Read Dataset
# --------------------------------------------------

uploaded_file.seek(0)
df = pd.read_csv(uploaded_file)

# --------------------------------------------------
# Dataset Loaded
# --------------------------------------------------

st.success("✅ Dataset Loaded Successfully")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

rows = df.shape[0]
cols = df.shape[1]
missing = int(df.isna().sum().sum())
duplicates = int(df.duplicated().sum())

numeric = len(df.select_dtypes(include="number").columns)
categorical = len(df.select_dtypes(exclude="number").columns)

st.markdown("## 📊 Dataset Overview")

c1,c2,c3 = st.columns(3)
c4,c5,c6 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-card">
    <h4>Rows</h4>
    <h2>{rows:,}</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
    <h4>Columns</h4>
    <h2>{cols}</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
    <h4>Missing</h4>
    <h2>{missing}</h2>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
    <h4>Duplicates</h4>
    <h2>{duplicates}</h2>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="metric-card">
    <h4>Numeric</h4>
    <h2>{numeric}</h2>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown(f"""
    <div class="metric-card">
    <h4>Categorical</h4>
    <h2>{categorical}</h2>
    </div>
    """, unsafe_allow_html=True)
#========
# Dataset Health Score
# ===============================================

health_score = 100

if missing > 0:
    health_score -= min(30, (missing / (rows * cols)) * 100)

if duplicates > 0:
    health_score -= min(20, (duplicates / rows) * 100)

health_score = max(0, round(health_score))

st.divider()

score1, score2 = st.columns([1, 2])

with score1:

    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=health_score,
        title={"text":"Dataset Health"},
        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"royalblue"},
            "steps":[
                {"range":[0,50],"color":"#ffb3b3"},
                {"range":[50,80],"color":"#ffe699"},
                {"range":[80,100],"color":"#b6f2b6"}
            ]
        }
    ))

    fig.update_layout(
        height=320,
        margin=dict(l=20,r=20,t=40,b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

with score2:

    st.subheader("📋 Dataset Summary")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Rows", f"{rows:,}")
        st.metric("Missing", missing)
        st.metric("Numeric", numeric)

    with c2:
        st.metric("Columns", cols)
        st.metric("Duplicates", duplicates)
        st.metric("Categorical", categorical)

    st.info(
        f"Memory Usage: {round(df.memory_usage().sum()/1024,2)} KB"
    )

    st.progress(health_score/100)

    if health_score >= 90:
        st.success("Excellent Dataset for Machine Learning 🟢")
    elif health_score >= 70:
        st.warning("Dataset needs minor preprocessing 🟡")
    else:
        st.error("Dataset requires preprocessing 🔴")

    
# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------


st.markdown("""
<div class="dashboard-card">
<h2>📋 Dataset Preview</h2>
<p>First 20 rows of the uploaded dataset</p>
</div>
""", unsafe_allow_html=True)

search = st.text_input(
    "🔍 Search rows",
    placeholder="Type any value..."
)

preview = df.copy()

if search:
    preview = preview[
        preview.astype(str)
               .apply(lambda x: x.str.contains(search, case=False))
               .any(axis=1)
    ]

st.dataframe(
    preview.head(20),
    use_container_width=True,
    height=450
)

csv = df.to_csv(index=False).encode()

st.download_button(
    "📥 Download Dataset",
    csv,
    "dataset.csv",
    "text/csv"
)

st.divider()

st.subheader("📊 Dataset Information")


c1, c2 = st.columns(2)
with c1:

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True,
        height=420
    )

    st.divider()

st.markdown("""
<div class="dashboard-card">
<h2>📊 Column Information</h2>
<p>Overview of every feature in the dataset</p>
</div>
""", unsafe_allow_html=True)

info = pd.DataFrame({
    "Column": df.columns,
    "Datatype": df.dtypes.astype(str),
    "Missing": df.isna().sum(),
    "Unique": df.nunique()
})

selected = st.selectbox(
    "Select Column",
    info["Column"]
)

with c2:
    st.subheader("📊 Dataset Summary")

    st.metric("Rows", rows)
    st.metric("Columns", cols)
    st.metric("Missing", missing)
    st.metric("Duplicates", duplicates)

    st.progress(health_score / 100)

    if health_score >= 90:
        st.success("Excellent Dataset")
    elif health_score >= 70:
        st.warning("Needs minor preprocessing")
    else:
        st.error("Needs preprocessing")

col_info = info[info["Column"] == selected].iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Datatype", col_info["Datatype"])
c2.metric("Missing", int(col_info["Missing"]))
c3.metric("Unique", int(col_info["Unique"]))
c4.metric(
    "Missing %",
    f"{round(col_info['Missing']/rows*100,2)}%"
)
c1, c2 = st.columns([2, 1])

with c1:
    st.dataframe(
        info,
        use_container_width=True,
        height=420
    )

    st.divider()

    st.subheader("📈 Numeric Statistics")

    numeric_df = df.select_dtypes(include="number")

    if len(numeric_df.columns):
        st.dataframe(
            numeric_df.describe().T,
            use_container_width=True
        )
    else:
        st.info("No numeric columns available.")
st.divider()

left, right = st.columns([2,1])

st.subheader("📈 Numeric Statistics")

numeric_df = df.select_dtypes(include="number")

if len(numeric_df.columns):

    st.dataframe(
        numeric_df.describe().T,
        use_container_width=True
    )

else:
    st.info("No numeric columns available.")

with c2:

    st.subheader("📌 Quick Summary")

    st.metric("Rows", f"{rows:,}")
    st.metric("Columns", cols)
    st.metric("Numeric", numeric)
    st.metric("Categorical", categorical)
    st.metric("Missing", missing)
    st.metric("Duplicates", duplicates)

    st.divider()

    st.subheader("📈 Health")

    st.progress(health_score/100)

    if health_score >= 90:
        st.success("Excellent Dataset")
    elif health_score >= 70:
        st.warning("Needs Minor Cleaning")
    else:
        st.error("Needs Preprocessing")

    st.divider()

    st.subheader("🚀 Workflow")

    st.markdown("""
    ✅ Upload Dataset

    ✅ Analyze Quality

    ✅ Visualize

    ✅ Train ML Model

    ✅ Export Report
    """)

st.divider()

st.subheader("🧠 AI Dataset Insights")

problem = "Unknown"

target = df.columns[-1]

if df[target].dtype == "object":
    if df[target].nunique() <= 20:
        problem = "Classification"
    else:
        problem = "Text Dataset"

else:
    if df[target].nunique() <= 15:
        problem = "Classification"
    else:
        problem = "Regression"

c1, c2 = st.columns(2)

with c1:

    st.success(f"""
Target Column

**{target}**
    """)

    st.info(f"""
Problem Type

**{problem}**
    """)

with c2:

    st.info(f"""
Rows

**{rows:,}**
    """)

    st.info(f"""
Features

**{cols-1}**
    """)

st.subheader("🔍 Data Quality Report")

warnings = []

if missing > 0:
    warnings.append(f"⚠ {missing} Missing Values found")

if duplicates > 0:
    warnings.append(f"⚠ {duplicates} Duplicate Rows found")

if numeric < 2:
    warnings.append("⚠ Very few numeric columns")

if cols < 5:
    warnings.append("⚠ Small dataset")

if len(warnings)==0:
    st.success("✅ Excellent dataset. No major issues detected.")

else:
    for w in warnings:
        st.warning(w)

st.subheader("🛠 Recommended Preprocessing")

steps = []

if missing:
    steps.append("Fill missing values")

if categorical:
    steps.append("Encode categorical columns")

steps.append("Scale numerical features")
steps.append("Remove outliers")
steps.append("Train/Test Split")
steps.append("Cross Validation")

for s in steps:
    st.success("✔ " + s)

st.subheader("🤖 Recommended Models")

if problem=="Classification":

    models = [
        "Logistic Regression",
        "Random Forest",
        "XGBoost",
        "LightGBM",
        "Support Vector Machine"
    ]

else:

    models = [
        "Linear Regression",
        "Random Forest Regressor",
        "XGBoost Regressor",
        "CatBoost",
        "Gradient Boosting"
    ]

cols_model = st.columns(len(models))

for col, model in zip(cols_model, models):

    with col:
        st.markdown(f"""
<div class="metric-card">
<h4>{model}</h4>
</div>
""", unsafe_allow_html=True)

st.divider()

score = health_score

if categorical:
    score -= 5

if missing:
    score -= 10

if duplicates:
    score -= 5

score = max(0, score)

st.subheader("🚀 ML Readiness")

st.progress(score/100)

st.metric("Score", f"{score}%")
# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()


st.caption(
    "MLDoctor v1.0 • AI Powered Dataset Diagnostic System • Built with Streamlit"
)
