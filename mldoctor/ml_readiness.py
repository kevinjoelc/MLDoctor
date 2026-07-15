def calculate_ml_readiness(report):

    score = 100

    # Missing Values
    score -= min(report["missing"]["total_missing"] / 20, 30)

    # Duplicates
    score -= min(report["duplicates"]["duplicates"] * 2, 10)

    # Outliers
    total_outliers = sum(
        value["outliers"]
        for value in report["outliers"].values()
    )

    score -= min(total_outliers / 20, 20)

    # High Correlation
    score -= len(report["correlation"]["high_correlation_pairs"]) * 5

    score = max(0, round(score))

    if score >= 90:
        status = "Ready"

    elif score >= 70:
        status = "Ready after preprocessing"

    elif score >= 50:
        status = "Needs preprocessing"

    else:
        status = "Not Ready"

    return {
        "score": score,
        "status": status
    }