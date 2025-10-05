"""
Extraindo dados meteorológicos do CE por ano
"""

import datetime as dt
from pathlib import Path
import zipfile
import pandas as pd
import requests
from tqdm import tqdm


# Gerar URL do arquivo por determinado ano
def gerar_url(ano: int) -> str:
    return f"https://portal.inmet.gov.br/uploads/dadoshistoricos/{ano}.zip"

# Baixar arquivo de um ano específico
def baixar_ano(ano: int, pasta_destino: Path) -> Path:
    pasta_destino.mkdir(exist_ok=True)  # Cria a pasta se não existir
    arquivo_local = pasta_destino / f"inmet_{ano}.zip"

    if arquivo_local.exists():
        print(f"{arquivo_local.name} já existe, pulando download")
        return arquivo_local
    
    url = gerar_url(ano)
    with requests.get(url, stream=True) as r:
        total = int(r.headers.get("content-length", 0))
        with open(arquivo_local, "wb") as f, tqdm(
            total=total, unit="iB", unit_scale=True, desc=str(ano)
        ) as barra:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
                barra.update(len(chunk))
    return arquivo_local

# Renomear colunas para nomes mais simples
def renomear_colunas(df: pd.DataFrame) -> pd.DataFrame:
    mapa = {
        "Data": "data",
        "Hora": "hora",
        "Precipitacao": "precipitacao",
        "Temp": "temperatura_ar",
        "Temp_Max": "temperatura_maxima",
        "Temp_Min": "temperatura_minima",
        "Umidade": "umidade_relativa",
        "Vento": "vento_velocidade",
    }
    return df.rename(columns=lambda x: mapa.get(x, x).lower())

# Ler todos os CSVs do Ceará dentro do ZIP
def ler_zip_inmet_ce(caminho_zip: Path) -> pd.DataFrame:
    dados = []
    with zipfile.ZipFile(caminho_zip) as z:
        arquivos_ce = [a for a in z.namelist() if a.lower().endswith(".csv") and "_ce_" in a.lower()]
        print(f"{len(arquivos_ce)} arquivos do CE encontrados")
        
        for arquivo in arquivos_ce:
            print("Lendo CSV:", arquivo)
            df = pd.read_csv(
                z.open(arquivo),
                sep=";",
                decimal=",",
                encoding="latin-1",
                skiprows=8,
                na_values="-9999",
                usecols=range(19),
            )
            df = renomear_colunas(df)
            
            if "hora" in df.columns:
                df["data_hora"] = pd.to_datetime(df["data"] + " " + df["hora"].str[:5])
                df = df.drop(columns=["data", "hora"])
            else:
                df["data_hora"] = pd.to_datetime(df["data"])
                df = df.drop(columns=["data"])
            
            dados.append(df)
    
    if not dados:
        raise ValueError("Nenhum CSV do Ceará foi encontrado no ZIP!")
    
    return pd.concat(dados, ignore_index=True)


entrada = input("Digite os anos que deseja baixar (ex: 2021,2022,2023): ")
anos = [int(a.strip()) for a in entrada.split(",")]

pasta = Path("dados")
todos_dfs = []

for ano in anos:
    zip_ano = baixar_ano(ano, pasta)    
    df_ano = ler_zip_inmet_ce(zip_ano)    
    todos_dfs.append(df_ano)

# Concatena DataFrame
df_ce = pd.concat(todos_dfs, ignore_index=True)

arquivo_saida = pasta / f"inmet_ce_{anos[0]}_{anos[-1]}.csv"
df_ce.to_csv(arquivo_saida, index=False)
print("Arquivo CSV do Ceará salvo em:", arquivo_saida)
