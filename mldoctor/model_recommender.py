import pandas as pd


def recommend_models(df, report, target=None):

    recommendations = []

    if target is None:
        return {
            "task": "Unknown",
            "recommended_models": [],
            "reason": "Target column not provided."
        }

    if target not in df.columns:
        return {
            "task": "Unknown",
            "recommended_models": [],
            "reason": "Target column not found."
        }

    target_column = df[target]

    # -----------------------
    # Detect Task
    # -----------------------

    if pd.api.types.is_numeric_dtype(target_column):

        unique = target_column.nunique()

        if unique <= 10:

            task = "Classification"

        else:

            task = "Regression"

    else:

        task = "Classification"

    # -----------------------
    # Recommend Models
    # -----------------------

    if task == "Classification":

        recommendations = [
            "Random Forest",
            "XGBoost",
            "Logistic Regression",
            "Support Vector Machine",
            "LightGBM"
        ]

    else:

        recommendations = [
            "Random Forest Regressor",
            "XGBoost Regressor",
            "Linear Regression",
            "Ridge Regression",
            "CatBoost Regressor"
        ]

    return {
        "task": task,
        "recommended_models": recommendations,
        "reason": "Recommendations based on detected prediction task."
    }