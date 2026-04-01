import pandas as pd

# Criando o DataFrame com os dados que você forneceu
data = {
    'Série': ['One Piece', 'Asterix', 'Golgo 13', 'Dragon Ball', 'Naruto', 'Tintin', 'Demon Slayer'],
    'Editora': ['Shueisha', 'Dargaud', 'Shogakukan', 'Shueisha', 'Shueisha', 'Casterman', 'Shueisha'],
    'Volumes': [114, 41, 219, 42, 72, 24, 23],
    'Vendas_Milhoes': [600, 393, 300, 260, 250, 250, 220]
}

df = pd.DataFrame(data)

def analisar_quadrinhos():
    print("--- 📚 SISTEMA DE ANÁLISE DE QUADRINHOS ---")
    
    # 1. Ranking de Vendas
    top_vendas = df.sort_values(by='Vendas_Milhoes', ascending=False).head(3)
    print("\n🏆 Top 3 em Vendas Totais:")
    print(top_vendas[['Série', 'Vendas_Milhoes']])
    
    # 2. Cálculo de Eficiência (Vendas por Volume)
    df['Vendas_por_Volume'] = (df['Vendas_Milhoes'] / df['Volumes']).round(2)
    mais_eficiente = df.loc[df['Vendas_por_Volume'].idxmax()]
    
    print(f"\n⚡ Série com maior densidade de vendas: {mais_eficiente['Série']}")
    print(f"Média de {mais_eficiente['Vendas_por_Volume']} milhões de cópias por volume lançado.")

    # 3. Market Share Simples
    print("\n📊 Títulos por Editora na amostra:")
    print(df['Editora'].value_counts())

if __name__ == "__main__":
    analisar_quadrinhos()