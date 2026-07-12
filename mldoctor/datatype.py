import pandas as pd

def analyze_datatypes(df):
    """
    Analyze datatypes of every column.
    """

    return {
        "datatypes": df.dtypes.astype(str).to_dict(),
        "numeric_columns": list(df.select_dtypes(include="number").columns),
        "categorical_columns": list(df.select_dtypes(exclude="number").columns)
    }