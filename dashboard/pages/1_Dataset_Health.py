import streamlit as st
import pandas as pd
import plotly.graph_objects as go


if "df" not in st.session_state:
    st.warning("📁 Please upload a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
# ---------------- Page ---------------- #

st.set_page_config(
    page_title="Dataset Health",
    page_icon="📊",
    layout="wide"
)

# ---------------- CSS ---------------- #

with open("dashboard/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- Title ---------------- #

st.title("📊 Dataset Health")

st.caption("Analyze the overall quality of your dataset")

st.divider()

# ---------------- Upload ---------------- #

uuploaded_file = st.session_state.get("uploaded_file")

# Get dataset from session
df = st.session_state.get("df", None)

if df is None:
    st.warning("📁 Please upload a dataset from the Home page.")
    st.stop()

# ---------------- Statistics ---------------- #

rows = df.shape[0]
cols = df.shape[1]

missing = df.isna().sum().sum()

duplicates = df.duplicated().sum()

numeric = len(df.select_dtypes(include="number").columns)

categorical = len(df.select_dtypes(exclude="number").columns)

memory = round(df.memory_usage().sum()/1024,2)

# ---------------- Health Score ---------------- #

health = 100

health -= min(30,(missing/(rows*cols))*100)

health -= min(20,(duplicates/rows)*100)

health = max(0,round(health))

# ---------------- KPI ---------------- #

c1,c2,c3,c4,c5,c6 = st.columns(6)

c1.metric("Rows",rows)

c2.metric("Columns",cols)

c3.metric("Missing",missing)

c4.metric("Duplicates",duplicates)

c5.metric("Numeric",numeric)

c6.metric("Categorical",categorical)

st.divider()

# ---------------- Gauge ---------------- #

left,right=st.columns([1,2])

with left:

    fig=go.Figure(go.Indicator(

        mode="gauge+number",

        value=health,

        title={"text":"Health Score"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":"royalblue"},

            "steps":[

                {"range":[0,50],"color":"#ffb3b3"},

                {"range":[50,80],"color":"#ffe699"},

                {"range":[80,100],"color":"#b6f2b6"}

            ]

        }

    ))

    fig.update_layout(height=350)

    st.plotly_chart(fig,use_container_width=True)

with right:

    st.subheader("Dataset Summary")

    st.write(f"**Rows :** {rows:,}")

    st.write(f"**Columns :** {cols}")

    st.write(f"**Missing Values :** {missing}")

    st.write(f"**Duplicate Rows :** {duplicates}")

    st.write(f"**Memory Usage :** {memory} KB")

    st.progress(health/100)

    if health>=90:
        st.success("Excellent dataset")

    elif health>=70:
        st.warning("Dataset needs preprocessing")

    else:
        st.error("Poor quality dataset")

st.divider()

# ---------------- Column Information ---------------- #

st.subheader("Column Information")

info=pd.DataFrame({

    "Column":df.columns,

    "Datatype":df.dtypes.astype(str),

    "Missing":df.isna().sum(),

    "Unique":df.nunique()

})

st.dataframe(

    info,

    use_container_width=True,

    height=500

)