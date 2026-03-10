import streamlit as st
import pandas as pd
from database import conectar
from notas import criar_nota # Vamos precisar adaptar essa funcao para web depois

# Configura o titulo da aba no navegador
st.set_page_config(page_title="Sistema MD - Gestao", layout="wide")

# Barra lateral com o menu que voce desenhou
st.sidebar.image("https://via.placeholder.com/150", caption="MD Gestao") # Aqui voce colocara sua logo
menu = st.sidebar.selectbox("Ir para:", ["Dashboard", "Consultar Notas", "Cadastros", "Estoque"])

if menu == "Consultar Notas":
    st.title("Hub de Consultas - Notas Fiscais")
    
    # 1. Busca os dados do seu SQLite usando o Pandas
    conn = conectar()
    query = "SELECT * FROM notas"
    df = pd.read_sql_query(query, conn)
    conn.close()

    # 2. Campo de busca por nome do cliente (como voce pediu)
    busca = st.text_input("Buscar por nome do cliente")
    
    if busca:
        # Filtra o que o Pandas carregou
        df = df[df['cliente'].str.contains(busca, case=False)]

    # 3. Exibe a Grid (Tabela)
    st.dataframe(df, use_container_width=True)

    # 4. Botoes de Exportacao
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Exportar para Excel"):
            df.to_excel("relatorio_vendas.xlsx", index=False)
            st.success("Arquivo Excel gerado na pasta do projeto!")
            
    with col2:
        st.button("Gerar PDF de todas as notas") # Aqui chamaremos a fpdf2 depois
        