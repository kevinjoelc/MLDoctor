# 🩺 MLDoctor

> AI-Powered Dataset Diagnostic System built with Streamlit

MLDoctor is an intelligent web application that analyzes CSV datasets and provides detailed insights into data quality, preprocessing requirements, visualization, machine learning recommendations, and automated PDF reporting.

---

# 📸 Project Preview

<img src="dashboard/assets/logo.png" width="120">

---

# ✨ Features

## 📊 Dataset Health Analysis
- Total rows and columns
- Dataset health score
- Missing value detection
- Duplicate detection
- Numeric & categorical feature count
- Memory usage analysis

---

## 🩹 Missing Value Analysis

- Missing value count
- Missing percentage
- AI preprocessing suggestions
- Interactive visualizations

---

## 📈 Outlier Detection

- IQR-based outlier detection
- Outlier percentage
- Boxplot visualization
- AI recommendations

---

## 🔗 Correlation Analysis

- Correlation heatmap
- Highly correlated feature detection
- Correlation matrix
- Feature relationship analysis

---

## 🤖 AI Model Recommendation

Automatically detects whether the problem is:

- Classification
- Regression

Then recommends suitable machine learning algorithms.

Examples:

Classification

- Logistic Regression
- Random Forest
- XGBoost
- Support Vector Machine
- Naive Bayes

Regression

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- Decision Tree
- Support Vector Regression (SVR)

---

## 🚀 AutoML

Automatically prepares datasets for machine learning.

Includes:

- Missing value handling
- Duplicate removal
- Feature encoding
- Feature scaling
- Train/Test Split

---

## 📊 Interactive Visualizations

Supports multiple chart types:

- Histogram
- Scatter Plot
- Line Chart
- Box Plot
- Correlation Heatmap
- Pie Chart
- Bar Chart

Users can interactively choose dataset columns.

---

## 📄 Professional PDF Report

Generate a complete analysis report containing:

- Cover Page
- Dataset Summary
- Column Information
- Numeric Statistics
- Missing Value Analysis
- Outlier Analysis
- Correlation Analysis
- AI Recommendations
- Dataset Visualizations

---

# 🖥️ Tech Stack

Frontend

- Streamlit

Backend

- Python

Libraries

- Pandas
- NumPy
- Plotly
- Matplotlib
- Seaborn
- Scikit-Learn
- ReportLab

---

# 📂 Project Structure

```
MLDoctor/
│
├── dashboard/
│   ├── assets/
│   │    ├── logo.png
│   │    └── style.css
│   │
│   ├── pages/
│   │    ├── 1_Dataset_Health.py
│   │    ├── 2_Missing_Values.py
│   │    ├── 3_Outliers.py
│   │    ├── 4_Correlation.py
│   │    ├── 5_Recommendations.py
│   │    ├── 6_Model_Recommendation.py
│   │    ├── 7_AutoML.py
│   │    ├── 8_Export_Report.py
│   │    └── Visualizations.py
│   │
│   └── Home.py
│
├── report_assets/
├── reports/
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/MLDoctor.git
```

Go inside the project

```bash
cd MLDoctor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run dashboard/Home.py
```

---

# 📦 Required Packages

```text
streamlit
pandas
numpy
plotly
matplotlib
seaborn
scikit-learn
reportlab
openpyxl
```

---

# 🎯 Workflow

```text
Upload Dataset
        │
        ▼
Dataset Health Analysis
        │
        ▼
Missing Value Analysis
        │
        ▼
Outlier Detection
        │
        ▼
Correlation Analysis
        │
        ▼
Model Recommendation
        │
        ▼
AutoML
        │
        ▼
Interactive Visualizations
        │
        ▼
Generate Professional PDF Report
```

---

# 📊 Supported Dataset Format

- CSV (.csv)

Example datasets:

- Healthcare
- Finance
- Sales
- Marketing
- Student Performance
- Vehicle Dataset
- Weather Dataset

---

# 🚀 Future Improvements

- SQL Database Support
- Excel Dataset Support
- AI Chat Assistant
- Feature Importance Analysis
- SHAP Explainability
- Hyperparameter Optimization
- Deep Learning Models
- Cloud Deployment

---

# 👨‍💻 Author

**Kevin Joel**

Artificial Intelligence & Machine Learning Student

---

# 📜 License

This project is intended for educational and academic purposes.