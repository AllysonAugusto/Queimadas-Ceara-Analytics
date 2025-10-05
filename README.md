# Queimadas Ceará Analytics

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-suportado-orange)

![Capa do Projeto](./imagens/capa_powerbi.png)  
*Visualização de monitoramento interativo das queimadas no Ceará.*

---

## 🎯 Objetivo do Projeto
Desenvolver um **sistema de monitoramento interativo de queimadas** no Ceará, utilizando **Python** para coleta e tratamento de dados e **Power BI** para visualização, permitindo:

- Identificar áreas mais afetadas por queimadas.  
- Acompanhar evolução temporal (ano a ano, mês a mês).  
- Relacionar queimadas com variáveis climáticas (chuva, seca, temperatura).  
- Apoiar conscientização ambiental e políticas públicas.

---

## 🔹 Fontes de Dados
- **INPE – Programa Queimadas**: dados de focos de calor via satélite.  
- **INMET – Instituto Nacional de Meteorologia**: chuvas, temperatura e umidade no Ceará.  
- **MapBiomas** ( alertas de desmatamento de vegetação nativa em todos os biomas brasileiros)

---

## ⚙️ Etapas Técnicas

### 1. Coleta de Dados (Python)
- Extrair dados da **API do INPE Queimadas** para focos ativos no Ceará.  
- Organizar e tratar informações com `pandas` ou `polars` (data, localização geográfica, intensidade).  
- Coletar dados climáticos do **INMET** para análise de correlação entre seca/chuva e incêndios.

### 2. Tratamento de Dados (Python)
- Limpeza de dados: valores faltantes, formatação de datas.  
- Criação de variáveis adicionais:
  - Número de focos por município/ano.  
  - Tendência de aumento/diminuição.  
  - Relação entre focos de queimadas e períodos de seca.

### 3. Integração com Power BI
- Exportação dos dados tratados (CSV ou conexão direta com banco de dados).  
- Criação de dashboards interativos:
  - 📊 Séries temporais: evolução dos focos de calor.  
  - 🗺️ Mapas do Ceará com hotspots de queimadas.  
  - 📉 Correlação entre chuvas e incêndios.  
  - 📌 Ranking dos municípios mais afetados.

---

## 📊 Resultado Esperado
Dashboard interativo em Power BI, permitindo identificar:

- Onde ocorrem mais queimadas no Ceará.  
- Variação ao longo do ano.  
- Relação entre seca/chuva e incêndios.  

---
