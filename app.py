# Aula 2
# Criar um app
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise do Trabalho e Rendimento no Brasil", layout="wide")
st.title("Análise do Trabalho e Rendimento no Brasil")

st.write("""
        ### Integrantes ###

        *Rhyan Lopes da Silva Santos; Nicolas Prado Azevedo; Gustavo Henrik*.

        """)

# Upload do CSV
arquivo = st.file_uploader(
    "Envie um arquivo CSV",
    type=["csv"]
)

if arquivo is not None:

    df = pd.read_csv(arquivo)

    st.write("""
        *Este dashboard apresenta uma análise sobre o trabalho e o rendimento no Brasil.*

        *O objetivo é compreender como o rendimento médio e a massa de rendimentos
        evoluíram entre 2012 e 2025, utilizando dados do IBGE (PNAD Contínua).*

        *Por meio dos gráficos, podemos observar os períodos de crescimento,
        queda e as principais mudanças ocorridas ao longo dos anos.*
        """)
    
    # Visualização dos dados
    st.subheader("Visualização dos dados")
    st.dataframe(df, use_container_width=True)

    col1, col2 = st.columns(2)
    col1.metric("Quantidade de registros", df.shape[0])
    col2.metric("Quantidade de colunas", df.shape[1])

    # Verificação de dados limpa
    st.subheader("Verificação dos dados")
    col_null, col_dup = st.columns([2, 1])

    with col_null:
        st.write("**Valores ausentes:**")
        st.dataframe(
            df.isnull().sum().reset_index().rename(columns={"index": "Coluna", 0: "Ausentes"}),
            hide_index=True,
            use_container_width=True
        )

        st.subheader("Registros duplicados")
        col_null, col_dup = st.columns([2, 1])
        st.metric("", df.duplicated().sum())

    # Tratamentos necessários
    st.subheader("Tratamentos necessários")
    df["Ano"] = pd.to_numeric(
        df["Ano"],
        errors="coerce"
    )

    df["Massa de rendimentos (R$ milhões)"] = pd.to_numeric(
        df["Massa de rendimentos (R$ milhões)"],
        errors="coerce"
    )

    df["Variação da massa de rendimentos (%)"] = pd.to_numeric(
        df["Variação da massa de rendimentos (%)"],
        errors="coerce"
    )

    df["Rendimento médio (R$)"] = pd.to_numeric(
        df["Rendimento médio (R$)"],
        errors="coerce"
    )

    df["Variação do rendimento (%)"] = pd.to_numeric(
        df["Variação do rendimento (%)"],
        errors="coerce"
    )

    # Aula 3
    # Gráfico 1
    # ===== GRÁFICO 1 =====
    st.subheader("1. Evolução do Rendimento Médio Real")
   
    fig1 = px.line(
        df,
        x="Ano",
        y="Rendimento médio (R$)",
        markers=True,
        title="Rendimento Médio Real (R$) - 2012 a 2025"
    )
   
    fig1.update_layout(
        xaxis_title="Ano",
        yaxis_title="Rendimento Médio (R$)"
    )
   
    st.plotly_chart(fig1, use_container_width=True)
 
    st.markdown("""
        <div style="background-color: #e8f1fb; padding: 15px; border-radius: 5px;">
 
        <p style="font-size: 16px; color: #0066cc;">
        <b>O que podemos observar?</b>
        </p>
 
        <p style="font-size: 16px; color: #0066cc;">
        O gráfico apresenta a evolução do rendimento médio real das pessoas ocupadas
        no Brasil entre 2012 e 2025.
        </p>
        
        <p style="font-size: 16px; color: #0066cc;">
        Ao longo desse período, o rendimento passou de
        <span style="font-size: 16px;">R$ 3.114</span> em 2012 para
        <span style="font-size: 16px;">R$ 3.694</span> em 2025, mostrando um crescimento
        no valor recebido.
        </p>
        
        <p style="font-size: 16px; color: #0066cc;">
        Entre 2019 e 2022, foram observadas algumas reduções no rendimento.
        </p>
        
        <p style="font-size: 16px; color: #0066cc;">
        A partir de 2023, o rendimento voltou a crescer e atingiu, em 2025,
        o maior valor registrado em toda a série analisada.
        </p>
        
        </div>
        """, unsafe_allow_html=True)
 
# Gráfico 2
    st.subheader("Variação anual da massa de rendimentos")

    fig2 = px.bar(
        df.dropna(subset=["Variação da massa de rendimentos (%)"]),
        x="Ano",
        y="Variação da massa de rendimentos (%)",
        title="Variação anual da massa de rendimentos (%)"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.info("""
        ### O que podemos observar?

        A **massa de rendimentos** representa o total recebido pelas pessoas ocupadas
        em determinado mês.

        Em **2020**, ocorreu a maior queda, de **10,0%**.

        Em **2023**, aconteceu a maior alta, de **11,4%**.

        Em **2025**, a massa de rendimentos chegou a aproximadamente
        **R$ 375,4 bilhões**.
        """)

#Indicador númerico
    ultimo = df.sort_values("Ano").iloc[-1]
    st.metric(
        "Rendimento médio em 2025",
        f"R$ {int(ultimo['Rendimento médio (R$)'])}",
        f"{ultimo['Variação do rendimento (%)']}% no Ano"
    )

    st.info("""
        ### Nossa investigação

        **O que investigamos?**

        *R- Trabalho e rendimento no Brasil; como o rendimento médio mudou e em quais anos a massa mais subiu ou caiu.*

        **Qual base?**

        *R- IBGE, PNAD Contínua, 2012–2025.*

        **O que os dados mostraram?**

        *R- Rendimento médio foi a R$ 3.694 em 2025; maior queda da massa em 2020; maior alta em 2023.*

        **Onde a IA ajudou?**

        *R- Na escolha dos gráficos e no texto das explicações. Nós conferimos os números.*
        """)

    #Explicação dos gráficos
    st.info("""
        ### Sobre o Dashboard

        Este dashboard apresenta a evolução do **trabalho e do rendimento no Brasil**
        entre **2012 e 2025**.

        Os dados do **IBGE (PNAD Contínua)** permitem analisar o comportamento do
        **rendimento médio real** e da **massa de rendimentos** ao longo desse período.

        Os gráficos facilitam a visualização das variações e ajudam a compreender
        como os rendimentos se comportaram ao longo dos anos.
        """)