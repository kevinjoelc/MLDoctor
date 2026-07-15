def calculate_health(report):

    score = 100

    # Missing values penalty
    total_missing = report["missing"]["total_missing"]
    score -= min(total_missing // 20, 20)

    # Duplicate penalty
    duplicates = report["duplicates"]["duplicates"]
    score -= min(duplicates * 2, 10)

    # Correlation penalty
    high_corr = len(report["correlation"]["high_correlation_pairs"])
    score -= min(high_corr * 5, 15)

    # Outlier penalty
    total_outliers = 0

    for value in report["outliers"].values():
        total_outliers += value["outliers"]

    score -= min(total_outliers // 20, 20)

    score = max(score, 0)

    if score >= 90:
        status = "Excellent"
        color = "green"

    elif score >= 75:
        status = "Good"
        color = "orange"

    elif score >= 50:
        status = "Fair"
        color = "darkorange"

    else:
        status = "Poor"
        color = "red"

    return {
        "score": score,
        "status": status,
        "color": color
    }