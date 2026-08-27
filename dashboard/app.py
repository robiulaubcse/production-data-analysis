import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_sql("SELECT * FROM production_data", engine)

st.set_page_config(
    page_title="Production Performance Dashboard",
    layout="wide"
)

st.markdown("""
<style>

.main-title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 20px;
}

.kpi-label {
    font-size: 14px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)




st.markdown(
    '<div class="main-title">Production Performance Dashboard</div>',
    unsafe_allow_html=True
)

# KPI calculations

total_target = df["target_qty"].sum()
total_actual = df["actual_qty"].sum()
total_good = df["good_qty"].sum()
total_reject = df["reject_qty"].sum()
total_downtime = df["downtime_min"].sum()

achievement_pct = (total_actual / total_target) * 100
reject_rate_pct = (total_reject / total_actual) * 100


# KPI Cards

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Target",
    f"{total_target:,}"
)

col2.metric(
    "Actual",
    f"{total_actual:,}"
)

col3.metric(
    "Achievement",
    f"{achievement_pct:.2f}%"
)

col4.metric(
    "Reject Rate",
    f"{reject_rate_pct:.2f}%"
)

col5.metric(
    "Downtime",
    f"{total_downtime:,} min"
)



# Daily Production Trend

daily_production = (
    df.groupby("date")[["target_qty", "actual_qty"]]
    .sum()
    .reset_index()
)

daily_production["date"] = pd.to_datetime(daily_production["date"])

fig = px.line(
    daily_production,
    x="date",
    y=["target_qty", "actual_qty"],
    markers=True,
    title="Daily Target vs Actual Production"
)

st.plotly_chart(fig, use_container_width=True)





# Machine Performance

machine_performance = (
    df.groupby("machine")
    .agg(
        target_qty=("target_qty", "sum"),
        actual_qty=("actual_qty", "sum")
    )
    .reset_index()
)

machine_performance["achievement_pct"] = (
    machine_performance["actual_qty"]
    / machine_performance["target_qty"]
) * 100

fig = px.bar(
    machine_performance,
    x="machine",
    y="achievement_pct",
    title="Machine-wise Production Achievement",
    text="achievement_pct"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig.add_hline(
    y=100,
    line_dash="dash"
)

st.plotly_chart(fig, use_container_width=True)


# Shift Performance

shift_performance = (
    df.groupby("shift")
    .agg(
        target_qty=("target_qty", "sum"),
        actual_qty=("actual_qty", "sum")
    )
    .reset_index()
)

shift_performance["achievement_pct"] = (
    shift_performance["actual_qty"]
    / shift_performance["target_qty"]
) * 100

fig = px.line(
    shift_performance,
    x="shift",
    y="achievement_pct",
    markers=True,
    title="Shift-wise Production Achievement"
)

fig.update_traces(
    text=shift_performance["achievement_pct"].round(2),
    texttemplate="%{text:.2f}%",
    textposition="top center"
)

fig.add_hline(
    y=100,
    line_dash="dash"
)

st.plotly_chart(fig, use_container_width=True)