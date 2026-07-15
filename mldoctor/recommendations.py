def generate_recommendations(report):
    recommendations = []

    # -------------------------------
    # Missing Values
    # -------------------------------
    missing = report["missing"]

    if missing["total_missing"] == 0:
        recommendations.append("✅ No missing values detected.")

    else:
        for column, percent in missing["missing_percentage"].items():

            if percent < 5:
                recommendations.append(
                    f"'{column}' has {percent}% missing values. Mean/Mode imputation is recommended."
                )

            elif percent < 30:
                recommendations.append(
                    f"'{column}' has {percent}% missing values. Median imputation is recommended."
                )

            elif percent < 60:
                recommendations.append(
                    f"'{column}' has {percent}% missing values. Consider advanced imputation techniques."
                )

            else:
                recommendations.append(
                    f"'{column}' has {percent}% missing values. Consider dropping this column."
                )

    # -------------------------------
    # Duplicate Rows
    # -------------------------------
    duplicates = report["duplicates"]["duplicates"]

    if duplicates == 0:
        recommendations.append("✅ No duplicate rows found.")

    else:
        recommendations.append(
            f"Dataset contains {duplicates} duplicate rows. Consider removing them."
        )

    # -------------------------------
    # Correlation
    # -------------------------------
    high_corr = report["correlation"]["high_correlation_pairs"]

    if len(high_corr) == 0:
        recommendations.append("✅ No highly correlated features detected.")

    else:
        for pair in high_corr:
            recommendations.append(
                f"'{pair['column_1']}' and '{pair['column_2']}' are highly correlated ({pair['correlation']}). Consider removing one of them."
            )

    # -------------------------------
    # Outliers
    # -------------------------------
    for column, info in report["outliers"].items():

        outliers = info["outliers"]

        if outliers == 0:
            continue

        elif outliers < 20:
            recommendations.append(
                f"'{column}' has {outliers} outliers. Review these values before training."
            )

        elif outliers < 100:
            recommendations.append(
                f"'{column}' has {outliers} outliers. RobustScaler or IQR filtering may help."
            )

        else:
            recommendations.append(
                f"'{column}' has {outliers} outliers. Investigate this feature before model training."
            )

    return recommendations