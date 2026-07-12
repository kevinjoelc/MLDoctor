from .missing import check_missing
from .duplicates import check_duplicates
from .datatype import analyze_datatypes
from .correlation import check_correlation
from .outliers import detect_outliers
from .recommendations import generate_recommendations
from .report import Report

def analyze(df):
    report={}
    report["shape"]=df.shape
    report["missing"]=check_missing(df)
    report["duplicates"]=check_duplicates(df)
    report["datatypes"]=analyze_datatypes(df)
    report["correlation"]=check_correlation(df)
    report["outliers"]=detect_outliers(df)
    report["recommendations"]=generate_recommendations(report)
    return Report(report)