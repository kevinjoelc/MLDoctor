import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import os

st.write("VISUALIZATIONS PAGE LOADED")

# ==========================================================
# REPORT ASSETS
# ==========================================================

os.makedirs("report_assets", exist_ok=True)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Visualizations",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# LOAD DATASET
# ==========================================================

df = st.session_state.get("df")

if df is None:

    st.warning("⚠ Please upload a dataset from Home Page.")

    st.stop()

# ==========================================================
# TITLE
# ==========================================================

st.title("📊 Advanced Data Visualizations")

st.markdown(
"""
Generate professional visualizations for exploratory
data analysis and PDF report generation.
"""
)

# ==========================================================
# DATASET INFORMATION
# ==========================================================

rows = len(df)

cols = len(df.columns)

numeric_cols = df.select_dtypes(include=np.number).columns

categorical_cols = df.select_dtypes(exclude=np.number).columns

# ==========================================================
# QUICK SUMMARY
# ==========================================================

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Rows",
    rows
)

c2.metric(
    "Columns",
    cols
)

c3.metric(
    "Numeric",
    len(numeric_cols)
)

c4.metric(
    "Categorical",
    len(categorical_cols)
)

st.divider()

# ==========================================================
# DATA PREVIEW
# ==========================================================

with st.expander("Dataset Preview",expanded=False):

    st.dataframe(
        df.head(15),
        use_container_width=True
    )

st.divider()

# ==========================================================
# HISTOGRAMS
# ==========================================================

st.header("📈 Histograms")

if len(numeric_cols)==0:

    st.info("No numeric columns found.")

