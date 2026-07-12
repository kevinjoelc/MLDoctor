import pandas as pd

def check_missing(df):
    total = int(df.isnull().sum().sum())

    column_missing = (
        df.isnull()
        .sum()
        .loc[lambda x: x > 0]
        .to_dict()
    )

    percent = (
        (df.isnull().sum()/len(df))*100
    ).round(2)

    percent = percent.loc[percent>0].to_dict()

    return {
        "total_missing": total,
        "columns_missing": column_missing,
        "missing_percentage": percent
    }