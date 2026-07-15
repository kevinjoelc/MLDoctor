import pandas as pd


def generate_preprocessing_plan(df, report):

    plan = []

    # -------------------------------
    # Missing Values
    # -------------------------------

    missing = report["missing"]["missing_percentage"]

    for column, percent in missing.items():

        if percent < 5:
            plan.append({
                "column": column,
                "action": "Mean/Mode Imputation",
                "reason": f"{percent}% missing values"
            })

        elif percent < 30:
            plan.append({
                "column": column,
                "action": "Median Imputation",
                "reason": f"{percent}% missing values"
            })

        elif percent < 60:
            plan.append({
                "column": column,
                "action": "Advanced Imputation",
                "reason": f"{percent}% missing values"
            })

        else:
            plan.append({
                "column": column,
                "action": "Drop Column",
                "reason": f"{percent}% missing values"
            })

    # -------------------------------
    # Duplicate Rows
    # -------------------------------

    duplicates = report["duplicates"]["duplicates"]

    if duplicates > 0:

        plan.append({
            "column": "Dataset",
            "action": "Remove Duplicate Rows",
            "reason": f"{duplicates} duplicate rows"
        })

    # -------------------------------
    # Highly Correlated Features
    # -------------------------------

    for pair in report["correlation"]["high_correlation_pairs"]:

        plan.append({
            "column": pair["column_2"],
            "action": "Remove One Correlated Feature",
            "reason": f"Correlation = {pair['correlation']}"
        })

    # -------------------------------
    # Outliers
    # -------------------------------

    for column, values in report["outliers"].items():

        if values["outliers"] > 0:

            plan.append({
                "column": column,
                "action": "Review Outliers / Use RobustScaler",
                "reason": f"{values['outliers']} outliers"
            })

    # -------------------------------
    # Categorical Columns
    # -------------------------------

    for column in report["datatypes"]["categorical_columns"]:

        plan.append({
            "column": column,
            "action": "Encode Categorical Feature",
            "reason": "Required before most ML models"
        })

    return plan