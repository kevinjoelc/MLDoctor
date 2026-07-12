import pandas as pd
from mldoctor import analyze

df = pd.read_csv("/Users/kevinjoel/MODEL/Datasets/fiat500.csv")

report = analyze(df)

print(report)

report.save_json()

report.save_html()