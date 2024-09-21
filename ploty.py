import pandas as pd
import plotly.express as px
from collections import Counter


def grafico_10(caminho_arquivo):
    # Carregar o arquivo CSV
    # Altere o caminho 'caminho_do_arquivo.csv' para o local correto do seu arquivo
    df = pd.read_csv(caminho_arquivo)

    # Contar os 10 odores mais frequentes na coluna 'descrição'
    top_10_odor_count = Counter(df['Descrição']).most_common(10)

    # Criar um novo DataFrame com os 10 odores mais frequentes
    top_10_df = pd.DataFrame(top_10_odor_count, columns=['Descrição', 'frequencia'])

    # Criar o histograma com uma escala de cor de tons de azul, fundo preto, barras grandes e sem grade
    fig = px.bar(
        top_10_df,
        x='Descrição',
        y='frequencia',
        color='frequencia',
        color_continuous_scale='Blues',  # Escala de cor de tons de azul
        title='Top 10 sub odores do dataset de validação',
        labels={'Descrição': 'Odor', 'frequencia': 'Frequência'}
    )

    # Atualizar o layout do gráfico
    fig.update_layout(
        plot_bgcolor='black',  # Fundo do gráfico preto
        paper_bgcolor='black',  # Fundo do papel preto
        font_color='white',     # Cor da fonte branca para contraste
        xaxis=dict(
            showgrid=False,
            tickangle=-45,  # Inclinar os rótulos do eixo x para melhor legibilidade
        ),
        yaxis=dict(showgrid=False),
        bargap=0.2,  # Ajustar o espaço entre as barras
        xaxis_title='Odores',
        yaxis_title='Frequência'
    )

    # Aumentar o tamanho das barras
    fig.update_traces(marker=dict(line=dict(width=2, color='white')))

    # Exibir o gráfico
    fig.show()

def grafico_50(caminho_arquivo):
    # Carregar o arquivo CSV
    # Altere o caminho 'caminho_do_arquivo.csv' para o local correto do seu arquivo
    df = pd.read_csv(caminho_arquivo)

    # Contar os 10 odores mais frequentes na coluna 'descrição'
    top_10_odor_count = Counter(df['Descrição']).most_common(50)

    # Criar um novo DataFrame com os 10 odores mais frequentes
    top_10_df = pd.DataFrame(top_10_odor_count, columns=['Descrição', 'frequencia'])

    # Criar o histograma com uma escala de cor de tons de azul, fundo preto, barras grandes e sem grade
    fig = px.bar(
        top_10_df,
        x='Descrição',
        y='frequencia',
        color='frequencia',
        color_continuous_scale='Blues',  # Escala de cor de tons de azul
        title='Top 50 sub odores do dataset de validação',
        labels={'Descrição': 'Odor', 'frequencia': 'Frequência'}
    )

    # Atualizar o layout do gráfico
    fig.update_layout(
        plot_bgcolor='black',  # Fundo do gráfico preto
        paper_bgcolor='black',  # Fundo do papel preto
        font_color='white',     # Cor da fonte branca para contraste
        xaxis=dict(
            showgrid=False,
            tickangle=-45,  # Inclinar os rótulos do eixo x para melhor legibilidade
        ),
        yaxis=dict(showgrid=False),
        bargap=0.2,  # Ajustar o espaço entre as barras
        xaxis_title='Odores',
        yaxis_title='Frequência'
    )

    # Aumentar o tamanho das barras
    fig.update_traces(marker=dict(line=dict(width=2, color='white')))

    # Exibir o gráfico
    fig.show()

def grafico_total(caminho_arquivo):
    # Carregar o arquivo CSV
    # Altere o caminho 'caminho_do_arquivo.csv' para o local correto do seu arquivo
    df = pd.read_csv(caminho_arquivo)

    # Contar os 10 odores mais frequentes na coluna 'descrição'
    top_10_odor_count = Counter(df['Descrição']).most_common(81)

    # Criar um novo DataFrame com os 10 odores mais frequentes
    top_10_df = pd.DataFrame(top_10_odor_count, columns=['Descrição', 'frequencia'])

    # Criar o histograma com uma escala de cor de tons de azul, fundo preto, barras grandes e sem grade
    fig = px.bar(
        top_10_df,
        x='Descrição',
        y='frequencia',
        color='frequencia',
        color_continuous_scale='Blues',  # Escala de cor de tons de azul
        title='Top 100 sub odores do dataset de validação',
        labels={'Descrição': 'Odor', 'frequencia': 'Frequência'}
    )

    # Atualizar o layout do gráfico
    fig.update_layout(
        plot_bgcolor='black',  # Fundo do gráfico preto
        paper_bgcolor='black',  # Fundo do papel preto
        font_color='white',     # Cor da fonte branca para contraste
        xaxis=dict(
            showgrid=False,
            tickangle=-45,  # Inclinar os rótulos do eixo x para melhor legibilidade
        ),
        yaxis=dict(showgrid=False),
        bargap=0.2,  # Ajustar o espaço entre as barras
        xaxis_title='Odores',
        yaxis_title='Frequência'
    )

    # Aumentar o tamanho das barras
    fig.update_traces(marker=dict(line=dict(width=2, color='white')))

    # Exibir o gráfico
    fig.show()


grafico_total('descricoes_sub_val.csv')

