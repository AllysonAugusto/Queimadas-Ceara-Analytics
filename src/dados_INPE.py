"""
Extração INPE Queimadas
- Anual (CE):  .../csv/anual/EstadosBr_sat_ref/CE/focos_br_ce_ref_{ano}.zip
- Mensal (Brasil): .../csv/mensal/Brasil/focos_mensal_br_{yyyymm}.zip
"""

import os
import zipfile
import requests
import pandas as pd
from typing import List, Optional

# -----------------------------
# Helpers genéricos
# -----------------------------
def _baixar_arquivo_zip(url: str, pasta_destino: str, nome_zip: str) -> Optional[str]:
    """Baixa um ZIP para pasta_destino/nome_zip e retorna o caminho salvo."""
    os.makedirs(pasta_destino, exist_ok=True)
    zip_path = os.path.join(pasta_destino, nome_zip)
    print(f"Baixando: {url}")
    try:
        with requests.get(url, stream=True, timeout=60) as r:
            r.raise_for_status()
            with open(zip_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print(f"✓ ZIP salvo em: {zip_path}")
        return zip_path
    except requests.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")
        return None
    except OSError as e:
        print(f"Erro ao salvar {zip_path}: {e}")
        return None

def _extrair_zip(zip_path: str, pasta_destino: str) -> bool:
    """Extrai todos os arquivos do ZIP para a pasta_destino."""
    try:
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(pasta_destino)
        print(f"✓ Arquivos extraídos em: {pasta_destino}")
        return True
    except zipfile.BadZipFile:
        print("Erro: ZIP corrompido.")
    except Exception as e:
        print(f"Erro ao extrair ZIP: {e}")
    return False

def ler_csv_extraido(pasta_raiz: str) -> Optional[List[pd.DataFrame]]:
    """Lê todos os .csv encontrados na pasta (após extração)."""
    try:
        arquivos = os.listdir(pasta_raiz)
        csvs = [a for a in arquivos if a.lower().endswith(".csv")]
        if not csvs:
            print("Nenhum CSV encontrado na pasta.")
            return None
        dfs = []
        for nome in csvs:
            caminho = os.path.join(pasta_raiz, nome)
            print(f"Lendo CSV: {caminho}")
            df = pd.read_csv(caminho, sep=",", encoding="utf-8", low_memory=False)
            dfs.append(df)
        return dfs
    except Exception as e:
        print(f"Erro ao ler CSVs: {e}")
        return None

# -----------------------------
# Fluxo 1 — ANUAL (CE) — mantém seu original, usando helpers
# -----------------------------
def baixar_dados_ce(ano: int, pasta_raiz: str = "dados_ceara") -> Optional[str]:
    """
    Baixa e extrai o ZIP anual do CE para o ano informado.
    Retorna o caminho da pasta do ano (ou None em caso de erro).
    """
    url = (f"https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/anual/"
           f"EstadosBr_sat_ref/CE/focos_br_ce_ref_{ano}.zip")
    print(f"Baixando dados anuais do CE - {ano} ...")

    pasta_ano = os.path.join(pasta_raiz, f"ano_{ano}")
    nome_zip = f"focos_br_ce_ref_{ano}.zip"
    zip_path = _baixar_arquivo_zip(url, pasta_ano, nome_zip)
    if not zip_path:
        return None

    if not _extrair_zip(zip_path, pasta_ano):
        return None

    return pasta_ano

# -----------------------------
# Fluxo 2 — MENSAL (Brasil)
# -----------------------------
def baixar_dados_mensal_brasil(ano: int, mes: int, pasta_raiz: str = "dados_brasil_mensal") -> Optional[str]:
    """
    Baixa e extrai o ZIP mensal do Brasil para ano+mes (1..12).
    Retorna o caminho da pasta do yyyymm (ou None em caso de erro).
    """
    if not (1 <= mes <= 12):
        print("Mês inválido (use 1..12).")
        return None

    yyyymm = f"{ano}{mes:02d}"
    url = (f"https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/mensal/Brasil/"
           f"focos_mensal_br_{yyyymm}.zip")
    print(f"Baixando dados mensais do Brasil - {yyyymm} ...")

    pasta_mes = os.path.join(pasta_raiz, f"{yyyymm}")
    nome_zip = f"focos_mensal_br_{yyyymm}.zip"
    zip_path = _baixar_arquivo_zip(url, pasta_mes, nome_zip)
    if not zip_path:
        return None

    if not _extrair_zip(zip_path, pasta_mes):
        return None

    return pasta_mes

def baixar_intervalo_mensal_brasil(ano_inicio: int, mes_inicio: int,
                                   ano_fim: int, mes_fim: int,
                                   pasta_raiz: str = "dados_brasil_mensal") -> List[str]:
    """
    Baixa vários meses de uma vez (inclusive limites) e retorna
    a lista de pastas extraídas com sucesso.
    """
    pastas_ok = []
    ai, mi = ano_inicio, mes_inicio
    af, mf = ano_fim, mes_fim

    # Iteração (ano,mes) simples
    ano, mes = ai, mi
    while (ano < af) or (ano == af and mes <= mf):
        pasta = baixar_dados_mensal_brasil(ano, mes, pasta_raiz=pasta_raiz)
        if pasta:
            pastas_ok.append(pasta)
        # Próximo mês
        mes += 1
        if mes == 13:
            mes = 1
            ano += 1
    return pastas_ok

# -----------------------------
# Execução direta
# -----------------------------
if __name__ == "__main__":
    print("Escolha o modo:\n 1) Anual CE\n 2) Mensal Brasil")
    modo = input("Digite 1 ou 2: ").strip()

    if modo == "1":
        ano_str = input("Ano (ex: 2023): ").strip()
        try:
            ano = int(ano_str)
        except ValueError:
            print("Ano inválido.")
            exit(1)

        pasta = baixar_dados_ce(ano)
        if pasta:
            print("\nDownload e extração concluídos (CE/Anual).")
            dfs = ler_csv_extraido(pasta)
            if dfs:
                print("-=" * 40)
                print(dfs[0].head())
    elif modo == "2":
        escolha = input("a) um mês  b) intervalo de meses  [a/b]: ").strip().lower()
        if escolha == "a":
            ano = int(input("Ano (ex: 2023): ").strip())
            mes = int(input("Mês (1..12): ").strip())
            pasta = baixar_dados_mensal_brasil(ano, mes)
            if pasta:
                print("\nDownload e extração concluídos (Brasil/Mensal).")
                dfs = ler_csv_extraido(pasta)
                if dfs:
                    print("-=" * 40)
                    print(dfs[0].head())
        else:
            ai = int(input("Ano início (ex: 2023): ").strip())
            mi = int(input("Mês início (1..12): ").strip())
            af = int(input("Ano fim (ex: 2023): ").strip())
            mf = int(input("Mês fim (1..12): ").strip())
            pastas = baixar_intervalo_mensal_brasil(ai, mi, af, mf)
            print(f"\nConcluídos: {len(pastas)} mês(es). Ex.: {pastas[:3]}")
            # (Opcional) concatenar tudo:
            if pastas:
                todos = []
                for p in pastas:
                    dfs = ler_csv_extraido(p) or []
                    todos.extend(dfs)
                if todos:
                    df_all = pd.concat(todos, ignore_index=True)
                    print("-=" * 40)
                    print("Prévia do consolidado mensal:")
                    print(df_all.head())
    else:
        print("Opção inválida.")
