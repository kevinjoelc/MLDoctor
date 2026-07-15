
# 🩺 MLDoctor

> AI-Powered Dataset Diagnostic System built with Streamlit

MLDoctor is an intelligent web application that analyzes CSV datasets and provides detailed insights into data quality, preprocessing requirements, visualization, machine learning recommendations, and automated PDF reporting.

---

# 📸 Project Preview
<img width="1470" height="834" alt="home" src="https://github.com/user-attachments/assets/5c7f0e6f-82b9-458a-9f45-d29d6ef3f95c" />

---

# ✨ Features

## 📊 Dataset Health Analysis
<img width="1470" height="834" alt="dh2" src="https://github.com/user-attachments/assets/d2408ae6-013b-4356-9b63-0516c5b3206d" />

- Total rows and columns
- Dataset health score
- Missing value detection
- Duplicate detection
- Numeric & categorical feature count
- Memory usage analysis

---

## 🩹 Missing Value Analysis
<img width="1470" height="836" alt="mv3" src="https://github.com/user-attachments/assets/dd9cb7ce-7987-4fc1-bd28-2e37d01ee193" />

- Missing value count
- Missing percentage
- AI preprocessing suggestions
- Interactive visualizations

---

## 📈 Outlier Detection
<img width="1470" height="836" alt="out4" src="https://github.com/user-attachments/assets/04643ddf-c5de-4c75-81aa-f690d094309e" />

- IQR-based outlier detection
- Outlier percentage
- Boxplot visualization
- AI recommendations

---

## 🔗 Correlation Analysis
<img width="1470" height="836" alt="cor4" src="https://github.com/user-attachments/assets/c9482653-795f-485e-9096-78a824137965" />

- Correlation heatmap
- Highly correlated feature detection
- Correlation matrix
- Feature relationship analysis

---

## 🤖 AI Model Recommendation
<img width="1470" height="833" alt="aimod6" src="https://github.com/user-attachments/assets/6e477b3c-3844-41ae-ad1a-b2c030a14509" />

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
<img width="1470" height="835" alt="autoMl7" src="https://github.com/user-attachments/assets/8380a1cb-67d7-4aac-b78d-010010730634" />

Automatically prepares datasets for machine learning.

Includes:

- Missing value handling
- Duplicate removal
- Feature encoding
- Feature scaling
- Train/Test Split

---

## 📊 Interactive Visualizations
<img width="1470" height="835" alt="vis9" src="https://github.com/user-attachments/assets/e0b8f59f-f831-4994-a5cc-a8801e0c9abd" />

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
<img width="1470" height="836" alt="exp8" src="https://github.com/user-attachments/assets/925f1ef6-9ea6-42a6-a2c1-2a1ddacbeffd" />

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
