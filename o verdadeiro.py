# PROJETO INTERDISCIPLINAR: QUADRINHOS MAIS VENDIDOS
import pandas as pd

# 1. BASE DE DADOS (Simulando o Banco de Dados dentro do código)
dados = {
    'Série': ['One Piece', 'Asterix', 'Golgo 13', 'Dragon Ball', 'Naruto', 'Tintin', 'Case Closed'],
    'Editora': ['Shueisha', 'Dargaud', 'Shogakukan', 'Shueisha', 'Shueisha', 'Casterman', 'Shogakukan'],
    'Volumes': [114, 41, 219, 42, 72, 24, 107],
    'Vendas_Milhoes': [600, 393, 300, 260, 250, 250, 270]
}

df = pd.DataFrame(dados)

def demonstrar_sistema():
    print("="*50)
    print("SISTEMA DE ANÁLISE ESTATÍSTICA DE QUADRINHOS")
    print("="*50)
    
    # Exibindo os dados brutos
    print("\n[TABELA DE DADOS CARREGADA]:")
    print(df.to_string(index=False))
    
    # Ciência de Dados: Cálculo de Vendas por Volume
    df['Eficiencia'] = (df['Vendas_Milhoes'] / df['Volumes']).round(2)
    
    print("\n" + "-"*50)
    print("ESTUDO DE CIÊNCIA DE DADOS: EFICIÊNCIA")
    print("-"*50)
    top_eficiente = df.loc[df['Eficiencia'].idxmax()]
    print(f"A série mais eficiente é '{top_eficiente['Série']}'")
    print(f"com {top_eficiente['Eficiencia']} milhões de vendas por volume.")

    # GERANDO GRÁFICO EM MODO TEXTO (Para funcionar no Online Python)
    print("\n" + "-"*50)
    print("GRÁFICO DE VENDAS TOTAIS (Milhões de Cópias)")
    print("-"*50)
    
    for index, row in df.iterrows():
        # Cria uma barra proporcional ao valor de vendas
        barra = "█" * int(row['Vendas_Milhoes'] / 20) 
        print(f"{row['Série'][:12]:<12} | {barra} {row['Vendas_Milhoes']}M")
    
    print("-"*50)
    print("Legenda: Cada █ representa 20 milhões de cópias.")

if __name__ == "__main__":
    demonstrar_sistema()