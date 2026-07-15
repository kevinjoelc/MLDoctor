import pandas as pd


def detect_features(df):
    result = {}

    total_rows = len(df)

    for column in df.columns:

        info = []

        # ID column
        if df[column].nunique() == total_rows:
            info.append("ID Column")

        # Constant column
        if df[column].nunique() == 1:
            info.append("Constant Column")

        # Numeric
        if pd.api.types.is_numeric_dtype(df[column]):
            info.append("Numeric")

        # Categorical
        else:
            info.append("Categorical")

        # Date column
        if "date" in column.lower() or "time" in column.lower():
            info.append("Date/Time")

        # High cardinality
        if df[column].dtype == object:
            if df[column].nunique() > 50:
                info.append("High Cardinality")

        result[column] = info

    return result