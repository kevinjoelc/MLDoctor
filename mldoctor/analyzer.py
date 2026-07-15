from .missing import check_missing
from .duplicates import check_duplicates
from .datatype import analyze_datatypes
from .correlation import check_correlation
from .outliers import detect_outliers
from .recommendations import generate_recommendations
from .report import Report
from .visualizer import Visualizer
from .health import calculate_health
from .column_health import analyze_column_health
from .feature_detector import detect_features
from .preprocessing import generate_preprocessing_plan
from .model_recommender import recommend_models
from .ml_readiness import calculate_ml_readiness
from .column_health import analyze_column_health

def analyze(df, target=None):

    report = {}

    # Basic Analysis
    report["shape"] = df.shape
    report["missing"] = check_missing(df)
    report["duplicates"] = check_duplicates(df)
    report["datatypes"] = analyze_datatypes(df)
    report["correlation"] = check_correlation(df)
    report["outliers"] = detect_outliers(df)

    # Recommendations
    report["recommendations"] = generate_recommendations(report)

    # Health
    report["health"] = calculate_health(report)

    # Column Health
    report["column_health"] = analyze_column_health(df, report)

    # Feature Detection
    report["feature_types"] = detect_features(df)

    # Preprocessing Plan
    report["preprocessing_plan"] = generate_preprocessing_plan(df, report)

    # Model Recommendation
    report["model_recommendation"] = recommend_models(
        df,
        report,
        target
    )

    report["ml_readiness"] = calculate_ml_readiness(report)

    # Generate Charts
    Visualizer(df).generate()

    return Report(report)