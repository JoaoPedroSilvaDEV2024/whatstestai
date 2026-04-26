import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="WhatsTest AI - QA Dashboard", layout="wide")

st.title("📊 WhatsTest AI - QA Dashboard")

# carregar dados
with open("app/results.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# métricas
total = len(df)
pass_count = len(df[df["status"] == "PASS"])
fail_count = len(df[df["status"] == "FAIL"])
accuracy = round((pass_count / total) * 100, 2)

col1, col2, col3 = st.columns(3)

col1.metric("Total Tests", total)
col2.metric("PASS", pass_count)
col3.metric("FAIL", fail_count)

st.metric("Accuracy", f"{accuracy}%")

st.divider()

# filtro
status_filter = st.selectbox("Filtrar status", ["ALL", "PASS", "FAIL"])

if status_filter != "ALL":
    df = df[df["status"] == status_filter]

st.dataframe(df, use_container_width=True)