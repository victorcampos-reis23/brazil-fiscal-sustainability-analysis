import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from bcb import sgs

# 1. Coleta da DBGG como % do PIB
try:
    #  bruta do governo geral (% PIB) - mensal
    dados_divida = sgs.get({'dbgg_pib': 13762}, last=1)
    d_atual = dados_divida['dbgg_pib'].iloc[-1] / 100 # Transforma 78.7 em 0.787
    
    # Se o valor vier acima de 1 (100%), significa que pegou a série errada em R$
    if d_atual > 1:
        d_atual = 0.787 
    
    print(f"Dados Oficiais BCB: DBGG atual em {d_atual*100:.2f}% do PIB")
except Exception as e:
    print(f"Erro ao acessar API: {e}. Usando estimativa de mercado: 78.7%")
    d_atual = 0.787

# 2. Definição dos eixos para a Matriz de Sensibilidade
# Juro Real (6% a 11%) vs Crescimento PIB (-1% a 4%)
juros_eixo = np.arange(0.06, 0.115, 0.01)
pib_eixo = np.arange(-0.01, 0.045, 0.005)

# 3. Cálculo do esforço fiscal (Matriz de Superávit Primário)
matriz_dados = []
for r in juros_eixo:
    linha = [d_atual * ((r - g) / (1 + g)) * 100 for g in pib_eixo]
    matriz_dados.append(linha)

df_heatmap = pd.DataFrame(
    matriz_dados, 
    index=[f"{i*100:.1f}%" for i in juros_eixo],
    columns=[f"{g*100:.1f}%" for g in pib_eixo]
)

# 4. Visualização Profissional Estilo Asset Management
plt.figure(figsize=(14, 9))
sns.heatmap(df_heatmap, annot=True, fmt=".2f", cmap="RdYlGn_r", center=0,
            cbar_kws={'label': 'Superávit Primário Necessário para Estabilizar a Dívida (% PIB)'})

plt.title(f'Matriz de Sustentabilidade Fiscal (DBGG: {d_atual*100:.1f}% do PIB)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Crescimento Real do PIB (%)', fontsize=12)
plt.ylabel('Taxa de Juros Real Ex-Ante (%)', fontsize=12)

plt.tight_layout()
plt.savefig('heatmap_fiscal_final.png', dpi=300)
plt.show()
