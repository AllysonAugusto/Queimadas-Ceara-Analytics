# queimadas-ceara-analytics

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-suportado-orange)

**Tema:** Monitoramento das Queimadas e Impactos Ambientais no Ceará com Python + Power BI

### 🎯 Objetivo do Projeto
Desenvolver um sistema de monitoramento interativo de queimadas no Ceará, utilizando Python para coletar e tratar dados e Power BI para visualização interativa, permitindo:

- Identificar áreas mais afetadas por queimadas.  
- Acompanhar evolução temporal (ano a ano, mês a mês).  
- Relacionar queimadas com variáveis climáticas (chuva, seca, temperatura).  
- Promover a conscientização ambiental e apoio a políticas públicas.

### 🔹 Fontes de Dados
- **INPE – Programa Queimadas** (dados de focos de calor via satélite)  
- **INMET – Instituto Nacional de Meteorologia** (chuvas, temperatura, umidade no Ceará)  
- **IBGE** (dados populacionais para cruzar impacto humano)

### ⚙️ Etapas Técnicas
1. **Coleta de Dados (Python)**
   - Usar API do INPE Queimadas para extrair dados de focos ativos no Ceará.  
   - Usar `pandas` ou `polars` para organizar e tratar as informações (data, localização geográfica, intensidade).  
   - Extrair dados climáticos do INMET para correlacionar seca/chuva com incêndios.

2. **Tratamento (Python)**
   - Limpeza dos dados (valores faltantes, formatação de datas).  
   - Criação de variáveis adicionais:
     - Nº de focos por município/ano.  
     - Tendência de aumento/diminuição.  
     - Relação focos x período de seca.

3. **Integração com Power BI**
   - Exportar os dados tratados pelo Python (CSV ou conexão direta com banco).  
   - Criar painéis com:
     - 📊 Séries temporais (focos de calor ao longo dos anos).  
     - 🗺️ Mapas do Ceará com hotspots das queimadas.  
     - 📉 Correlação entre chuvas e queimadas.  
     - 📌 Ranking dos municípios mais afetados.

### 📊 Resultado Esperado
Dashboard em Power BI que qualquer pessoa pode interagir e entender:

- Onde ocorrem mais queimadas no Ceará.  
- Como elas variam ao longo do ano.  
- Relação entre seca/chuva e os incêndios.

