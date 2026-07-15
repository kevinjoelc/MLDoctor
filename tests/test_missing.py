import pandas as pd
from mldoctor.missing import check_missing

def test_check_missing():
    df = pd.DataFrame({
        "A": [1, None, 3],
        "B": [None, 5, 6]
    })

    result = check_missing(df)

    assert result["total_missing"] == 2
    assert result["columns_missing"]["A"] == 1
    assert result["columns_missing"]["B"] == 1