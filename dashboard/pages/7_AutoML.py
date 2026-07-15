import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score

from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
import streamlit as st

if "df" not in st.session_state:
    st.warning("📁 Please upload a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
# ----------------------------

st.set_page_config(
    page_title="AutoML",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AutoML")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

uploaded_file = st.session_state.get("uploaded_file")

if uploaded_file is None:
    st.warning("⚠ Please upload a dataset from the Home page.")
    st.stop()

uploaded_file.seek(0)
df = pd.read_csv(uploaded_file)

target = st.selectbox(
    "Select Target Column",
    df.columns
)

# ---------------------------------

X = df.drop(columns=[target])

y = df[target]

# Encode categorical columns

for col in X.select_dtypes(include="object"):

    le = LabelEncoder()

    X[col] = le.fit_transform(X[col].astype(str))

# Encode target if classification

from pandas.api.types import is_numeric_dtype

# Detect problem type
if is_numeric_dtype(y):
    if y.nunique() <= 10:
        problem = "Classification"
    else:
        problem = "Regression"
else:
    problem = "Classification"
    le = LabelEncoder()
    y = le.fit_transform(y.astype(str))


X = X.fillna(0)

# Make sure all features are numeric
X = X.apply(pd.to_numeric, errors="coerce").fillna(0)

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)

results = []

# ---------------------------------

if problem == "Classification":

    models = {

        "Logistic Regression": LogisticRegression(max_iter=1000),

        "Decision Tree": DecisionTreeClassifier(),

        "Random Forest": RandomForestClassifier()

    }

    for name, model in models.items():

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        score = accuracy_score(y_test, pred)

        results.append([name, round(score * 100, 2)])

else:

    models = {

        "Linear Regression": LinearRegression(),

        "Decision Tree": DecisionTreeRegressor(),

        "Random Forest": RandomForestRegressor()

    }

    for name, model in models.items():

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        score = r2_score(y_test, pred)

        results.append([name, round(score, 3)])

# ---------------------------------

result = pd.DataFrame(

    results,

    columns=[

        "Model",

        "Score"

    ]

)

result = result.sort_values(

    "Score",

    ascending=False

)

st.success(f"Detected Problem : {problem}")

st.dataframe(

    result,

    use_container_width=True

)

winner = result.iloc[0]

st.balloons()

st.success(

    f"🏆 Best Model : {winner['Model']}"

)

st.metric(

    "Best Score",

    winner["Score"]

)