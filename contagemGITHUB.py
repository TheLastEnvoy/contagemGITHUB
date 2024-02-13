import requests
import streamlit as st
import matplotlib.pyplot as plt

def contar_arquivos_sharepoint(site_url, caminho):
    # URL base da API do SharePoint
    base_url = f"{site_url}/_api/web/GetFolderByServerRelativeUrl('{caminho}')/Files"

    # Autenticação básica (substitua com suas credenciais)
    user = "seu_usuario"
    password = "sua_senha"
    auth = (user, password)

    # Fazendo a solicitação GET para obter a lista de arquivos
    response = requests.get(base_url, auth=auth)
    files = response.json()

    contagem_total = len(files['value'])
    contagem_por_trecho = {file['Name']: 1 for file in files['value']}

    return contagem_total, contagem_por_trecho

# Definindo o site do SharePoint e o caminho do diretório
site_url = "https://<seu_site_sharepoint>"
caminho = "<caminho_do_diretorio>"

# Obtendo contagem total e contagem por trecho
contagem_total, contagem_por_trecho = contar_arquivos_sharepoint(site_url, caminho)

# Exibindo no dashboard
st.title("Quantidade de arquivos no diretório do SharePoint")
st.write(f"Total de arquivos: {contagem_total}")

st.subheader("Arquivos:")
for trecho, contagem in contagem_por_trecho.items():
    st.write(f"{trecho}: {contagem}")

# Criando gráfico de pizza
fig, ax = plt.subplots()
labels = contagem_por_trecho.keys()
sizes = contagem_por_trecho.values()
colors = plt.cm.tab20c.colors[:len(labels)]

wedges, texts, autotexts = ax.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85, explode=[0.05] * len(labels))

ax.set_title("Distribuição dos arquivos", pad=20)

# Adicionando legenda
ax.legend(wedges, labels, title="Arquivos", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

st.pyplot(fig)
