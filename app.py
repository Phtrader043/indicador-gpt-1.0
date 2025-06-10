import streamlit as st
import json
from signal_engine import gerar_sinal, validar_sinal
import datetime
import plotly.graph_objs as go

st.set_page_config(page_title="Indicador GPT 1.0", layout="wide")
st.title("📊 INDICADOR GPT 1.0")

if st.button("🚀 Gerar Sinal"):
    gerar_sinal()

validar_sinal()

try:
    with open("signals.json", "r") as f:
        historico = json.load(f)
except:
        historico = []

if historico:
    ultimo = historico[-1]
    st.subheader("📍 Sinal Atual")
    st.write(f"**Ativo:** {ultimo['ativo']}")
    st.write(f"**Tipo:** {ultimo['tipo']}")
    st.write(f"**Hora de Entrada:** {ultimo['entrada']}")
    st.write(f"**Hora de Saída:** {ultimo['saida']}")
    st.write(f"**Probabilidade:** {ultimo['probabilidade']}%")
    st.write(f"**Resultado:** {ultimo['resultado'] if ultimo['resultado'] else 'Aguardando...'}")

    st.subheader("📈 Estatísticas de Performance")
    wins = [s for s in historico if s["resultado"] == "WIN"]
    losses = [s for s in historico if s["resultado"] == "LOSS"]
    total = len(wins) + len(losses)

    if total > 0:
        acerto = round((len(wins) / total) * 100, 2)
        st.metric("Assertividade", f"{acerto}%")

        labels = ["WIN", "LOSS"]
        values = [len(wins), len(losses)]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
        fig.update_layout(title_text="Distribuição de Resultados")
        st.plotly_chart(fig, use_container_width=True)

        fig2 = go.Figure()
        resultados = [1 if s["resultado"] == "WIN" else 0 for s in historico if s["resultado"]]
        fig2.add_trace(go.Scatter(y=resultados, mode='lines+markers', name='Resultados', line=dict(color='green')))
        fig2.update_layout(yaxis=dict(title="1 = WIN, 0 = LOSS"), xaxis_title="Sinais", title="Linha do Tempo")
        st.plotly_chart(fig2, use_container_width=True)
