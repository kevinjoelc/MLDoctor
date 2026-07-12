def generate_recommendations(report):

    recommendations = []


    if report["missing"]["total_missing"] > 0:
        recommendations.append(
            "Dataset contains missing values. Consider imputation or removal."
        )


    if report["duplicates"]["duplicates"] > 0:
        recommendations.append(
            "Duplicate rows detected. Remove duplicate records."
        )

    if len(report["correlation"]["high_correlation_pairs"]) > 0:
        recommendations.append(
            "Highly correlated features found. Consider removing one of them."
        )

    for col, info in report["outliers"].items():
        if info["outliers"] > 0:
            recommendations.append(
                f"{col} contains {info['outliers']} outliers."
            )

    return recommendations