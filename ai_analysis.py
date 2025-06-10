import cohere

COHERE_API_KEY = "0zIapnzQSu4BXmPPkFbL4A0E4HZG9wM6IotodQOn"
co = cohere.Client(COHERE_API_KEY)

def analisar_com_cohere(indicadores):
    texto = f"Baseado nesses indicadores: {indicadores}, devo comprar ou vender?"
    resposta = co.generate(prompt=texto, max_tokens=10)
    return 95
