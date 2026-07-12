# 🩺 MLDoctor

MLDoctor is an open-source Python package that automatically analyzes datasets before machine learning. It helps identify common data quality issues and provides preprocessing recommendations to improve model performance.

---

## 🚀 Features

- ✅ Missing Value Detection
- ✅ Duplicate Row Detection
- ✅ Data Type Analysis
- ✅ Correlation Analysis
- ✅ Outlier Detection (IQR Method)
- ✅ Automatic Dataset Recommendations
- ✅ JSON Report Generation
- ✅ Easy-to-use Python API

---

## 📦 Installation

Clone the repository and install locally:

```bash
git clone https://github.com/yourusername/mldoctor.git
cd mldoctor

pip install -e .
```

Or after publishing on PyPI:

```bash
pip install mldoctor
```

---

## 📖 Usage

```python
import pandas as pd
from mldoctor import analyze

# Load dataset
df = pd.read_csv("employee.csv")

# Analyze dataset
report = analyze(df)

# Print report
print(report)

# Save report
report.save_json("report.json")
```

---

## 📊 Example Output

```json
{
  "shape": [1000, 15],

  "missing": {
      "total_missing": 25,
      "columns_missing": {
          "Age": 10,
          "Salary": 15
      }
  },

  "duplicates": {
      "duplicates": 4
  },

  "datatypes": {
      "numeric_columns": [
          "Age",
          "Salary"
      ]
  },

  "recommendations": [
      "Dataset contains missing values.",
      "Duplicate rows detected."
  ]
}
```

---

## 📁 Project Structure

```
mldoctor/
│
├── mldoctor/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── missing.py
│   ├── duplicates.py
│   ├── datatype.py
│   ├── correlation.py
│   ├── outliers.py
│   ├── imbalance.py
│   ├── recommendations.py
│   ├── report.py
│   └── utils.py
│
├── examples/
│   ├── test_missing.py
│   └── test_analyze.py
│
├── tests/
│
├── README.md
├── LICENSE
├── requirements.txt
└── pyproject.toml
```

---

## 🧠 What MLDoctor Checks

### Missing Values
- Total missing values
- Missing values per column
- Missing percentage

### Duplicate Rows
- Total duplicate rows
- Duplicate row records

### Data Types
- Numeric columns
- Categorical columns
- Datatype summary

### Correlation
- Correlation matrix
- Highly correlated feature pairs

### Outliers
- IQR-based outlier detection
- Lower and upper limits
- Outlier count

### Recommendations
- Missing value handling
- Duplicate removal
- Feature correlation suggestions
- Outlier handling recommendations

---

## 📌 Example

```python
from mldoctor import analyze

report = analyze(df)

print(report)

report.save_json("report.json")
```

---

## 🛠 Built With

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## 📈 Roadmap

### Version 0.2
- Dataset Health Score
- Better recommendations

### Version 0.3
- HTML report generation
- Interactive charts

### Version 0.4
- Automatic preprocessing pipeline
- Missing value imputation suggestions

### Version 0.5
- Command Line Interface (CLI)

### Version 1.0
- Complete dataset profiling
- One-command dataset diagnosis
- PDF and HTML reports
- Feature importance suggestions

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Kevin Joel**

AI & Machine Learning Student

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

⭐ If you found this project useful, consider giving it a star on GitHub!