import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import os

API_KEY = os.getenv("API_KEY")
API_URL = "http://api:8000"
HEADERS = {"X-API-Key": API_KEY}

st.title("Sensor Hub - Visualização e Cadastro")

# 🔧 Criar novo dispositivo
st.subheader("📌 Cadastro de Dispositivo")
with st.form("create_device_form"):
    new_name = st.text_input("Nome do novo dispositivo")
    submitted = st.form_submit_button("Criar dispositivo")
    if submitted and new_name.strip():
        resp = requests.post(f"{API_URL}/devices/", json={"name": new_name}, headers=HEADERS)
        if resp.status_code == 200:
            st.success(f"Dispositivo '{new_name}' criado com sucesso!")
            #st.experimental_rerun()
        else:
            st.error("Erro ao criar dispositivo.")

# 🔍 Buscar dispositivos
def listar_dispositivos():
    res = requests.get(f"{API_URL}/devices/", headers=HEADERS)
    if res.status_code == 200:
        return res.json()
    else:
        st.error("Erro ao buscar dispositivos.")
        return []

dispositivos = listar_dispositivos()
nomes = [f"{d['id']} - {d['name']}" for d in dispositivos]

st.subheader("📊 Consulta de Leituras")
if dispositivos:
    idx = st.selectbox("Selecione um dispositivo", options=range(len(nomes)), format_func=lambda i: nomes[i])
    device_id = dispositivos[idx]["id"]
else:
    st.warning("Nenhum dispositivo cadastrado.")
    st.stop()

@st.cache_data(show_spinner=False)
def get_metrics(device_id):
    r = requests.get(f"{API_URL}/metrics/", params={"device_id": device_id}, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return []

metricas = get_metrics(device_id)
if metricas:
    metric = st.selectbox("Métrica disponível", metricas)
else:
    st.warning("Nenhuma métrica encontrada para este dispositivo.")
    st.stop()

start = st.date_input("Data inicial")
end = st.date_input("Data final")
limit = st.number_input("Limite", min_value=1, max_value=1000, value=100)
group_by_day = st.checkbox("Agrupar por dia")

if st.button("Consultar leituras"):
    params = {
        "device_id": device_id,
        "metric": metric,
        "start": f"{start}T00:00:00",
        "end": f"{end}T23:59:59",
        "limit": limit
    }
    res = requests.get(f"{API_URL}/readings/", params=params, headers=HEADERS)
    if res.status_code == 200:
        df = pd.DataFrame(res.json())
        if df.empty:
            st.info("Nenhum dado encontrado.")
        else:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            if group_by_day:
                df["date"] = df["timestamp"].dt.date
                df = df.groupby("date")["value"].mean().reset_index()
                st.dataframe(df)
                st.plotly_chart(px.line(df, x="date", y="value", title=f"Média diária: {metric}"))
            else:
                st.dataframe(df)
                st.plotly_chart(px.line(df, x="timestamp", y="value", title=f"Métrica: {metric}"))
            st.download_button("⬇️ Exportar CSV", df.to_csv(index=False), file_name="leituras.csv", mime="text/csv")
    else:
        st.error(f"Erro {res.status_code}: {res.text}")

