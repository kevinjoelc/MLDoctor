import pandas as pd
from mldoctor.outliers import detect_outliers

def test_detect_outliers():
    df = pd.DataFrame({
        "A": [10, 11, 12, 13, 100],
        "B": [5, 6, 7, 8, 9]
    })

    result = detect_outliers(df)

    assert result["A"]["outliers"] == 1
    assert result["B"]["outliers"] == 0