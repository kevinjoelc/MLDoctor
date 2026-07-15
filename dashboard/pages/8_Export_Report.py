import streamlit as st
import pandas as pd
import numpy as np
import tempfile
import os
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

# =====================================================
# LOAD DATASET
# =====================================================

df = st.session_state.get("df")
uploaded_file = st.session_state.get("uploaded_file")

if df is None:
    st.warning("⚠ Please upload a dataset first.")
    st.stop()

# =====================================================
# DATASET SUMMARY
# =====================================================

rows = df.shape[0]
cols = df.shape[1]

missing = int(df.isna().sum().sum())
duplicates = int(df.duplicated().sum())

numeric = len(df.select_dtypes(include=np.number).columns)
categorical = len(df.select_dtypes(exclude=np.number).columns)

memory = round(df.memory_usage(deep=True).sum()/1024/1024,2)

health_score = 100

health_score -= min(missing,20)
health_score -= min(duplicates*2,20)

health_score=max(0,health_score)

styles=getSampleStyleSheet()

# =====================================================
# FUNCTIONS
# =====================================================

def heading(story,text):

    story.append(
        Paragraph(
            f"<font size=22 color='darkblue'><b>{text}</b></font>",
            styles["Heading1"]
        )
    )

    story.append(Spacer(1,15))


# -----------------------------------------------------

def add_cover(story):

    story.append(
        Paragraph(
            "<font size=30 color='#1E3A8A'><b>MLDoctor AI Report</b></font>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,25))

    story.append(
        Paragraph(
            "AI Powered Dataset Diagnostic System",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1,40))

    story.append(
        Paragraph(
            f"<b>Dataset :</b> {uploaded_file.name}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Generated :</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Rows :</b> {rows}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Columns :</b> {cols}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Dataset Health :</b> {health_score}/100",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,40))

    story.append(
        Paragraph(
            "<b>Status :</b> Ready for Machine Learning",
            styles["Heading2"]
        )
    )

    story.append(PageBreak())

# -----------------------------------------------------

def add_summary(story):

    heading(story,"Dataset Summary")

    data=[

        ["Metric","Value"],

        ["Rows",rows],

        ["Columns",cols],

        ["Missing Values",missing],

        ["Duplicate Rows",duplicates],

        ["Numeric Columns",numeric],

        ["Categorical Columns",categorical],

        ["Memory Usage",f"{memory} MB"],

        ["Health Score",f"{health_score}/100"]

    ]

    table=Table(
        data,
        colWidths=[220,220]
    )

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1E3A8A")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("BACKGROUND",(0,1),(-1,-1),colors.HexColor("#EFF6FF")),

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("BOTTOMPADDING",(0,0),(-1,0),10),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("FONTSIZE",(0,0),(-1,-1),11),

    ]))

    story.append(table)

    story.append(PageBreak())

# -----------------------------------------------------

def add_column_information(story):

    heading(story,"Column Information")

    data=[[
        "Column",
        "Datatype",
        "Missing",
        "Unique",
        "Sample"
    ]]

    for col in df.columns:

        sample=""

        if len(df[col].dropna())>0:
            sample=str(df[col].dropna().iloc[0])

        data.append([
            col,
            str(df[col].dtype),
            int(df[col].isna().sum()),
            int(df[col].nunique()),
            sample[:25]
        ])

    table=Table(
        data,
        colWidths=[120,80,60,60,160]
    )

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),0.5,colors.black),

        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

        ("FONTSIZE",(0,0),(-1,-1),8),

        ("BOTTOMPADDING",(0,0),(-1,0),10)

    ]))

    story.append(table)

    story.append(PageBreak())

# -----------------------------------------------------

def add_numeric_statistics(story):

    heading(story,"Numeric Statistics")

    stats=df.describe().round(2).T

    data=[[
        "Feature",
        "Count",
        "Mean",
        "Std",
        "Min",
        "25%",
        "50%",
        "75%",
        "Max"
    ]]

    for feature in stats.index:

        data.append([

            feature,

            stats.loc[feature,"count"],

            stats.loc[feature,"mean"],

            stats.loc[feature,"std"],

            stats.loc[feature,"min"],

            stats.loc[feature,"25%"],

            stats.loc[feature,"50%"],

            stats.loc[feature,"75%"],

            stats.loc[feature,"max"]

        ])

    table=Table(data)

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.green),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("FONTSIZE",(0,0),(-1,-1),7),

    ]))

    story.append(table)

    story.append(PageBreak())

# =====================================================
# MISSING VALUE ANALYSIS
# =====================================================

