import pandas as pd
import requests
import zipfile
import os

#Baixar dados
def baixar_dados_ce(ano, pasta_raiz="dados_ceara"):
  url = f"https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/anual/EstadosBr_sat_ref/CE/focos_br_ce_ref_{ano}.zip"
  print(f"Baixando dados do ano {ano}...")

  try:
    resposta = requests.get(url, stream=True)
    resposta.raise_for_status()
  except requests.RequestException as e:
    print(f"Erro ao baixar dados do ano {ano}: {e}")
    return None

  #Pasta do ano
  pasta_ano = os.path.join(pasta_raiz, f"ano_{ano}")
  os.makedirs(pasta_ano, exist_ok=True)

  #Salvar zip
  try:
    zip_path = os.path.join(pasta_ano, f"focos_br_ce_ref_{ano}.zip")
    with open(zip_path, "wb") as f:
      for chunk in resposta.iter_content(chunk_size=8192):
        f.write(chunk)

    print(f"Dados do ano {ano} baixados.")
  except OSError as e:
    print(f"Erro ao salvar o arquivo zip: {e}")
    return None

#Extrair todos os arquivos do zip
  try:
    with zipfile.ZipFile(zip_path, "r") as z:
      z.extractall(pasta_ano)
      print(f"\nTodos os arquivos extraidos em: {pasta_ano}")
  except zipfile.BadZipFile as e:
    print("Erro: Zip corrompido")
    return None
  except Exception as e:
    print(f"Erro ao extrair ZIP:{e}")
    return None

  return pasta_ano


def ler_csv_extraido(pasta_raiz):
  try:
    arquivos = os.listdir(pasta_raiz)
    arquivos_csv = [arquivo for arquivo in arquivos if arquivo.endswith(".csv")]
    
    
    if not arquivos_csv:
      print("Nenhum arquivo CSV encontrado na pasta extraida")
      return None

    dfs = []

    for arquivo in arquivos_csv:
      caminho_csv = os.path.join(pasta_raiz, arquivo)
      print(f"\nLendo arquivo CSV: {caminho_csv}")

      df = pd.read_csv(caminho_csv, sep=",", encoding="utf-8", low_memory=False)

      dfs.append(df)

    return dfs

  except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    return None

if __name__ == "__main__":
  ano = input("Digite o ano desejado (ex: 2023): ")

  try:
    ano = int(ano)
  except ValueError:
    print("Ano inválido. Certifique-se de digitar um número inteiro.")
    exit()

  pasta = baixar_dados_ce(ano)
  if pasta:
    print("\nDownload e extração concluidos.")

    dfs = ler_csv_extraido(pasta)
    if dfs:
      print("-=-=-=-=" * 30)
      print(dfs[0].head())
