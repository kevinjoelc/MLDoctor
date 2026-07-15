import pandas as pd
from mldoctor import analyze

df = pd.read_csv("/Users/kevinjoel/MODEL/Datasets/titanic.csv")

report = analyze(
    df,
    target="Survived"
)

print(report)

report.save_json()

report.save_html()