def add_missing_analysis(story):

    heading(story, "Missing Value Analysis")

    story.append(
        Paragraph(
            f"<b>Total Missing Values :</b> {missing}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 10))

    data = [[
        "Column",
        "Missing",
        "Percentage",
        "Recommendation"
    ]]

    for col in df.columns:

        miss = int(df[col].isna().sum())

        percent = round((miss / rows) * 100, 2)

        if miss == 0:
            rec = "No Action Needed"

        elif pd.api.types.is_numeric_dtype(df[col]):
            rec = "Fill using Median"

        else:
            rec = "Fill using Mode"

        data.append([
            col,
            miss,
            f"{percent} %",
            rec
        ])

    table = Table(
        data,
        colWidths=[140,60,80,180]
    )

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.red),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

        ("FONTSIZE",(0,0),(-1,-1),8),

    ]))

    story.append(table)

    story.append(Spacer(1,20))

    if missing==0:

        story.append(
            Paragraph(
                "<font color='green'><b>AI Insight :</b> Excellent! No missing values detected.</font>",
                styles["BodyText"]
            )
        )

    else:

        story.append(
            Paragraph(
                "<font color='red'><b>AI Insight :</b> Missing values detected. Clean the dataset before training.</font>",
                styles["BodyText"]
            )
        )

    story.append(PageBreak())


# =====================================================
# DUPLICATE ANALYSIS
# =====================================================

def add_duplicate_analysis(story):

    heading(story, "Duplicate Analysis")

    story.append(
        Paragraph(
            f"<b>Total Duplicate Rows :</b> {duplicates}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    if duplicates==0:

        story.append(
            Paragraph(
                "<font color='green'><b>Excellent!</b> No duplicate rows were found.</font>",
                styles["BodyText"]
            )
        )

    else:

        story.append(
            Paragraph(
                "<font color='red'><b>Recommendation :</b> Remove duplicate rows before training.</font>",
                styles["BodyText"]
            )
        )

    story.append(PageBreak())


# =====================================================
# OUTLIER ANALYSIS
# =====================================================

def add_outlier_analysis(story):

    heading(story, "Outlier Analysis")

    numeric_df = df.select_dtypes(include=np.number)

    data = [[
        "Column",
        "Outliers",
        "Percentage"
    ]]

    for col in numeric_df.columns:

        q1 = numeric_df[col].quantile(0.25)
        q3 = numeric_df[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        count = ((numeric_df[col] < lower) |
                 (numeric_df[col] > upper)).sum()

        percent = round((count / rows) * 100,2)

        data.append([
            col,
            int(count),
            f"{percent}%"
        ])

    table = Table(
        data,
        colWidths=[220,100,100]
    )

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.orange),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),0.5,colors.black),

        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

        ("FONTSIZE",(0,0),(-1,-1),9),

    ]))

    story.append(table)

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>AI Recommendation :</b> Remove extreme outliers only if they are errors. Tree-based models generally handle moderate outliers well.",
            styles["BodyText"]
        )
    )

    story.append(PageBreak())


# =====================================================
# CORRELATION ANALYSIS
# =====================================================

def add_correlation_analysis(story):

    heading(story, "Correlation Analysis")

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.shape[1] < 2:

        story.append(
            Paragraph(
                "Not enough numeric columns for correlation analysis.",
                styles["BodyText"]
            )
        )

        story.append(PageBreak())

        return

    corr = numeric_df.corr().round(2)

    data = [["Feature 1","Feature 2","Correlation"]]

    cols = corr.columns

    for i in range(len(cols)):

        for j in range(i+1,len(cols)):

            value = corr.iloc[i,j]

            if abs(value)>=0.70:

                data.append([
                    cols[i],
                    cols[j],
                    value
                ])

    if len(data)==1:

        story.append(
            Paragraph(
                "No highly correlated features found.",
                styles["BodyText"]
            )
        )

    else:

        table = Table(
            data,
            colWidths=[180,180,80]
        )

        table.setStyle(TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkgreen),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),0.5,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

            ("FONTSIZE",(0,0),(-1,-1),8),

        ]))

        story.append(table)

    story.append(PageBreak())

# =====================================================
# VISUALIZATION PAGE
# =====================================================

def add_visualizations(story):

    heading(story, "Dataset Visualizations")

    images = [

    ("Correlation Heatmap",
     "report_assets/correlation.png"),

    ("Histograms",
     "report_assets/histograms.png"),

    ("Boxplots",
     "report_assets/boxplots.png"),

    ("Missing Values",
     "report_assets/missing.png")

]

    found = False

    for title, path in images:

        if os.path.exists(path):

            found = True

            story.append(
                Paragraph(
                    f"<b>{title}</b>",
                    styles["Heading2"]
                )
            )

            story.append(Spacer(1,8))

            img = Image(
                path,
                width=6.5*inch,
                height=4*inch
            )

            story.append(img)

            story.append(Spacer(1,20))

    if not found:

        story.append(
            Paragraph(
                "No visualization images were found.",
                styles["BodyText"]
            )
        )

    story.append(PageBreak())


# =====================================================
# AI RECOMMENDATIONS
# =====================================================

