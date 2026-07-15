import pandas as pd
from mldoctor.duplicates import check_duplicates

def test_check_duplicates():
    df = pd.DataFrame({
        "A": [1, 2, 2],
        "B": [3, 4, 4]
    })

    result = check_duplicates(df)

    assert result["duplicates"] == 1
    assert len(result["duplicate_rows"]) == 1