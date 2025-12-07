# queimadas-ceara-analytics

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-suportado-orange)

## Monitoramento de Queimadas e Impactos Ambientais no Ceará

Este repositório reúne scripts em Python e um relatório Power BI usados para
monitorar as queimadas no estado do Ceará e compará-las com o restante do Brasil.
A partir dos dados do INPE, INMET e MapBiomas são calculados, por exemplo:

- séries temporais de focos de queimadas por dia, mês e ano;
- médias diárias de focos e número de dias secos no período;
- chuva total e chuva média em cada recorte de tempo;
- participação do Ceará no total de focos do Brasil (% e ranking entre os estados);
- área queimada por bioma, com destaque para a Caatinga.

Com esses indicadores, o projeto permite acompanhar a evolução das queimadas no CE,
comparar o estado com outros estados brasileiros e relacionar os focos com o clima
e com a dinâmica dos biomas.

---

## Objetivos

- Monitorar a distribuição espacial e temporal de queimadas no Ceará.
- Comparar o comportamento do Ceará com outros estados brasileiros.
- Relacionar focos de queimadas com variáveis climáticas (chuva, dias secos).
- Avaliar a participação da Caatinga na área queimada total dos biomas brasileiros.
- Disponibilizar dashboards interativos e reprodutíveis.

---

## Stack Tecnológica

- **Python** – organização e preparação dos dados (INPE, INMET, MapBiomas).
- **Pandas / Jupyter** – limpeza, junção e exportação para `.csv`.
- **Power BI Desktop** – modelagem de dados, criação de medidas DAX e dashboards.
- **Fontes oficiais**:
  - INPE – Programa Queimadas (focos de calor por estado e por coordenada).
  - INMET – séries de precipitação e variáveis meteorológicas para o Ceará.
  - MapBiomas – área queimada por bioma e dados de desmatamento  
    *(coletados manualmente no site oficial e salvos na pasta `dados/outros`)*.

---

## 📂 Estrutura do projeto

Ajuste conforme o seu repositório real:

```text
.
├── dados/
│   ├── inpe/             # dados brutos do INPE (coletados via scripts Python)
│   ├── inmet/            # dados brutos do INMET (coletados via scripts Python)
│   └── outros/           # arquivos coletados manualmente (ex.: MapBiomas)
├── imagens/              # figuras e prints dos dashboards
├── src/                  # scripts Python de tratamento e coleta
├── powerbi/
│   └── queimadas_ceara.pbix   # arquivo principal do Power BI
├── requirements.txt
└── README.md
   ```


## Como executar

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/<seu-usuario>/queimadas-ceara-analytics.git
   cd queimadas-ceara-analytics
   ```

```bash
python -m venv .venv
```

# Windows
```bash
.venv\Scripts\activate
```
# Linux/Mac
```bash
source .venv/bin/activate
```
```bash
pip install -r requirements.txt
```