def add_ai_recommendations(story):

    heading(story, "AI Recommendations")

    recommendations=[]

    if missing>0:
        recommendations.append(
            "• Handle missing values before training."
        )

    if duplicates>0:
        recommendations.append(
            "• Remove duplicate rows."
        )

    if numeric>0:
        recommendations.append(
            "• Scale numerical columns if using distance-based algorithms."
        )

    if categorical>0:
        recommendations.append(
            "• Encode categorical columns."
        )

    numeric_df=df.select_dtypes(include=np.number)

    if len(numeric_df.columns)>1:

        corr=numeric_df.corr().abs()

        if (corr.where(np.triu(np.ones(corr.shape),k=1).astype(bool))>0.90).sum().sum()>0:

            recommendations.append(
                "• Highly correlated features detected. Consider removing redundant features."
            )

    recommendations.extend([

        "• Perform Train-Test Split.",

        "• Use Cross Validation.",

        "• Standardize data for Logistic Regression and SVM.",

        "• Tree models generally require little preprocessing.",

        "• Evaluate multiple models before deployment."

    ])

    for rec in recommendations:

        story.append(
            Paragraph(
                rec,
                styles["BodyText"]
            )
        )

        story.append(Spacer(1,6))

    story.append(PageBreak())


# =====================================================
# MODEL RECOMMENDATION
# =====================================================

def add_model_recommendation(story):

    heading(story, "Recommended Machine Learning Models")

    if categorical==1:

        models=[

            "Logistic Regression",

            "Random Forest Classifier",

            "XGBoost Classifier",

            "Support Vector Machine",

            "Naive Bayes"

        ]

        problem="Classification"

    else:

        models=[

            "Linear Regression",

            "Random Forest Regressor",

            "XGBoost Regressor",

            "Gradient Boosting",

            "CatBoost"

        ]

        problem="Regression"

    story.append(
        Paragraph(
            f"<b>Detected Problem Type :</b> {problem}",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1,15))

    for model in models:

        story.append(
            Paragraph(
                "✔ "+model,
                styles["BodyText"]
            )
        )

        story.append(Spacer(1,5))

    story.append(PageBreak())


# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

def add_final_summary(story):

    heading(story,"Executive Summary")

    story.append(
        Paragraph(
            f"<b>Rows :</b> {rows}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Columns :</b> {cols}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Health Score :</b> {health_score}/100",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    if health_score>=90:

        color="green"

        msg="Excellent Dataset"

    elif health_score>=70:

        color="orange"

        msg="Good Dataset"

    else:

        color="red"

        msg="Needs Preprocessing"

    story.append(

        Paragraph(

            f"<font color='{color}' size=18><b>{msg}</b></font>",

            styles["Heading2"]

        )

    )

    story.append(Spacer(1,20))

    story.append(

        Paragraph(

            """
This report was automatically generated by MLDoctor.

The dataset was analyzed for:

• Dataset Structure

• Missing Values

• Duplicate Records

• Outliers

• Correlations

• Numeric Statistics

• Visualizations

• Machine Learning Readiness

• AI Recommendations

The dataset is now ready for further preprocessing and model training.
""",

            styles["BodyText"]

        )

    )

    story.append(PageBreak())

# =====================================================
# GENERATE PDF
# =====================================================

st.title("📄 Export Professional Report")

st.info(
    """
This report contains

• Dataset Summary

• Column Information

• Numeric Statistics

• Missing Value Analysis

• Duplicate Analysis

• Outlier Analysis

• Correlation Analysis

• Visualizations

• AI Recommendations

• Model Recommendations

• Executive Summary
"""
)

if st.button("📄 Generate Professional PDF Report", use_container_width=True):

    styles = getSampleStyleSheet()

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    doc = SimpleDocTemplate(
        temp.name
    )

    story = []

    # -------------------------------------------------
    # BUILD REPORT
    # -------------------------------------------------

    add_cover(story)

    add_summary(story)

    add_column_information(story)

    add_numeric_statistics(story)

    add_missing_analysis(story)

    add_duplicate_analysis(story)

    add_outlier_analysis(story)

    add_correlation_analysis(story)

    add_visualizations(story)

    add_ai_recommendations(story)

    add_model_recommendation(story)

    add_final_summary(story)

    # -------------------------------------------------
    # BUILD PDF
    # -------------------------------------------------

    doc.build(story)

    st.success("✅ PDF Report Generated Successfully!")

    with open(temp.name, "rb") as pdf:

        st.download_button(

            label="⬇ Download MLDoctor Report",

            data=pdf,

            file_name="MLDoctor_Report.pdf",

            mime="application/pdf",

            use_container_width=True

        )

    try:
        os.remove(temp.name)
    except:
        pass


# =====================================================
# PREVIEW
# =====================================================

st.divider()

st.subheader("📊 Dataset Preview")

st.dataframe(
    df.head(15),
    use_container_width=True
)

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric("Rows", rows)

c2.metric("Columns", cols)

c3.metric("Health Score", f"{health_score}/100")