else:

    column = st.selectbox(
        "Select Numeric Column",
        numeric_cols,
        key="histogram"
    )

    fig = px.histogram(

        df,

        x=column,

        nbins=30,

        marginal="box",

        title=f"Histogram of {column}"

    )

    fig.update_layout(

        template="plotly_white",

        height=600

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(
            "report_assets/histograms.png",
            width=1200,
            height=700
        )

    except:
        pass

st.divider()

# ==========================================================
# BOXPLOT
# ==========================================================

st.header("📦 Box Plot")

if len(numeric_cols):

    column = st.selectbox(

        "Select Column",

        numeric_cols,

        key="box"

    )

    fig = px.box(

        df,

        y=column,

        points="outliers",

        title=f"Box Plot of {column}"

    )

    fig.update_layout(

        template="plotly_white",

        height=600

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/boxplots.png",

            width=1200,

            height=700

        )

    except:

        pass

st.divider()

# ==========================================================
# SCATTER PLOT
# ==========================================================

st.header("📉 Scatter Plot")

if len(numeric_cols)>=2:

    x = st.selectbox(

        "X Axis",

        numeric_cols,

        key="scatter_x"

    )

    y = st.selectbox(

        "Y Axis",

        numeric_cols,

        index=1,

        key="scatter_y"

    )

    fig = px.scatter(

        df,

        x=x,

        y=y,

        trendline="ols",

        title=f"{x} vs {y}"

    )

    fig.update_layout(

        template="plotly_white",

        height=650

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/scatter.png",

            width=1200,

            height=700

        )

    except:

        pass

st.divider()

# ==========================================================
# PIE CHART
# ==========================================================

st.header("🥧 Pie Chart")

if len(categorical_cols):

    pie_col = st.selectbox(
        "Select Categorical Column",
        categorical_cols,
        key="pie"
    )

    vc = df[pie_col].value_counts().head(10)

    fig = px.pie(

        names=vc.index,

        values=vc.values,

        title=f"{pie_col} Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=600

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/pie.png",

            width=1200,

            height=700

        )

    except:

        pass

st.divider()

# ==========================================================
# BAR CHART
# ==========================================================

st.header("📊 Bar Chart")

if len(categorical_cols):

    bar_col = st.selectbox(

        "Select Category",

        categorical_cols,

        key="bar"

    )

    vc = df[bar_col].value_counts().head(15)

    fig = px.bar(

        x=vc.index,

        y=vc.values,

        labels={"x":"Category","y":"Count"},

        title=f"{bar_col} Frequency"

    )

    fig.update_layout(

        template="plotly_white",

        height=600

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/bar.png",

            width=1200,

            height=700

        )

    except:

        pass

st.divider()

# ==========================================================
# LINE CHART
# ==========================================================

st.header("📈 Line Chart")

if len(numeric_cols):

    line_col = st.selectbox(

        "Select Numeric Feature",

        numeric_cols,

        key="line"

    )

    fig = px.line(

        df,

        y=line_col,

        title=f"{line_col} Trend"

    )

    fig.update_layout(

        template="plotly_white",

        height=600

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/line.png",

            width=1200,

            height=700

        )

    except:

        pass

st.divider()

# ==========================================================
# VIOLIN PLOT
# ==========================================================

st.header("🎻 Violin Plot")

if len(numeric_cols):

    violin_col = st.selectbox(

        "Select Numeric Feature",

        numeric_cols,

        key="violin"

    )

    fig = px.violin(

        df,

        y=violin_col,

        box=True,

        points="all",

        title=f"Violin Plot - {violin_col}"

    )

    fig.update_layout(

        template="plotly_white",

        height=650

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/violin.png",

            width=1200,

            height=700

        )

    except:

        pass

st.divider()

# ==========================================================
# DISTRIBUTION PLOT
# ==========================================================

st.header("📉 Distribution Plot")

if len(numeric_cols):

    dist_col = st.selectbox(

        "Distribution Column",

        numeric_cols,

        key="dist"

    )

    fig = ff.create_distplot(

        [df[dist_col].dropna()],

        [dist_col],

        show_hist=True,

        show_rug=False

    )

    fig.update_layout(

        title=f"Distribution of {dist_col}",

        template="plotly_white",

        height=650

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/distribution.png",

            width=1200,

            height=700

        )

    except:

        pass

st.divider()

# ==========================================================
# COUNT PLOT
# ==========================================================

st.header("📋 Count Plot")

if len(categorical_cols):

    count_col = st.selectbox(

        "Select Category",

        categorical_cols,

        key="count"

    )

    vc = df[count_col].value_counts()

    fig = px.bar(

        x=vc.index,

        y=vc.values,

        title=f"Count Plot - {count_col}"

    )

    fig.update_layout(

        template="plotly_white",

        height=600

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/countplot.png",

            width=1200,

            height=700

        )

    except:

        pass

st.divider()

# ==========================================================
# CORRELATION HEATMAP
# ==========================================================

st.header("🔥 Correlation Heatmap")

if len(numeric_cols) >= 2:

    corr = df[numeric_cols].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Feature Correlation Matrix",
        aspect="auto"
    )

    fig.update_layout(
        template="plotly_white",
        height=750
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    try:
        fig.write_image(
            "report_assets/correlation.png",
            width=1400,
            height=900
        )
    except:
        pass

st.divider()

# ==========================================================
# MISSING VALUE HEATMAP
# ==========================================================

st.header("❌ Missing Value Heatmap")

missing_df = df.isnull().astype(int)

fig = px.imshow(
    missing_df.T,
    color_continuous_scale="Reds",
    aspect="auto",
    title="Missing Value Heatmap"
)

fig.update_layout(
    template="plotly_white",
    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

try:

    fig.write_image(
        "report_assets/missing.png",
        width=1400,
        height=900
    )

except:
    pass

st.divider()

# ==========================================================
# CORRELATION TABLE
# ==========================================================

st.header("📋 Strong Correlations")

if len(numeric_cols) >= 2:

    corr = df[numeric_cols].corr().abs()

    corr_pairs = []

    cols = corr.columns

    for i in range(len(cols)):

        for j in range(i + 1, len(cols)):

            value = corr.iloc[i, j]

            if value >= 0.70:

                corr_pairs.append({

                    "Feature 1": cols[i],

                    "Feature 2": cols[j],

                    "Correlation": round(value, 3)

                })

    if len(corr_pairs):

        corr_df = pd.DataFrame(corr_pairs)

        st.dataframe(
            corr_df,
            use_container_width=True
        )

    else:

        st.success(
            "No highly correlated features detected."
        )

st.divider()

# ==========================================================
# CORRELATION BAR CHART
# ==========================================================

st.header("📊 Top Correlations")

if len(numeric_cols) >= 2 and len(corr_pairs):

    corr_df = corr_df.sort_values(
        "Correlation",
        ascending=False
    )

    fig = px.bar(

        corr_df,

        x="Correlation",

        y="Feature 1",

        color="Correlation",

        orientation="h",

        hover_data=["Feature 2"],

        title="Highest Correlations"

    )

    fig.update_layout(

        template="plotly_white",

        height=700

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    try:

        fig.write_image(

            "report_assets/top_correlations.png",

            width=1400,

            height=900

        )

    except:

        pass

st.divider()

# ==========================================================
# DATA TYPES
# ==========================================================

st.header("📑 Dataset Composition")

types = df.dtypes.astype(str).value_counts()

fig = px.pie(

    names=types.index,

    values=types.values,

    hole=0.4,

    title="Data Types"

)

fig.update_layout(

    template="plotly_white",

    height=600

)

st.plotly_chart(

    fig,

    use_container_width=True

)

try:

    fig.write_image(

        "report_assets/datatypes.png",

        width=1200,

        height=700

    )

except:

    pass

st.divider()

# Dataset statistics
rows = len(df)
cols = len(df.columns)

missing = int(df.isna().sum().sum())
duplicates = int(df.duplicated().sum())

numeric = len(df.select_dtypes(include="number").columns)
categorical = len(df.select_dtypes(exclude="number").columns)

# ==========================================================
# AI VISUAL INSIGHTS
# ==========================================================

st.header("🤖 AI Insights")

insights = []

if missing == 0:
    insights.append(
        "✅ No missing values detected."
    )
else:
    insights.append(
        f"⚠ Dataset contains {missing} missing values."
    )

if duplicates == 0:
    insights.append(
        "✅ No duplicate rows found."
    )
else:
    insights.append(
        f"⚠ {duplicates} duplicate rows detected."
    )

if len(numeric_cols):

    insights.append(
        f"📈 {len(numeric_cols)} numerical features available."
    )

if len(categorical_cols):

    insights.append(
        f"📋 {len(categorical_cols)} categorical features available."
    )

if len(numeric_cols) >= 2:

    max_corr = corr.where(
        np.triu(np.ones(corr.shape), k=1).astype(bool)
    ).max().max()

    insights.append(
        f"🔥 Highest correlation = {round(max_corr,2)}"
    )

for item in insights:

    st.success(item)

st.divider()

# ==========================================================
# PAIRWISE SCATTER MATRIX
# ==========================================================

st.header("🌐 Scatter Matrix")

if len(numeric_cols) >= 2:

    cols_to_use = list(numeric_cols[:5])  # Limit for performance

    fig = px.scatter_matrix(
        df,
        dimensions=cols_to_use,
        title="Scatter Matrix"
    )

    fig.update_layout(
        height=850,
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    try:
        fig.write_image(
            "report_assets/scatter_matrix.png",
            width=1500,
            height=1200
        )
    except:
        pass

st.divider()

# ==========================================================
# FEATURE DISTRIBUTION SUMMARY
# ==========================================================

st.header("📊 Feature Summary")

summary_df = pd.DataFrame({

    "Feature": df.columns,

    "Datatype": df.dtypes.astype(str),

    "Missing": df.isna().sum(),

    "Unique": df.nunique()

})

st.dataframe(
    summary_df,
    use_container_width=True,
    height=450
)

st.divider()

# ==========================================================
# DATA QUALITY SCORE
# ==========================================================

st.header("🏥 Dataset Health")

score = 100

score -= min(missing,20)

score -= min(duplicates*2,20)

st.progress(score/100)

if score>=90:

    st.success("Excellent Dataset")

elif score>=75:

    st.info("Good Dataset")

elif score>=50:

    st.warning("Dataset Needs Cleaning")

else:

    st.error("Poor Dataset")

st.metric(
    "Health Score",
    f"{score}/100"
)

st.divider()

# ==========================================================
# DATA QUALITY DASHBOARD
# ==========================================================

st.header("📋 Data Quality Dashboard")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Rows",
    rows
)

c2.metric(
    "Columns",
    cols
)

c3.metric(
    "Missing",
    missing
)

c4.metric(
    "Duplicates",
    duplicates
)

st.divider()

# ==========================================================
# ML READINESS
# ==========================================================

st.header("🤖 ML Readiness")

checks=[]

checks.append(("Dataset Loaded",True))

checks.append(("Numeric Features",len(numeric_cols)>0))

checks.append(("Categorical Features",len(categorical_cols)>=0))

checks.append(("No Missing Values",missing==0))

checks.append(("No Duplicates",duplicates==0))

checks.append(("Enough Rows",rows>50))

for title,status in checks:

    if status:

        st.success(f"✅ {title}")

    else:

        st.error(f"❌ {title}")

st.divider()

# ==========================================================
# RECOMMENDED PREPROCESSING
# ==========================================================

st.header("🧠 AI Preprocessing Recommendations")

recommendations=[]

if missing>0:

    recommendations.append(
        "Fill missing values using Median/Mode."
    )

if duplicates>0:

    recommendations.append(
        "Remove duplicate rows."
    )

if len(categorical_cols):

    recommendations.append(
        "Encode categorical variables."
    )

if len(numeric_cols):

    recommendations.append(
        "Normalize or Standardize numerical features."
    )

if len(numeric_cols)>=2:

    recommendations.append(
        "Check feature correlations before training."
    )

recommendations.extend([

    "Split into Train/Test datasets.",

    "Perform Cross Validation.",

    "Compare multiple ML models.",

    "Tune Hyperparameters.",

    "Evaluate using suitable metrics."

])

for rec in recommendations:

    st.info("• "+rec)

st.divider()

# ==========================================================
# PDF STATUS
# ==========================================================

st.header("📄 Export Report Status")

required_images=[

    "histograms.png",

    "boxplots.png",

    "scatter.png",

    "pie.png",

    "bar.png",

    "line.png",

    "distribution.png",

    "countplot.png",

    "correlation.png",

    "missing.png",

    "top_correlations.png",

    "datatypes.png",

    "scatter_matrix.png"

]

status=[]

for img in required_images:

    path=os.path.join(
        "report_assets",
        img
    )

    status.append({

        "Image":img,

        "Available":os.path.exists(path)

    })

status_df=pd.DataFrame(status)

st.dataframe(
    status_df,
    use_container_width=True
)

if status_df["Available"].all():

    st.success(
        "✅ All report images generated successfully."
    )

else:

    st.warning(
        "⚠ Some report images are missing. Generate all charts before exporting the PDF."
    )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
<div style='text-align:center'>

### MLDoctor

AI Powered Dataset Diagnostic System

Dataset Visualization & Exploratory Data Analysis Module

</div>
""",
    unsafe_allow_html=True
)