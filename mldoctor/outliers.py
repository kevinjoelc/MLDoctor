import pandas as pd

def detect_outliers(df):
    """
    Detect outliers using the IQR method.
    """

    numeric = df.select_dtypes(include="number")

    result = {}

    for col in numeric.columns:

        q1 = numeric[col].quantile(0.25)
        q3 = numeric[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        count = ((numeric[col] < lower) | (numeric[col] > upper)).sum()

        result[col] = {
            "outliers": int(count),
            "lower_limit": float(round(lower, 2)),
            "upper_limit": float(round(upper, 2))
        }

    return result