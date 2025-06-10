import datetime
import json
from indicators import calcular_indicadores
from ai_analysis import analisar_com_cohere
from data_sources.cryptocompare import get_crypto_data
from data_sources.twelvedata import get_forex_data

def gerar_sinal():
    agora = datetime.datetime.now()
    hora_entrada = agora.strftime("%H:%M:%S")
    hora_saida = (agora + datetime.timedelta(minutes=1)).strftime("%H:%M:%S")

    ativo = "BTC"
    tipo = "COMPRA"
    tipo_ativo = "CRYPTO"

    indicadores = calcular_indicadores(ativo, tipo_ativo)
    score_ia = analisar_com_cohere(indicadores)

    score_final = score_ia
    if score_final < 90:
        return

    if tipo_ativo == "CRYPTO":
        preco_entrada = float(get_crypto_data(symbol=ativo)[-1]["close"])
    else:
        preco_entrada = float(get_forex_data(pair=ativo)[-1]["close"])

    sinal = {
        "ativo": ativo,
        "tipo": tipo,
        "entrada": hora_entrada,
        "saida": hora_saida,
        "probabilidade": score_final,
        "resultado": "",
        "preco_entrada": preco_entrada,
        "tipo_ativo": tipo_ativo
    }

    try:
        with open("signals.json", "r") as f:
            sinais = json.load(f)
    except:
        sinais = []

    sinais.append(sinal)
    with open("signals.json", "w") as f:
        json.dump(sinais, f, indent=2)

def validar_sinal():
    try:
        with open("signals.json", "r") as f:
            sinais = json.load(f)
    except:
        return

    if not sinais:
        return

    sinal = sinais[-1]
    if sinal["resultado"]:
        return

    hora_saida = datetime.datetime.strptime(sinal["saida"], "%H:%M:%S").time()
    agora = datetime.datetime.now().time()

    if agora > hora_saida:
        ativo = sinal["ativo"]
        tipo = sinal["tipo"]
        tipo_ativo = sinal.get("tipo_ativo", "CRYPTO")
        preco_entrada = float(sinal.get("preco_entrada", 0))

        if tipo_ativo == "CRYPTO":
            dados = get_crypto_data(symbol=ativo, limit=1)
            preco_final = float(dados[-1]["close"])
        else:
            dados = get_forex_data(pair=ativo)
            preco_final = float(dados[-1]["close"])

        if tipo == "COMPRA":
            resultado = "WIN" if preco_final > preco_entrada else "LOSS"
        else:
            resultado = "WIN" if preco_final < preco_entrada else "LOSS"

        sinal["resultado"] = resultado
        sinais[-1] = sinal

        with open("signals.json", "w") as f:
            json.dump(sinais, f, indent=2)
