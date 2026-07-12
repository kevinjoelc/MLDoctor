import pandas as pd

def check_correlation(df, threshold=0.8):
    """
    Finds highly correlated numerical columns.
    """

    numeric = df.select_dtypes(include="number")

    if numeric.shape[1] < 2:
        return {
            "high_correlation_pairs": [],
            "correlation_matrix": {}
        }

    corr = numeric.corr()

    pairs = []

    cols = corr.columns

    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):

            value = corr.iloc[i, j]

            if abs(value) >= threshold:
                pairs.append({
                    "column_1": cols[i],
                    "column_2": cols[j],
                    "correlation": round(float(value), 3)
                })

    return {
        "high_correlation_pairs": pairs,
        "correlation_matrix": corr.round(3).to_dict()
    }