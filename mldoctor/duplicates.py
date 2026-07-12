def check_duplicates(df):

    duplicates = int(df.duplicated().sum())

    duplicate_rows = df[df.duplicated()].to_dict(orient="records")

    return {
        "duplicates": duplicates,
        "duplicate_rows": duplicate_rows
    }