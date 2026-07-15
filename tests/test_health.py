from mldoctor.health import calculate_health

def test_calculate_health():
    report = {
        "missing": {
            "total_missing": 0
        },
        "duplicates": {
            "duplicates": 0
        },
        "correlation": {
            "high_correlation_pairs": []
        },
        "outliers": {}
    }

    result = calculate_health(report)

    assert result["score"] == 100
    assert result["status"] == "Excellent"