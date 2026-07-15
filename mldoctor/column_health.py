def analyze_column_health(df, report):
    result = []

    missing = report["missing"]["columns_missing"]
    dtypes = report["datatypes"]["datatypes"]
    outliers = report["outliers"]

    for column in df.columns:

        score = 100
        issues = []

        # Missing values
        if column in missing:
            miss = report["missing"]["missing_percentage"][column]

            if miss > 50:
                score -= 50
                issues.append("High Missing")

            elif miss > 20:
                score -= 30
                issues.append("Missing Values")

            elif miss > 0:
                score -= 10
                issues.append("Few Missing")

        # Outliers
        if column in outliers:
            count = outliers[column]["outliers"]

            if count > 100:
                score -= 30
                issues.append("Many Outliers")

            elif count > 20:
                score -= 15
                issues.append("Outliers")

        # Data type
        dtype = dtypes[column]

        if dtype == "str":
            score -= 10
            issues.append("Categorical")

        # Status
        if score >= 90:
            status = "Excellent"

        elif score >= 75:
            status = "Good"

        elif score >= 50:
            status = "Fair"

        else:
            status = "Poor"

        result.append({
            "column": column,
            "score": score,
            "status": status,
            "issues": ", ".join(issues) if issues else "None"
        })

    return result